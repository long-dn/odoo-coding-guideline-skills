# Test Case 8: English source text

## User Prompt

Review this Odoo validation method:

```python
def _check_internal_user(self):
    for rec in self:
        if rec.user_id.share:
            msg = 'Người duyệt phải là người dùng nội bộ (không phải portal/public).'
            raise ValidationError(msg)
```

## What we're testing

- The skill should reject non-English user-facing source text.
- It should recommend English source text and translations through Odoo i18n export.
- It should preserve single-quote Python style.

## Expected output

The assistant should flag the Vietnamese message and suggest English source text, for example:

```python
def _check_internal_user(self):
    for rec in self:
        if rec.user_id.share:
            raise ValidationError(_('The approver must be an internal user, not a portal or public user.'))
```

It should mention that Vietnamese text should come from exported translations, not from Python source.
