---
name: odoo19-coding-guidelines
description: >-
  Official Odoo 19 coding guideline reference for AI coding agents. Use this
  skill before writing, modifying, or reviewing Odoo modules when the work
  involves module layout, file naming, XML records, Python style, ORM
  conventions, model/method/field naming, translations, `i18n/`, `.po`, `.pot`,
  translation export, JavaScript, SCSS, or security pitfalls. Trigger on Odoo
  coding requests such as "create an addon", "review this module", "fix this
  XML view", "write a model method", "add translations", "create a po file",
  "style this Odoo component", or any file under an Odoo addons directory. This
  skill complements syntax/version skills by focusing on maintainability, naming,
  structure, security, translation export discipline, and official coding style
  from the Odoo 19 coding guidelines.
---

# Odoo 19 Coding Guidelines

This skill keeps Odoo code aligned with the official Odoo 19 coding guidelines: readable, consistent, maintainable, translatable, and safe.

## Version and scope

This skill is written for Odoo 19 guidelines. If the project is clearly another Odoo version, still use the broad engineering principles, but avoid asserting version-specific details unless verified from that version's documentation.

When code syntax itself is the main risk, pair this skill with a version-specific syntax skill such as `odoo19-syntax`. This skill is about style and structure; it is not a replacement for migration or API reference checks.

## How to use this skill

Load only the reference files relevant to the current task:

| Task involves... | Load this reference |
|---|---|
| Addon tree, filenames, manifests, directories | `references/module_structure.md` |
| XML records, menus, actions, views, templates | `references/xml.md` |
| Python style, method structure, imports, translations | `references/python.md` |
| Translation files, `i18n/`, `.po`, `.pot`, translation export | `references/translations.md` |
| Odoo model names, fields, method naming, class ordering | `references/odoo_conventions.md` |
| JavaScript modules, services, components, comments | `references/javascript.md` |
| SCSS/CSS selectors, variables, property order | `references/scss.md` |
| Public methods, ORM bypass, domains, HTML, eval | `references/security.md` |
| Review checklist before final answer | `references/review_checklist.md` |

For a code review, load the domain references matching the changed files plus `references/security.md` and `references/review_checklist.md`.

## Workflow

1. Identify the touched domains from file paths and requested behavior.
2. Read the relevant references before changing code.
3. Preserve the existing module's local conventions when they do not conflict with the guideline.
4. Prefer small, idiomatic changes over broad rewrites.
5. Before final response or review findings, run the self-check below.

## Self-check

- Module files use lowercase `[a-z0-9_]` names and standard directories.
- XML records use consistent attribute order, grouped models, stable external ids, and minimal `<data>` wrappers.
- Python favors readability, meaningful names, idiomatic dict/list handling, and clear comments only where useful.
- Odoo names follow conventions: singular model names, `_id`/`_ids` suffixes, `_compute_*`, `_onchange_*`, `_check_*`, `action_*`.
- Model classes are ordered from private attributes to defaults, fields, constraints, compute methods, onchange/constraints, CRUD, actions, then business methods.
- Translatable strings keep interpolation inside `_()` and use named placeholders when multiple values are present.
- Do not manually create or edit `i18n/*.po`; use Odoo translation export/import workflows.
- JS and SCSS respect Odoo naming, structure, and formatting patterns.
- Security-sensitive code avoids unsafe public methods, raw SQL, unsafe domain construction, unescaped HTML, unsafe eval, and dynamic attribute access.

## What not to do

- Do not turn guideline compliance into unrelated refactors.
- Do not copy long text from Odoo documentation into user-facing answers.
- Do not create handwritten `.po` files. Generated translation files must come from Odoo's export workflow.
- Do not skip security review for controllers, public model methods, raw SQL, HTML/QWeb generation, or domain construction.
- Do not use this skill as proof that code is Odoo 19-compatible; verify syntax/API separately when needed.
