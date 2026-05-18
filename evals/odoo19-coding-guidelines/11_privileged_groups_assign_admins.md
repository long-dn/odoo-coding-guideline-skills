# Test Case 11: Assign admins to privileged groups

## User Prompt

Review this Odoo security group:

```xml
<record id="group_example_manager" model="res.groups">
    <field name="name">Manager</field>
</record>
```

## What we're testing

- The skill should trigger for XML security groups.
- It should treat Manager as a privileged module role, not only Administrator.
- It should recommend assigning both root and admin users.

## Expected output

The assistant should recommend adding:

```xml
<field name="user_ids" eval="[(4, ref('base.user_root')), (4, ref('base.user_admin'))]"/>
```
