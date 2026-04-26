# XML Guidelines

Use this reference for XML records, views, menus, actions, data, and templates.

Source: official Odoo 19 coding guidelines, "XML files" section.

## Record format

Prefer `<record>` declarations for records.

- Put `id` before `model`.
- In `<field>`, put `name` first.
- Put the value in the tag body or in `eval`, then put other attributes such as `widget` and `options` by importance.
- Group records by model where dependencies do not force another order.
- Use `<data>` only for `noupdate="1"` data. If the whole file is noupdate, put `noupdate="1"` on `<odoo>`.

```xml
<record id="view_example_form" model="ir.ui.view">
    <field name="name">example.model.form</field>
    <field name="model">example.model</field>
    <field name="arch" type="xml">
        <form>
            <field name="name"/>
        </form>
    </field>
</record>
```

## External ids

Use predictable external ids. Names should help reviewers identify the record type and target model.

Common patterns:

- Views: `<model>_view_<view_type>` or `view_<model>_<view_type>`, following the module's local style.
- Actions: `<model>_action` or `action_<model>`.
- Menus: `<model>_menu` or `menu_<model>`.
- Security groups: `group_<role_or_feature>`.
- Record rules: `<model>_rule_<scope>`.

Do not churn existing external ids unless migration is part of the task.

## Menus and actions

- Keep menu definitions close to related actions when dependencies matter.
- Keep root/module menus in the module menu file.
- Avoid overly generic ids such as `view_form`, `action_window`, or `menu_main` in modules with multiple models.

## Data files

- Split demo data from production data.
- Use `noupdate="1"` for stable configuration that should not be overwritten on module update.
- Keep mail templates, scheduled actions, sequences, and security XML in discoverable files.

## QWeb and templates

- Keep template names explicit and module-prefixed.
- Keep dynamic text translatable when user-visible.
- Avoid unsafe raw HTML output; load `security.md` for HTML or Markup handling.

## Icon accessibility

Odoo validates Font Awesome icons in views and templates. A bare icon is not acceptable if it has no accessible label or adjacent text.

Any `<i>` tag with a Font Awesome class such as `fa`, `fa-*`, or `fa fa-*` must have one of:

- A `title` attribute on the `<i>` tag itself.
- A `title` on a parent element.
- A `title` on a descendant element.
- Visible text associated with the icon.

Good:

```xml
<i class="fa fa-exclamation-triangle me-2" title="Credit limit warning"/>
<span title="Credit limit warning">
    <i class="fa fa-exclamation-triangle me-2"/>
</span>
<span>
    <i class="fa fa-exclamation-triangle me-2"/>
    Credit limit exceeded
</span>
```

Avoid:

```xml
<i class="fa fa-exclamation-triangle me-2"/>
```

This avoids warnings such as: `A <i> with fa class (...) must have title in its tag, parents, descendants or have text`.

## Review cues

Flag these in reviews:

- `<data>` wrappers with no `noupdate`.
- Field attributes ordered inconsistently in new code.
- XML ids too generic for maintenance.
- Demo records placed in production data files.
- View XML mixed with security, report, or demo records without an existing module convention.
- Font Awesome `<i>` icons without `title` or visible text.
