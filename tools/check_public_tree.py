"""Default-deny checks for the reviewed public Git tree; independent of ignore rules."""
import json
import gzip
from pathlib import Path, PurePosixPath
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PRIVATE_PARTS = {'analysis', 'reverse', 'validation', 'publication', '__pycache__', '.pytest_cache', '.venv'}
PRIVATE_NAMES = {'agents.md', 'agent.md', 'reconstruction_plan.md'}
SECRETS = re.compile(r'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}|sk-[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{16})\b')
PERSONAL_PATH = re.compile(r'(?:[A-Za-z]:[\\/]+[Uu]sers[\\/]+[^\s\\/]+|/[Uu]sers/[^/\s]+|/[Hh]ome/[^/\s]+)')


def check_path(path, allowed):
    p = PurePosixPath(path)
    parts = {part.lower() for part in p.parts}
    if parts & PRIVATE_PARTS or p.name.lower() in PRIVATE_NAMES:
        return 'private development material'
    if p.suffix.lower() in {'.swf', '.fla', '.log', '.db', '.zip'} or p.name.startswith('.env'):
        return 'excluded source, log, database, archive or environment file'
    if path not in allowed:
        return 'not in the reviewed publication allowlist'
    return None


def main():
    allowed = set(json.loads((ROOT / 'public-files.json').read_text(encoding='utf-8')))
    entries = subprocess.check_output(['git', 'ls-files', '--stage', '-z'], cwd=ROOT).decode().split('\0')
    errors = []
    reviewed = []
    for entry in entries:
        if not entry:
            continue
        metadata, path = entry.split('\t', 1)
        reason = check_path(path, allowed)
        if metadata.split()[0] not in ('100644', '100755'):
            reason = 'symlink/submodule or unexpected Git file mode'
        if reason:
            errors.append(f'{path}: {reason}')
            continue
        reviewed.append((metadata.split()[1], path))
    missing = allowed - {entry.split('\t', 1)[1] for entry in entries if entry}
    errors.extend(f'{path}: allowlisted file is missing from the index' for path in sorted(missing))
    # Read staged objects, including compressed metadata; do not trust worktree bytes.
    payload = subprocess.check_output(['git', 'cat-file', '--batch'], cwd=ROOT,
        input=''.join(oid+'\n' for oid, _ in reviewed).encode())
    offset = 0
    for _, path in reviewed:
        end = payload.index(b'\n', offset)
        size = int(payload[offset:end].split()[-1])
        data = payload[end+1:end+1+size]
        offset = end+size+2
        if data.startswith(b'version https://git-lfs.github.com/spec'):
            errors.append(f'{path}: unreviewed LFS pointer')
        if path.endswith('.json.gz'):
            data = gzip.decompress(data)
        text = data.decode('utf-8', 'replace')
        wide_text = data[:len(data)//2*2].decode('utf-16-le', 'replace')
        big_endian_text = data[:len(data)//2*2].decode('utf-16-be', 'replace')
        if any(SECRETS.search(s) or PERSONAL_PATH.search(s) for s in (text, wide_text, big_endian_text)):
            errors.append(f'{path}: possible secret or personal filesystem path')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'Public-tree policy passed: {sum(bool(e) for e in entries)} tracked files reviewed.')


if __name__ == '__main__':
    main()
