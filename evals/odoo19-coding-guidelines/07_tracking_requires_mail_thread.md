# Test Case 7: Field tracking requires mail.thread

## User Prompt

Review this Odoo model warning:

```text
Field osp.approval.category.state: unknown parameter 'tracking'
```

```python
class ApprovalCategory(models.Model):
    _name = 'osp.approval.category'

    state = fields.Selection(
        selection=[('draft', 'Draft'), ('approved', 'Approved')],
        default='draft',
        tracking=True,
    )
```

## What we're testing

- The skill should recognize that field `tracking` is not a generic field parameter.
- It should explain that `tracking` requires `mail.thread`.
- It should note that `mail.activity.mixin` alone is not enough.

## Expected output

The assistant should recommend either removing `tracking=True` or adding `mail.thread` when chatter tracking is desired:

```python
_inherit = ['mail.thread', 'mail.activity.mixin']
```

It should also mention adding `mail` to module dependencies when introducing mail mixins.
