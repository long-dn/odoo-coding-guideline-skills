# Changelog - odoo19-coding-guidelines

## [0.1.10] - 2026-05-18

Extend automatic root/admin assignment from administrator groups to privileged module groups such as manager roles.

## [0.1.9] - 2026-05-06

Block the removed `doall` field in Odoo 19 `ir.cron` XML records.

## [0.1.8] - 2026-05-02

Require administrator `res.groups` XML records to assign both root and admin users.

## [0.1.7] - 2026-04-28

Require multi-line XML tag attributes to be indented at least one full indentation level from the opening tag line.

## [0.1.6] - 2026-04-27

Block direct display of the technical `active` field on form views.

## [0.1.5] - 2026-04-27

Require English source text for user-facing labels, field strings/help, exceptions, menus, actions, and templates.

## [0.1.4] - 2026-04-27

Clarify that field `tracking` requires `mail.thread`; `mail.activity.mixin` alone is not enough.

## [0.1.3] - 2026-04-27

Add XML accessibility rule for Font Awesome icons requiring text or title metadata.

## [0.1.2] - 2026-04-27

Require single-quoted Python string literals in new and modified Odoo code.

## [0.1.1] - 2026-04-27

Add translation file rules that block handwritten `i18n/*.po` files and prefer Odoo export workflows.

## [0.1.0] - 2026-04-26

Initial public skill with Odoo 19 coding guideline references.
