import importlib.util
from pathlib import Path
import unittest
import gzip

spec = importlib.util.spec_from_file_location('public_policy', Path(__file__).resolve().parents[1] / 'tools/check_public_tree.py')
policy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(policy)


class PublicationPolicyTests(unittest.TestCase):
    def test_compressed_assets_are_inspected_after_lossless_decompression(self):
        payload = ('C:'+chr(92)+'Users'+chr(92)+'example'+chr(92)+'asset').encode()
        compressed = gzip.compress(payload,mtime=0)
        for name in ('art.svgz','font.ttf.gz','effect.mp3.gz','scene.json.gz'):
            data = policy.decoded_content(name,compressed)
            self.assertEqual(data,payload)
            self.assertIsNotNone(policy.PERSONAL_PATH.search(data.decode()))

    def test_private_paths_rejected_even_if_allowlisted(self):
        for path in ('AGENTS.md', 'Agent.md', 'reverse/movie.xml', 'analysis/report.md',
                     'validation/screenshot.png', 'source.swf', '.env.secret'):
            self.assertIsNotNone(policy.check_path(path, {path}))

    def test_default_deny_and_reviewed_file(self):
        self.assertIsNotNone(policy.check_path('unreviewed.py', set()))
        self.assertIsNone(policy.check_path('wd2/runtime.py', {'wd2/runtime.py'}))
