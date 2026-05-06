# Test Case 10: Do not use doall on ir.cron

## User Prompt

Review this Odoo 19 scheduled action XML. It raises:

```text
ValueError: Invalid field 'doall' in 'ir.cron'
```

```xml
<record id="ir_cron_sale_cutoff" model="ir.cron">
    <field name="name">Sale Order: Daily Cut-off Batch</field>
    <field name="model_id" ref="sale.model_sale_order"/>
    <field name="state">code</field>
    <field name="code">model._cron_sale_cutoff()</field>
    <field name="interval_number">1</field>
    <field name="interval_type">days</field>
    <field name="active" eval="True"/>
    <field name="doall" eval="False"/>
</record>
```

## What we're testing

- The skill should trigger for XML data records.
- It should recognize that Odoo 19 `ir.cron` records must not declare `doall`.
- It should recommend removing the `<field name="doall" .../>` line.

## Expected output

The assistant should explain that `doall` is not a valid Odoo 19 `ir.cron`
field and suggest removing it from the XML record.
