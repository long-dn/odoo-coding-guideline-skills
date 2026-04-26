# JavaScript Guidelines

Use this reference for Odoo JavaScript, OWL components, frontend services, and comments.

Source: official Odoo 19 coding guidelines, JavaScript conventions section.

## General style

- Keep JavaScript modules small and focused.
- Prefer clear names over abbreviations.
- Avoid global state unless using Odoo's service/registry patterns.
- Keep comments for behavior that is not obvious from the code.
- Match the surrounding module's established OWL and registry patterns.

## Odoo frontend patterns

- Put authored JavaScript under `static/src/js` or a more specific subdirectory already used by the module.
- Put QWeb/OWL XML templates under `static/src/xml`.
- Keep component templates, JS, and styles named consistently.
- Register components, fields, views, or services through the appropriate Odoo registry rather than ad hoc bootstrapping.
- Do not bypass services that already provide the desired behavior.

## Naming

- Use descriptive component and service names.
- Keep exported symbols stable and explicit.
- Avoid names that encode temporary implementation details.

## Review cues

Flag these in reviews:

- Direct DOM manipulation where an OWL state/template pattern is expected.
- Global event listeners without cleanup.
- New frontend files placed outside `static/src`.
- Component names and template names that do not match.
- Service calls or registries copied from another module without checking the local dependency and asset bundle.
