# MSRE Hardware Design — Agent Instructions

> **Read this file first.** It tells AI coding agents (Claude Code, OpenClaw, OpenAI Codex,
> Cursor, and equivalent) how to work in this repository.

---

## What this repo contains

Procurement-ready hardware designs for the **Molten Salt Reactor Experiment (MSRE)**
(ORNL, 1965–1969). Designs are structured as 12 component packages under `components/`.

**This is a documentation + data repository.** There is no compiled source code.
The primary artefacts are:
- `components/*/bom.csv` — Bill of materials (CSV; 171 line items across 12 components)
- `components/*/specifications.md` — Detailed dimensional and material specifications
- `docs/` — Safety, materials, and system documentation
- `bom_review/` — Multi-agent BOM review reports from msr-gstack
- `cad/` — Parametric CadQuery CAD models (STEP + PNG) for all 12 components

---

## Commands

```bash
make validate   # Validate BOM CSV structure and required fields
make lint       # Lint all markdown files (requires markdownlint-cli)
make check      # Full check: lint + validate
```

Install dependencies:
```bash
npm install -g markdownlint-cli   # for make lint
pip install csvkit                # for make validate (csvstat used)
```

---

## Repository structure

```
msre_hardware_design/
├── CLAUDE.md                        ← This file
├── llms.txt                         ← LLM discovery file
├── mcp.json                         ← MCP server config
├── Makefile                         ← make validate / lint / check
├── .ai/
│   ├── requirements.md              ← Project goals & constraints
│   ├── architecture.md              ← System architecture overview
│   └── tech-stack.md                ← Tech stack reference
├── docs/
│   ├── system_overview.md           ← Full MSRE system description
│   ├── safety_considerations.md     ← Nuclear safety, chemical hazards
│   ├── materials_guide.md           ← Hastelloy-N, graphite, salt specs
│   └── references.md                ← ORNL primary sources
├── system/
│   ├── flow_diagram.md              ← Process flow and P&ID description
│   └── integration.md               ← Component interfaces
├── components/
│   ├── 01_reactor_vessel/           ← Hastelloy-N pressure vessel
│   ├── 02_reactor_core/             ← Graphite moderator assembly
│   ├── 03_primary_heat_exchanger/   ← Fuel-to-coolant salt HX
│   ├── 04_fuel_salt_pump/           ← Primary loop centrifugal pump
│   ├── 05_coolant_salt_pump/        ← Secondary loop pump
│   ├── 06_fuel_drain_tank/          ← Emergency drain storage
│   ├── 07_freeze_valves/            ← Passive salt freeze valves
│   ├── 08_off_gas_system/           ← Fission-gas handling
│   ├── 09_control_rods/             ← Reactivity control
│   ├── 10_reactor_cell/             ← Biological shielding
│   ├── 11_coolant_radiator/         ← Air-cooled heat rejection
│   └── 12_instrumentation_control/  ← I&C system
└── bom_review/                      ← msr-gstack multi-agent BOM reviews
```

---

## BOM CSV schema

Every `bom.csv` file has these columns (always in this order):

```
part_id, description, material, specification, quantity, unit,
dimension_1_mm, dimension_2_mm, dimension_3_mm, notes
```

- `part_id`: Component prefix + 3-digit number (e.g. `RV-001`, `IC-025`)
- `quantity`: numeric or `as req'd`
- `unit`: `ea`, `m`, `kg`, `L`, `set`, `wall`, `slab`
- Dimensions: SI (mm). Empty string if not applicable.

---

## Rules for agents working in this repo

1. **Never add libraries or dependencies** without checking `.ai/tech-stack.md` first.
2. **All material changes must reference an ORNL primary source** (list in `docs/references.md`).
3. **BOM CSV edits must preserve the column schema** — do not add or reorder columns.
4. **Safety-critical items are flagged** in `bom_review/` — fix findings there first.
5. **Units are always SI (mm, kg, °C)** with Imperial in parentheses in notes.
6. **Do not delete existing `part_id` values** — append new items at end of CSV.
7. **Run `make validate` after every BOM edit** to catch schema errors.
8. **Run `make lint` after every markdown edit.**

---

## Known open items (as of 2026-03-17)

| Item | File | Status |
|------|------|--------|
| Graphite stringer count | `components/02_reactor_core/bom.csv` RC-001/002 | PARTIALLY RESOLVED — openmsr/msre (ORNL-TM-3039) confirms 617 total (full+fractional); our 509 full-sized + ~108 fractional is consistent. Exact zone split still needs ORNL-TM-728 Table 3.1. |
| Vessel OD discrepancy | `cad/scripts/01_reactor_vessel.py` | OPEN — ORNL-TM-728: 55.5 in (1410 mm); ORNL-TM-3229 (via openmsr): references "60-in. OD ASME F&D head". Likely reflects flange OD vs. shell OD. See `docs/openmsr_validation.md §2.1`. |
| Roof plug weight vs. crane SWL | `components/10_reactor_cell/bom.csv` RCL-002A/RCL-008 | Requires design decision on plug dims or crane upgrade to 25 t |
| OGS-016 / IC-025A dual-tag | `components/08_off_gas_system/bom.csv` | Cross-reference note needed |
| OpenMC k-eff validation | `cad/step/02_reactor_core.step` | PLANNED — convert core STEP to h5m via CAD_to_openMC and run criticality benchmark against openmsr/msre result. See `docs/openmsr_validation.md §2.3`. |

---

## Related repositories

| Repo | Role |
|------|------|
| [msr-gstack](https://github.com/pranavkantgaur/msr-gstack) | Multi-agent MSR specialist team (review skills) |
| [msr_data_layer](https://github.com/pranavkantgaur/msr_data_layer) | RAG access to ORNL historical reports |
| [msr_physical_ai_layer](https://github.com/pranavkantgaur/msr_physical_ai_layer) | Physical-AI fabrication guidance |
| [openmsr/msre](https://github.com/openmsr/msre) | Independent MSRE CAD model (OnShape v24) + OpenMC benchmarks + CFD validation — **primary cross-validation source for CAD geometry** |

---

## Safety notice for agents

⚠️ This repository describes nuclear reactor hardware. Any agent suggesting design changes must:
- Reference a primary ORNL source or peer-reviewed nuclear engineering paper.
- Not weaken safety margins (e.g., crane SWL, B₄C absorber loading, criticality controls).
- Flag radiological hazard changes (tritium, fission products, B₄C) for human review.

*The MSRE operated at up to 8 MWt with fluoride salts at 650 °C and a primary loop radioactive
inventory of ~10⁶ Ci. Design errors have real-world consequences.*
