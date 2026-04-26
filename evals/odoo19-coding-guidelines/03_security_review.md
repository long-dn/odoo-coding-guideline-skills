# Test Case 3: Security review

## User Prompt

Review this Odoo controller/model flow for guideline issues:

```python
def action_force_approve(self, ids):
    records = self.sudo().browse(ids)
    records.write({'state': 'approved'})
```

## What we're testing

- The skill should load security guidance.
- It should treat public methods and RPC parameters as untrusted.
- It should flag broad `sudo()` and missing state/access validation.

## Expected output

The assistant should explain that a public method can be RPC-callable, ids from clients must be validated, `sudo()` must be narrow and justified, and server-side business checks are required before writes.
