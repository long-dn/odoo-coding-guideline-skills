# odoo-coding-guideline-skills

Public Odoo coding guideline skills for AI coding agents, distributed in the standard `SKILL.md` format.

This repository is installed with the open `skills` CLI only. It does not ship a custom installer and does not maintain provider-specific generated files.

## Install

Install by Odoo version. The Odoo version is selected through the skill name:

| Odoo version | Skill name | Install command |
|---|---|---|
| 19 | `odoo19-coding-guidelines` | `npx skills add long-dn/odoo-coding-guideline-skills --skill odoo19-coding-guidelines` |

Install it globally for your user:

```bash
npx skills add long-dn/odoo-coding-guideline-skills --skill odoo19-coding-guidelines --global
```

Install for a specific supported agent:

```bash
npx skills add long-dn/odoo-coding-guideline-skills --skill odoo19-coding-guidelines --agent codex
npx skills add long-dn/odoo-coding-guideline-skills --skill odoo19-coding-guidelines --agent claude-code
npx skills add long-dn/odoo-coding-guideline-skills --skill odoo19-coding-guidelines --agent cursor
npx skills add long-dn/odoo-coding-guideline-skills --skill odoo19-coding-guidelines --agent github-copilot
npx skills add long-dn/odoo-coding-guideline-skills --skill odoo19-coding-guidelines --agent gemini-cli
```

Supported agents in this repo:

| Agent | `skills` CLI agent id |
|---|---|
| Codex | `codex` |
| Gemini CLI | `gemini-cli` |
| Claude Code | `claude-code` |
| Cursor | `cursor` |
| GitHub Copilot | `github-copilot` |

## Available Skills

| Skill | What it covers | Status |
|---|---|---|
| [`odoo19-coding-guidelines`](./skills/odoo19-coding-guidelines/) | Official Odoo 19 coding guidelines for module structure, XML records/accessibility, Python style, ORM conventions, translation export, JS, SCSS, and security review | Initial |

## How It Works

Each skill lives under `skills/<name>/` and contains a standard `SKILL.md` file with YAML frontmatter:

```text
skills/odoo19-coding-guidelines/
├── SKILL.md
├── README.md
├── CHANGELOG.md
└── references/
```

Manual test prompts live outside the installable skill folders under `evals/<skill-name>/`.

## Add a New Skill

```bash
python scripts/new_skill.py my-new-skill --description "When to use this skill"
```

Then edit the generated files under `skills/my-new-skill/` and add a row to the Available Skills table above.

## Validate

```bash
npx skills add . --list
npx skills add . --skill odoo19-coding-guidelines --agent codex --copy
```

## License

MIT. See [LICENSE](./LICENSE).
