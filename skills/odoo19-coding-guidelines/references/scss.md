# SCSS Guidelines

Use this reference for SCSS/CSS naming, selector structure, variables, and property order.

Source: official Odoo 19 coding guidelines, SCSS section.

## File placement

Put authored styles under `static/src/scss` or the module's existing style directory under `static/src`.

## Selectors and class names

- Avoid `id` selectors.
- Prefix classes with `o_<module_name>` or the main route name for website modules.
- The webclient may use the shorter `o_` prefix.
- Avoid hyper-specific nested names. Prefer the "grandchild" style where children use meaningful shorter class names.

Prefer:

```html
<div class="o_example_wrapper">
    <div class="o_example_entries">
        <span class="o_example_entry">
            <a class="o_example_link">Entry</a>
        </span>
    </div>
</div>
```

Avoid long chains such as `o_example_wrapper_entries_entry_link`.

## Variables

Global SCSS variable convention:

```scss
$o-block-color: value;
$o-block-title-color: value;
$o-block-title-color-hover: value;
```

Use `$o-[root]-[element]-[property]-[modifier]`.

Scoped variables use `$-name` and stay inside the block:

```scss
.o_example {
    $-inner-gap: 1rem;

    margin-right: $-inner-gap;
}
```

Scoped SCSS variables and CSS variables belong at the top of the block, followed by a blank line before declarations.

## Property order

Order properties from outside to inside, then decorative rules:

1. Positioning and layout.
2. Display and flow.
3. Box model: margin, size, border, padding.
4. Background and visual decoration.
5. Typography.
6. Effects such as filters.

## Review cues

Flag these in reviews:

- `#id` selectors in module SCSS.
- Classes missing the `o_<module>` prefix.
- Deeply chained BEM-like names that will be painful to maintain.
- Scoped variables mixed into the middle of declarations.
- Visual/decorative properties placed before layout properties in new blocks.
