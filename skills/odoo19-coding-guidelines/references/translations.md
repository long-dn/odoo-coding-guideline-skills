# Translation Files

Use this reference for `i18n/`, `.po`, `.pot`, and translation export/import workflows.

Sources: official Odoo 19 translating modules guide and Odoo 19 CLI reference.

## Hard rule for agents

Do not manually create or edit `i18n/*.po` files in code changes.

Reason:

- `.po` files should reflect Odoo's extracted translation terms.
- Manual generation is easy to make stale, incomplete, or noisy.
- Export is more exact and usually smaller because it includes the real module terms.

When a task adds or changes translatable strings, update the source code/XML only. Source strings must be English. Tell the user that translation files should be regenerated with Odoo export.

## Allowed files

- `i18n/<module_name>.pot`: translation template exported from Odoo.
- `i18n/<lang>.po`: translated language file exported/maintained through Odoo translation workflows.

Agents may create the `i18n/` directory only when wiring a module structure, but should not populate handwritten `.po` files.

## Export from the UI

For a template export:

1. Open Settings > Translations > Import / Export > Export Translations.
2. Leave language empty/default for a new language/template.
3. Select PO File format.
4. Select the module.
5. Export and place the downloaded `<module_name>.pot` in `i18n/`.

For a translated language file, select the target language and export the selected module, then place the resulting `.po` in `i18n/`.

## Export from CLI

Odoo 19 supports the `i18n export` subcommand:

```bash
odoo-bin i18n export <module_name> --languages pot --database <db_name> --addons-path <addons_path>
```

For a specific language:

```bash
odoo-bin i18n export <module_name> --languages vi_VN --database <db_name> --addons-path <addons_path>
```

Notes:

- `pot` is the template language and is the default if no language is specified.
- For `.po` and `.pot`, Odoo creates files under the module's `i18n/` folder when no output path is specified.
- If `--output` is used, only one language is allowed and output from all selected modules goes into that one file.
- Language codes must use the locale format expected by Odoo, for example `vi_VN` or `fr_BE`.

## Import

Use Odoo's import workflow for incoming `.po` or `.csv` files. CLI form:

```bash
odoo-bin i18n import <file.po> --language <language_code> --database <db_name> --addons-path <addons_path>
```

Add `--overwrite` only when intentionally replacing existing translations.

## Review cues

Flag these in reviews:

- New `.po` files authored directly by an agent or script instead of exported.
- `.po` entries that do not correspond to source terms.
- Translation changes mixed into unrelated code changes.
- Non-English source strings in Python/XML instead of English source plus exported translations.
- English source strings changed only to satisfy a generated `.po` file.
