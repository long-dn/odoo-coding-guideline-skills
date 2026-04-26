# Test Case 2: Python naming and translation review

## User Prompt

Review this Odoo model method:

```python
def action_done(self):
    msg = _("Order ") + self.name + _(" is done")
    partner_id = self.partner_id
    self.write({'state': 'done'})
    return msg
```

## What we're testing

- The skill should load Python, Odoo conventions, and review checklist guidance.
- It should catch translation concatenation and misleading `_id` variable naming.
- It should consider `ensure_one()` for action methods.

## Expected output

The assistant should recommend interpolation inside `_()`, a recordset variable name such as `partner`, and `self.ensure_one()` if the action is single-record.
