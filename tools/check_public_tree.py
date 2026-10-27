"""Default-deny checks for the reviewed public Git tree; independent of ignore rules."""
import json
from pathlib import Path, PurePosixPath
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PRIVATE_PARTS = {'analysis', 'reverse', 'validation', 'publication', '__pycache__', '.pytest_cache', '.venv'}
PRIVATE_NAMES = {'agents.md', 'agent.md', 'reconstruction_plan.md'}
SECRETS = re.compile(r'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}|sk-[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{16})\b')
PERSONAL_PATH = re.compile(r'(?:[A-Za-z]:[\\/]Users[\\/][^\s\\/]+|/[Uu]sers/[^/\s]+|/[Hh]ome/[^/\s]+)')


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
        data = subprocess.check_output(['git', 'show', ':'+path], cwd=ROOT)
        if data.startswith(b'version https://git-lfs.github.com/spec'):
            errors.append(f'{path}: unreviewed LFS pointer')
        if Path(path).suffix in {'.py', '.md', '.json', '.yml', '.yaml', '.txt', '.toml', '.svg'}:
            text = data.decode('utf-8', 'replace')
            if SECRETS.search(text) or PERSONAL_PATH.search(text):
                errors.append(f'{path}: possible secret or personal filesystem path')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'Public-tree policy passed: {sum(bool(e) for e in entries)} tracked files reviewed.')


if __name__ == '__main__':
    main()
