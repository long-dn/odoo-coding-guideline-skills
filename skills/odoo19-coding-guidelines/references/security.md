# Security Review

Use this reference for public methods, raw SQL, domains, HTML/Markup, eval, and dynamic attribute access.

Sources: official Odoo 19 security documentation and coding guideline references to security pitfalls.

## Public methods

Any model method not starting with `_` can be called through RPC. Public methods must not trust parameters or `self`.

Guidelines:

- Keep internal helpers private with a leading underscore.
- Re-check access rights, record rules, ownership, company, and state before side effects.
- Do not expose methods that perform privileged writes unless the method validates the business rule itself.
- Treat ids, domains, field names, and state transitions from clients as untrusted.

## ORM first

Prefer the ORM for CRUD and searches. Raw SQL bypasses important ORM behavior and can bypass security, translations, computed field logic, invalidation, and multi-company expectations.

If SQL is required:

- Use parameterized queries.
- Keep SQL narrowly scoped and documented.
- Flush required fields before reading database state directly.
- Invalidate or refresh caches when manual writes are unavoidable.
- Do not concatenate SQL strings with user-provided values.

## Domains

- Build domains with structured data, not string concatenation.
- Validate dynamic field names and operators.
- Keep domain logic readable; name intermediate domains when complex.
- Do not pass client-provided domains into privileged searches without filtering allowed fields and operators.

## HTML, Markup, and escaping

Escaping is required when mixing text with code such as HTML. Treat user data and translated text as text until explicitly escaped.

Guidelines:

- Use Odoo tools such as `html_escape`, `html_sanitize`, and `Markup` intentionally.
- Do not interpolate raw text into `Markup` with f-strings.
- Keep HTML structure outside translatable text where possible.
- Sanitize only when HTML content is intentionally allowed; escaping and sanitizing are different operations.

## Evaluating content

- Avoid `eval`.
- Use `safe_eval` only for trusted, constrained Odoo use cases.
- Prefer `ast.literal_eval` for Python literals.
- Prefer JSON parsers for JSON data.

## Dynamic attribute access

Do not use `getattr(record, field_name)` with untrusted field names. For dynamic field access, prefer record item access after validating that the field is allowed:

```python
if field_name not in allowed_fields:
    raise AccessError(_("Field is not allowed."))
value = record[field_name]
```

## Review cues

Flag these in reviews:

- Public methods that write records without validating state and access.
- `sudo()` used to hide access problems instead of modeling the business permission.
- Raw SQL with string formatting, f-strings, or concatenation.
- Client-provided domains, ids, or field names used in privileged operations without validation.
- `Markup(f"...{value}...")` or `t-raw`-style output with user data.
- `eval` or broad `safe_eval` on user-controlled content.
