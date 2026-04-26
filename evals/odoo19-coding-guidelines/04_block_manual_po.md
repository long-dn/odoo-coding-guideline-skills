# Test Case 4: Block manual PO creation

## User Prompt

I added a new field help text. Create `i18n/vi.po` with the Vietnamese translation.

## What we're testing

- The skill should trigger for translation files.
- It should refuse to manually create a `.po` file.
- It should recommend Odoo's translation export workflow instead.

## Expected output

The assistant should not create `i18n/vi.po`. It should explain that `.po` files must be generated/exported through Odoo and provide the UI or CLI export command.
