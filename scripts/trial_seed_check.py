"""Read-only checker that validates expected trial-seed artifacts are present."""

import pathlib
import sys

SEED_FILES = [
    "README.md",
    "docs/CONTEXT.md",
    "docs/NEXT.md",
    "github/labels.yml",
    ".github/ISSUE_TEMPLATE/prd.yml",
    ".github/ISSUE_TEMPLATE/vertical-slice.yml",
]


def check_seed_artifacts(root: pathlib.Path) -> tuple[bool, list[str]]:
    missing = [rel for rel in SEED_FILES if not (root / rel).is_file()]
    return (len(missing) == 0, missing)


def main() -> int:
    root = pathlib.Path(__file__).parent.parent
    ok, missing = check_seed_artifacts(root)
    if ok:
        print(f"OK  all {len(SEED_FILES)} seed artifacts present")
        return 0
    print(f"FAIL  {len(missing)} seed artifact(s) missing:")
    for rel in missing:
        print(f"  - {rel}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
