# MSRE Hardware Design — Tech Stack

**Last updated:** 2026-03-17

---

## Primary file formats

| Format | Use | Location |
|--------|-----|---------|
| Markdown (`.md`) | All documentation, specifications, README files | Throughout |
| CSV (`.csv`) | Bill of materials — structured, machine-parseable | `components/*/bom.csv` |
| Python (`.py`) | Validation scripting | `validation/` |
| YAML (`.yml`) | GitHub Actions CI workflows | `.github/workflows/` |
| JSON (`.json`) | MCP configuration | `mcp.json` |

---

## No build step / no compiled code

This is a **documentation + data repository**. There is no:
- Package.json / npm / node_modules
- requirements.txt / pip environment
- CMakeLists / Makefile for compiled code

The `Makefile` at root provides linting and validation shortcuts only.

---

## Tooling

| Tool | Purpose | Install |
|------|---------|---------|
| `markdownlint-cli` | Lint all `.md` files | `npm install -g markdownlint-cli` |
| `csvkit` (csvstat, csvclean) | BOM CSV validation | `pip install csvkit` |
| `python3` | BOM schema validation script | Standard |
| GitHub Actions | CI: lint + validate on every push | `.github/workflows/validate.yml` |

---

## CI / GitHub Actions

Workflow: `.github/workflows/validate.yml`
- Triggers: push to any branch, pull_request
- Steps:
  1. Lint all markdown with `markdownlint`
  2. Validate BOM CSV column count and required fields
  3. Report any schema violations

---

## Schemas

### BOM CSV — required columns (exactly 10, in this order)

```
part_id, description, material, specification, quantity, unit,
dimension_1_mm, dimension_2_mm, dimension_3_mm, notes
```

Validation rules enforced by `make validate`:
- Exactly 10 columns per row
- `part_id` matches `[A-Z]+-[0-9]+` pattern
- `quantity` is numeric or the string `as req'd` or starts with `~` or `≥`
- `unit` is one of: `ea`, `m`, `kg`, `L`, `set`, `wall`, `slab`

---

## Do NOT add

- Any npm package (no `package.json` at root)
- Any Python package (no `requirements.txt` unless extending `validation/`)
- Any CAD file format (STL, STEP, DXF) without first creating a `cad/` subdirectory and
  updating this file
- Any database or binary format without updating this file

---

## MCP Integrations (`mcp.json`)

The repo exposes a local MCP configuration for agents that support it:
- **filesystem**: read/write access to components BOM and specs
- **github**: read PRs, issues, and workflow runs

See `mcp.json` for full configuration.
