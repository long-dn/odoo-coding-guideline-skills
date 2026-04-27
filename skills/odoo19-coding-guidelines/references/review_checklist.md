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
- Form views do not include `<field name="active">`.
- QWeb output does not introduce unsafe HTML.
- User-facing XML source text is English; translations handle other languages.
- Font Awesome `<i class="fa ...">` icons have text or a `title` on the icon, parent, or descendant.

## Python and ORM

- Names are meaningful and match Odoo conventions.
- Python string literals use single quotes in new or modified code, except docstrings or cases where double quotes avoid escaping.
- Field suffixes match field types.
- Fields with `tracking=True` or `tracking=<sequence>` are only on models inheriting `mail.thread` or a mixin/model that inherits it.
- Model class members are in conventional order.
- Action methods use `self.ensure_one()` when single-record.
- User-facing Python source text is English in field labels/help, exceptions, notifications, and wizard messages.
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
