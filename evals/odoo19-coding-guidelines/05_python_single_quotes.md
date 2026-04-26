# Test Case 5: Python single quote style

## User Prompt

Review this Odoo field declaration:

```python
icon = fields.Char(default="fa-check-circle")
```

## What we're testing

- The skill should trigger for Python style.
- It should require single quotes for Python string literals in new or modified Odoo code.

## Expected output

The assistant should flag the double-quoted string and suggest:

```python
icon = fields.Char(default='fa-check-circle')
```
