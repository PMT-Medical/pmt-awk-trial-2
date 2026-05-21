import os
import pathlib
import subprocess
import sys
import tempfile
import unittest


SEED_FILES = [
    "README.md",
    "docs/CONTEXT.md",
    "docs/NEXT.md",
    "github/labels.yml",
    ".github/ISSUE_TEMPLATE/prd.yml",
    ".github/ISSUE_TEMPLATE/vertical-slice.yml",
]


def _make_full_tree(root: pathlib.Path) -> None:
    for rel in SEED_FILES:
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.touch()


class TestCheckSeedArtifacts(unittest.TestCase):
    def test_success_when_all_files_present(self):
        from scripts.trial_seed_check import check_seed_artifacts

        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            _make_full_tree(root)
            ok, missing = check_seed_artifacts(root)

        self.assertTrue(ok)
        self.assertEqual(missing, [])

    def test_failure_reports_missing_file(self):
        from scripts.trial_seed_check import check_seed_artifacts

        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            _make_full_tree(root)
            (root / "docs" / "CONTEXT.md").unlink()
            ok, missing = check_seed_artifacts(root)

        self.assertFalse(ok)
        self.assertIn("docs/CONTEXT.md", missing)

    def test_failure_reports_all_missing_files(self):
        from scripts.trial_seed_check import check_seed_artifacts

        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            ok, missing = check_seed_artifacts(root)

        self.assertFalse(ok)
        self.assertEqual(len(missing), len(SEED_FILES))

    def test_cli_exits_zero_for_real_repo(self):
        repo_root = pathlib.Path(__file__).parent.parent
        result = subprocess.run(
            [sys.executable, str(repo_root / "scripts" / "trial_seed_check.py")],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
        self.assertIn("OK", result.stdout)
