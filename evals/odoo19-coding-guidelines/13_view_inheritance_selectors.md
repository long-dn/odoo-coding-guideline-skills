# Test Case 13: Stable view inheritance selectors

## User Prompt

Review this Odoo inherited view error:

```text
View inheritance may not use attribute 'string' as a selector.
```

```xml
<xpath expr="//page[@string='Metadata']" position="before">
    <page string="Approval">
        <group>
            <field name="approval_state"/>
        </group>
    </page>
</xpath>
```

## What we're testing

- The skill should reject xpath selectors using `@string`.
- It should require stable technical anchors such as `name` or `id`.
- It should suggest adding `name` or `id` to structural containers such as `page` and `group`.

## Expected output

The assistant should suggest targeting a technical anchor:

```xml
<xpath expr="//page[@name='metadata']" position="before">
    <page name="approval" string="Approval">
        <group name="approval_group">
            <field name="approval_state"/>
        </group>
    </page>
</xpath>
```

It should explain that user-facing `string` values are labels/translatable text and must not be used as inheritance selectors.
