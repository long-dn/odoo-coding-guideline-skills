# Test Case 12: Recursive computed fields

## User Prompt

Review this Odoo warning:

```text
UserWarning: Field res.partner.allow_door_hold should be declared with recursive=True
```

```python
allow_door_hold = fields.Boolean(compute='_compute_allow_door_hold')

@api.depends('parent_id.allow_door_hold')
def _compute_allow_door_hold(self):
    ...
```

## What we're testing

- The skill should trigger for Odoo field parameter warnings.
- It should recognize a recursive computed dependency through `parent_id`.
- It should recommend adding `recursive=True` to the field declaration.

## Expected output

The assistant should recommend:

```python
allow_door_hold = fields.Boolean(
    compute='_compute_allow_door_hold',
    recursive=True,
)
```
