# Module Structure

Use this reference for addon layout, filenames, and where files belong.

Source: official Odoo 19 coding guidelines, "Module structure" section.

## Directory layout

Prefer the standard addon tree:

```text
my_module/
├── __init__.py
├── __manifest__.py
├── controllers/
├── data/
├── models/
├── report/
├── security/
├── static/
│   ├── img/
│   ├── lib/
│   └── src/
│       ├── js/
│       ├── scss/
│       └── xml/
├── views/
└── wizard/
```

Only create directories the module actually needs. Keep Python model code in `models/`, transient models in `wizard/`, report model code and report XML in `report/`, business/security data in `data/` and `security/`, and UI assets in `static/src/`.

## File naming

- File names should contain only lowercase letters, digits, and underscores.
- Main model file: `<model_name>.py`, replacing dots with underscores, for example `plant_order.py`.
- Inherited model extension: name the file after the inherited model, for example `res_partner.py`.
- Views: `<model_name>_views.xml`, for example `plant_order_views.xml`.
- Menus: `<module_name>_menus.xml`.
- Templates: `<model_or_module>_templates.xml`.
- Wizards: `wizard/<transient_name>.py` and `wizard/<transient_name>_views.xml`.
- SQL/statistical reports: `report/<report_name>.py` and `report/<report_name>_views.xml`.
- Printable reports: split report actions/paper formats from QWeb templates, commonly `<name>_reports.xml` and `<name>_templates.xml`.

## Permissions and assets

- Use folder permissions `755` and file permissions `644`.
- Put third-party frontend libraries under `static/lib/`.
- Put authored JS, SCSS, and QWeb templates under `static/src/js`, `static/src/scss`, and `static/src/xml`.

## Review cues

Flag these in reviews:

- Mixed unrelated model classes in one large file when the module already follows one file per model.
- Uppercase, dashed, spaced, or dotted filenames.
- Wizard Python files outside `wizard/`.
- Report QWeb templates mixed into ordinary form/list view files without a local reason.
