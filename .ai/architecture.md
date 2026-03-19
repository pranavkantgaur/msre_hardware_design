# MSRE Hardware Design — Architecture Overview

**Audience:** AI agents, engineers new to the project, integration teams  
**Last updated:** 2026-03-17

---

## 1. System Architecture (One Page)

The MSRE is a three-loop reactor system:

```
┌─────────────────────────────────────────────────────────────────┐
│  PRIMARY LOOP (Fuel Salt — radioactive)                         │
│                                                                 │
│  ┌──────────┐   fuel hot    ┌────────────┐   fuel cold          │
│  │ Reactor  │──────────────▶│  Primary   │──────────────┐       │
│  │  Vessel  │               │    Heat    │              │       │
│  │  + Core  │◀──────────────│  Exchanger │              │       │
│  └────┬─────┘   fuel cold   └──────┬─────┘              │       │
│       │                            │                     │       │
│  ┌────▼─────┐                      │             ┌───────▼────┐  │
│  │  Fuel    │◀─────────────────────┘             │ Fuel Salt  │  │
│  │  Salt    │      return                        │   Pump     │  │
│  │  Pump    │──────────────────────────────────▶ └────────────┘  │
│  └──────────┘                                                   │
│       │ (drain line, freeze valves)                             │
│  ┌────▼──────────┐                                              │
│  │ Fuel Drain    │  (emergency/scheduled drain; criticality-    │
│  │ Tank + FZV    │   safe annular geometry + B₄C absorber)     │
│  └───────────────┘                                              │
│       │ (off-gas line)                                          │
│  ┌────▼──────────┐                                              │
│  │  Off-Gas Sys  │  (He sparge → charcoal delay beds →         │
│  │ + Tritium     │   tritium control → stack monitor)          │
│  │  Control Train│                                              │
│  └───────────────┘                                              │
└─────────────────────────────────────────────────────────────────┘
          │ coolant hot                   ▲ coolant cold
          ▼                               │
┌─────────────────────────────────────────────────────────────────┐
│  SECONDARY LOOP (Coolant Salt — non-radioactive)                │
│                                                                 │
│  ┌──────────────┐  coolant hot   ┌───────────────┐             │
│  │   Primary    │───────────────▶│    Coolant    │             │
│  │    Heat      │                │    Radiator   │──▶ (air)    │
│  │  Exchanger   │◀───────────────│  (air-cooled) │             │
│  └──────────────┘  coolant cold  └───────┬───────┘             │
│                                          │                      │
│                                   ┌──────▼──────┐              │
│                                   │  Coolant    │              │
│                                   │ Salt Pump   │              │
│                                   └─────────────┘              │
└─────────────────────────────────────────────────────────────────┘
          │ wrapped by
┌─────────▼───────────────────────────────────────────────────────┐
│  REACTOR CELL (Biological shielding + N₂ inert atmosphere)      │
│  Control Rods │ I&C (NIS, TCs, EM flowmeters, level, pressure)  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Repository Data Flow

```
ORNL Technical Reports (primary sources)
    │
    ▼
components/*/specifications.md   ← human-readable design parameters
components/*/bom.csv             ← machine-parseable procurement data
    │
    ├──▶  msr-gstack agents       ← multi-agent BOM review (bom_review/)
    │     (review-materials,
    │      review-safety,
    │      review-reactor-design,
    │      review-instrumentation,
    │      review-salt-chemistry,
    │      review-fuel-cycle)
    │
    ├──▶  msr_data_layer          ← RAG knowledge base for agents
    │     (ORNL report chunks +
    │      BOM parameters indexed)
    │
    └──▶  msr_physical_ai_layer   ← fabrication planning AI
          (BOM → process plan →
           robot / CNC instructions)
```

---

## 3. Component Dependency Order

For assembly, components must be fabricated and qualified in this order:

```
1. Reactor Vessel (01)       ← structural foundation
2. Reactor Core (02)         ← goes inside vessel
3. Fuel Drain Tank (06)      ← must be ready before primary loop is filled
4. Freeze Valves (07)        ← installed in drain/fill lines before loop fill
5. Primary Heat Exchanger (03)
6. Fuel Salt Pump (04)       ← primary loop complete
7. Coolant Salt Pump (05)    ← secondary loop
8. Coolant Radiator (11)     ← secondary loop heat rejection
9. Off-Gas System (08)       ← connect to pump bowl before criticality
10. Control Rods (09)         ← install in vessel before fuel loading
11. I&C (12)                  ← commission before any nuclear operation
12. Reactor Cell (10)         ← final containment; close before nuclear startup
```

---

## 4. BOM CSV Structure

All `components/*/bom.csv` files share this 10-column schema:

| Column | Type | Notes |
|--------|------|-------|
| `part_id` | string | Prefix + 3-digit (e.g. `RV-001`) |
| `description` | string | Plain English name |
| `material` | string | Common name / alloy name |
| `specification` | string | ASTM/UNS/etc. procurement standard |
| `quantity` | number or `as req'd` | |
| `unit` | enum | `ea`, `m`, `kg`, `L`, `set`, `wall`, `slab` |
| `dimension_1_mm` | number or string | OD / width / diameter |
| `dimension_2_mm` | number or string | wall thickness / depth |
| `dimension_3_mm` | number or string | length / height |
| `notes` | string | Procurement notes, QA requirements |

---

## 5. Key Design Parameters (agent grounding facts)

| Parameter | Value | Source |
|-----------|-------|--------|
| Thermal power | 7.34 MWt design / 8 MWt operated | ORNL-TM-728 |
| Fuel salt | LiF-BeF₂-ZrF₄-UF₄ 65-29.1-5-0.9 mol% | ORNL-TM-728 |
| Core inlet temperature | 632 °C | ORNL-TM-728 |
| Core outlet temperature | 654 °C | ORNL-TM-728 |
| Primary loop flow | ~75.7 L/s (1200 USgpm) | ORNL-TM-728 |
| Reactor vessel OD | 1410 mm | ORNL-TM-728 |
| Graphite stringers | ~509 total (226 Zone I + 283 Zone II) | Calc. from ORNL-TM-728 |
| Primary HX tubes | 159 U-tubes, 9.53 mm OD | ORNL-TM-728 |
| Structural material | Hastelloy-N (INOR-8), UNS N10003 | ORNL-TM-728 |
| Operating pressure | ≤172 kPa gauge | ORNL-TM-728 |
| Tritium production | ~50–200 Ci/year (estimated) | Derived |
