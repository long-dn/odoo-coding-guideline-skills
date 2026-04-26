# odoo19-coding-guidelines

> Official Odoo 19 coding guideline reference for AI coding agents.

This skill helps assistants write and review Odoo modules with the official Odoo 19 coding style: module structure, XML records, Python idioms, Odoo naming conventions, translation export rules, JavaScript, SCSS, and security pitfalls.

## What it covers

- Module structure and file naming.
- XML record formatting, ids, data files, menus, views, and templates.
- Python readability, single-quote string style, idioms, imports, comments, and translations.
- Translation file rule: do not create handwritten `i18n/*.po`; use Odoo export.
- Odoo model, field, method, and class ordering conventions.
- JavaScript and OWL placement and review cues.
- SCSS naming, variables, selector hygiene, and property order.
- Security review for public methods, raw SQL, domains, HTML, eval, and dynamic field access.

## Install

```bash
npx skills add long-dn/odoo-coding-guideline-skills --skill odoo19-coding-guidelines
```

Install for a specific supported agent:

```bash
npx skills add long-dn/odoo-coding-guideline-skills --skill odoo19-coding-guidelines --agent codex
```

Supported agent ids: `codex`, `gemini-cli`, `claude-code`, `cursor`, `github-copilot`.

## Tested with

Test prompts live in `../../evals/odoo19-coding-guidelines/`. Run them manually against the skill to validate behavior.

## Modify

Edit `SKILL.md` or any file under `references/`, then validate from the repo root:

```bash
npx skills add . --list
```

## Sources

- Official Odoo 19 documentation: Coding guidelines.
- Official Odoo 19 documentation: Security in Odoo.
