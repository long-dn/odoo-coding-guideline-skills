# Test Case 1: Module layout review

## User Prompt

Review this Odoo 19 addon tree and tell me what violates the official coding guidelines:

```text
my_addon/
├── Models/
│   └── SaleOrderExtension.py
├── views.xml
├── report_template.xml
├── wizard_confirm.py
└── static/
    └── style.scss
```

## What we're testing

- The skill should trigger for Odoo addon review.
- It should load module structure and review checklist guidance.
- It should flag directory and filename problems.

## Expected output

The assistant should identify uppercase directory/file names, generic XML filenames, wizard file outside `wizard/`, static authored SCSS outside `static/src/scss`, and mixed report/view XML naming.
