#!/usr/bin/env python3
"""
Scaffold a new skill under `skills/<name>/`.

Usage:
    python scripts/new_skill.py <skill-name> [--description "Short description"]
"""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"


SKILL_MD_TEMPLATE = """---
name: {name}
description: {description}
---

# {title}

Replace this opening paragraph with a one-sentence summary of what this skill does and when an AI assistant should consult it.

## How to use this skill

The detailed rules are split by domain in `references/`. Load only the references relevant to the current task.

| Task involves... | Load this reference |
|---|---|
| (domain A) | `references/<topic-a>.md` |
| (domain B) | `references/<topic-b>.md` |

## Workflow

1. Identify the task domain.
2. Load relevant references.
3. Apply the rules.
4. Self-check for common red flags before responding.
"""


README_TEMPLATE = """# {title}

> One-sentence description of what this skill does.

## Install

```bash
npx skills add long-dn/odoo-coding-guideline-skills --skill {name}
```

## Modify

Edit `SKILL.md` or any file under `references/`, then validate from the repo root:

```bash
npx skills add . --list
```
"""


CHANGELOG_TEMPLATE = """# Changelog - {name}

## [0.1.0] - {today}

Initial draft.
"""


EXAMPLE_REFERENCE = """# Example reference

Replace this placeholder with concrete rules and examples.
"""


EXAMPLE_EVAL = """# Test Case 1: Example prompt

## User Prompt

(Write a representative user prompt that should trigger this skill.)

## Expected output

(Sketch what the assistant should produce.)
"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise SystemExit(f"File already exists: {path}")
    path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name", help="Skill folder name, e.g. 'odoo19-coding-guidelines'")
    parser.add_argument(
        "--description",
        default="Short description of when an assistant should use this skill. Make it specific.",
        help="Description for the SKILL.md frontmatter",
    )
    args = parser.parse_args()

    name = args.name.strip().lower()
    if not name or not name.replace("-", "").replace("_", "").isalnum():
        sys.exit("Skill name must be alphanumeric with optional dashes/underscores")

    target = SKILLS_DIR / name
    if target.exists():
        sys.exit(f"Skill already exists: {target}")

    title = name.replace("-", " ").replace("_", " ").title()
    today = date.today().isoformat()

    write(target / "SKILL.md", SKILL_MD_TEMPLATE.format(name=name, description=args.description, title=title))
    write(target / "README.md", README_TEMPLATE.format(name=name, title=title))
    write(target / "CHANGELOG.md", CHANGELOG_TEMPLATE.format(name=name, today=today))
    write(target / "references" / "example.md", EXAMPLE_REFERENCE)
    write(ROOT / "evals" / name / "example.md", EXAMPLE_EVAL)

    print(f"Created skill at {target}")
    print("Next steps:")
    print(f"  1. Edit skills/{name}/SKILL.md")
    print(f"  2. Add reference files under skills/{name}/references/")
    print(f"  3. Add test prompts under evals/{name}/")
    print("  4. Run: npx skills add . --list")


if __name__ == "__main__":
    main()
