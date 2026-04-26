# Odoo Naming and Model Conventions

Use this reference for Odoo model names, field names, method names, class order, and common ORM conventions.

Source: official Odoo 19 coding guidelines, "Symbols and Conventions" section.

## Model names

- Model technical names use dot notation and should usually be prefixed by the module name.
- Model names should be singular: `res.partner`, `sale.order`, not pluralized forms.
- Transient models should describe the target model and action, for example `<related_model>.<action>`. Avoid adding "wizard" to the technical name.
- SQL/report models should follow `<related_model>.report.<action>`.

## Python classes and variables

- Odoo Python classes use PascalCase.
- Use PascalCase variables for model classes or model recordset accessors.
- Use lowercase underscore names for ordinary variables.
- Suffix raw database ids with `_id` and lists of ids with `_ids`.
- Do not name a recordset variable `partner_id`; use `partner` or `partners`.

```python
Partner = self.env['res.partner']
partners = Partner.browse(partner_ids)
partner_id = partners[:1].id
```

## Field names

- `Many2one` fields end with `_id`, for example `partner_id`.
- `One2many` and `Many2many` fields end with `_ids`, for example `sale_order_line_ids`.
- Boolean names should read naturally in conditions.
- Avoid generic field names when the model has multiple similar concepts.

## Field parameters

Use field parameters only when the target model supports them.

### `tracking`

Only add `tracking=True` or `tracking=<sequence>` on fields when the model inherits `mail.thread`, or inherits another mixin/model that itself inherits `mail.thread`.

Good:

```python
class ApprovalCategory(models.Model):
    _name = 'osp.approval.category'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    state = fields.Selection(
        selection=[('draft', 'Draft'), ('approved', 'Approved')],
        default='draft',
        tracking=True,
    )
```

Avoid:

```python
class ApprovalCategory(models.Model):
    _name = 'osp.approval.category'

    state = fields.Selection(
        selection=[('draft', 'Draft'), ('approved', 'Approved')],
        default='draft',
        tracking=True,
    )
```

Important:

- `mail.activity.mixin` alone adds activity behavior, not field value tracking validation.
- If a model only inherits `mail.activity.mixin`, do not use field `tracking`.
- Ensure the module depends on `mail` before adding `mail.thread`.
- Do not override `_valid_field_parameter` merely to silence the warning. That hook is for framework-level extensions; for normal business models, either inherit `mail.thread` or remove `tracking`.
- The warning to prevent is: `unknown parameter 'tracking'`.

## Method names

- Compute methods: `_compute_<field_name>`.
- Search methods: `_search_<field_name>`.
- Default methods: `_default_<field_name>`.
- Selection methods: `_selection_<field_name>`.
- Onchange methods: `_onchange_<field_name>`.
- Constraint methods: `_check_<constraint_name>`.
- Object action methods: `action_<verb_or_action>`.
- Action methods normally operate on one record; call `self.ensure_one()` at the start when that is the contract.

## Model class order

Order model members consistently:

1. Private attributes such as `_name`, `_description`, `_inherit`.
2. Default methods and `default_get`.
3. Field declarations.
4. SQL constraints and indexes.
5. Compute, inverse, and search methods in field declaration order.
6. Selection methods.
7. Constraint and onchange methods.
8. CRUD and ORM override methods.
9. Action methods.
10. Other business methods.

## Review cues

Flag these in reviews:

- Recordsets stored in variables ending with `_id`.
- `Many2one` fields without `_id` or x2many fields without `_ids`.
- `tracking=True` on a model that does not inherit `mail.thread`.
- Action methods that silently process multi-record sets when the UI action is single-record.
- New methods placed randomly in a model class instead of near their convention group.
- Plural model technical names.
