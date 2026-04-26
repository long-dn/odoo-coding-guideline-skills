# Python Guidelines

Use this reference for Python style, imports, readability, comments, and translations.

Source: official Odoo 19 coding guidelines, "Programming in Odoo", "Idiomatic Python", and translation guidance.

## Readability first

- Favor readable code over clever or overly compact code.
- Use meaningful variable, class, and method names.
- Multiple return points are acceptable when they make control flow clearer.
- Use short comments for non-obvious logic; avoid comments that restate the code.
- Add docstrings for methods whose contract is not obvious from the name and signature.

## Idiomatic Python

Prefer standard Python constructs:

```python
new_dict = dict(my_dict)
new_list = list(old_list)
values = {"foo": 3, "bar": 4}
values.update(foo=3, bar=4)
```

Use builtins and collection truthiness correctly:

```python
value = values.get("key")

if records:
    ...

for key, value in values.items():
    ...
```

Use comprehensions when they improve readability:

```python
pairs = [(item["id"], item["name"]) for item in rows]
```

Use `setdefault` for simple grouping:

```python
grouped = {}
for line in lines:
    grouped.setdefault(line.partner_id, []).append(line)
```

## Imports

- Keep imports grouped and stable according to the module's existing style.
- Avoid importing modules or helpers that are not used.
- Prefer Odoo public helpers over private or internal paths when available.

## Translations

Keep interpolation inside `_()` so translators see the full sentence.

Good:

```python
message = _("Order %(name)s cannot be confirmed.", name=order.name)
```

Avoid:

```python
message = _("Order %s cannot be confirmed.") % order.name
message = _("Order ") + order.name + _(" cannot be confirmed.")
```

Guidelines:

- Use named placeholders when more than one variable is present.
- Do not build translatable sentences by concatenating translated fragments.
- Prefer `%`-style placeholders in Odoo translatable strings.
- Keep HTML structure separate from translated text; load `security.md` when using `Markup`.
- Do not create or patch `i18n/*.po` by hand after adding translatable strings. Use Odoo's translation export workflow; load `translations.md`.

## Review cues

Flag these in reviews:

- Clever one-liners that hide business rules.
- Pointless temporary variables that make code longer without improving meaning.
- `len(collection)` used only as a truthiness check.
- Translated strings assembled through concatenation or interpolation outside `_()`.
- Handwritten or manually patched `i18n/*.po` files in coding changes.
- Comments explaining obvious assignments instead of business intent.
