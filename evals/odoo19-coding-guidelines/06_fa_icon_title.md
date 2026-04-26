# Test Case 6: Font Awesome icon title

## User Prompt

Review this Odoo view snippet. It raises:

```text
A <i> with fa class (fa fa-exclamation-triangle me-2) must have title in its tag, parents, descendants or have text
```

```xml
<i class="fa fa-exclamation-triangle me-2"/>
```

## What we're testing

- The skill should trigger for XML view accessibility.
- It should recognize the Odoo warning for bare Font Awesome icons.
- It should suggest adding a `title` or visible text.

## Expected output

The assistant should explain that Font Awesome `<i>` tags need accessible text or `title`, and suggest:

```xml
<i class="fa fa-exclamation-triangle me-2" title="Credit limit warning"/>
```

or a parent/visible-text alternative.
