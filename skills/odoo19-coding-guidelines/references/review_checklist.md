# Review Checklist

Use this checklist before finalizing a change or when reviewing an Odoo module.

## Module layout

- Files are in the expected directories.
- File names are lowercase alphanumeric with underscores.
- Security, views, reports, wizards, static assets, and demo data are not mixed without a local convention.

## XML

- Records use stable, meaningful external ids.
- `<record>` attributes and `<field>` attributes follow guideline order in new code.
- `<data>` is reserved for noupdate use.
- Production data and demo data are split.
- QWeb output does not introduce unsafe HTML.

## Python and ORM

- Names are meaningful and match Odoo conventions.
- Python string literals use single quotes in new or modified code, except docstrings or cases where double quotes avoid escaping.
- Field suffixes match field types.
- Model class members are in conventional order.
- Action methods use `self.ensure_one()` when single-record.
- Translatable strings are built inside `_()` with appropriate placeholders.
- Changes do not add handwritten `i18n/*.po`; translations are exported from Odoo.
- Code favors ORM operations unless SQL is justified.

## Frontend

- JS, XML templates, and SCSS live under `static/src`.
- OWL/components/services use Odoo registry and service patterns.
- Styles use `o_<module>` classes and avoid id selectors.
- SCSS variables and property order are consistent.

## Security

- Public methods do not trust RPC parameters.
- Access rules, company boundaries, ownership, and state transitions are enforced server-side.
- `sudo()` is justified and narrow.
- Raw SQL is parameterized.
- Dynamic domains and field names are validated.
- HTML is escaped or sanitized according to intent.
- `eval` is absent; safer parsers are used where possible.

## Final response

When reporting work, mention the guideline areas actually touched, not every rule in this skill.
