# Test Case 9: Do not show active on form views

## User Prompt

Review this Odoo form view:

```xml
<form>
    <sheet>
        <group>
            <field name="name"/>
            <field name="active"/>
        </group>
    </sheet>
</form>
```

## What we're testing

- The skill should trigger for XML form views.
- It should flag direct display of the technical `active` field.
- It should recommend using Odoo's standard archive/unarchive behavior instead.

## Expected output

The assistant should say not to add `<field name="active">` to form views and suggest removing it from the form view.
