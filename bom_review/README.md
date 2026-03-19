# MSRE Hardware Design — BOM Review

**Reviewed by:** msr-gstack multi-agent system  
**Source:** https://github.com/pranavkantgaur/msr-gstack/tree/copilot/setup-multi-agent-system  
**Hardware designs reviewed:** https://github.com/pranavkantgaur/msre_hardware_design/tree/copilot/create-hardware-designs-msre/components  
**Review date:** 2026-03-17  

---

## What Is msr-gstack?

[msr-gstack](https://github.com/pranavkantgaur/msr-gstack) is a multi-agent organization system
for MSR development, modelled on the gstack framework. Each agent is a domain specialist with a
structured review workflow defined in a `SKILL.md` file. Agents are invoked by pointing an AI
assistant at the relevant skill and providing the material to review.

---

## Agents Invoked

Six of the nine msr-gstack agents were invoked for this BOM review. Their skills were applied
directly to the twelve component BOM CSV files in `components/*/bom.csv`.

| Agent | Skill File | Components Reviewed |
|-------|-----------|---------------------|
| **Reactor Design Engineer** | `review-reactor-design/SKILL.md` | 01 Vessel, 02 Core, 03 HX, 09 Control Rods |
| **Materials Engineer** | `review-materials/SKILL.md` | All 12 components (material selection) |
| **Safety Analyst** | `review-safety/SKILL.md` | 06 Drain Tank, 07 Freeze Valves, 09 Control Rods, 10 Cell |
| **I&C Engineer** | `review-instrumentation/SKILL.md` | 07 Freeze Valves, 08 Off-Gas, 12 I&C |
| **Molten Salt Expert** | `review-salt-chemistry/SKILL.md` | 01 Vessel, 03 HX, 04/05 Pumps, 06 Drain Tank |
| **Fuel Cycle Chemist** | `review-fuel-cycle/SKILL.md` | 02 Core, 08 Off-Gas (noble gas removal) |

Not invoked: `plan-program-review`, `plan-cto-review`, `retro-rd` (these are plan/strategy reviews,
not component-level BOM reviews).

---

## Finding Severity Levels

| Severity | Meaning |
|----------|---------|
| 🔴 **CRITICAL** | Safety-basis error, missing safety-critical specification, or BOM omission that would prevent safe fabrication/operation |
| 🟠 **SIGNIFICANT** | Technical error affecting design validity, dimension mismatch, procurement-blocking omission, or unresolved reference |
| 🟡 **MINOR** | Documentation gap, notation, approximation needing refinement, or clarification needed |
| ✅ **PASS** | Reviewed and verified consistent with specifications and applicable standards |

---

## Summary Table

| # | Component | Critical | Significant | Minor | Agent(s) |
|---|-----------|----------|-------------|-------|---------|
| 01 | Reactor Vessel | 0 | 2 | 2 | Reactor Design, Materials |
| 02 | Reactor Core | 0 | 2 | 2 | Reactor Design, Materials, Fuel Cycle |
| 03 | Primary Heat Exchanger | 0 | 1 | 2 | Reactor Design, Materials, Salt |
| 04 | Fuel Salt Pump | 0 | 0 | 2 | Materials, Salt |
| 05 | Coolant Salt Pump | 0 | 1 | 0 | Materials |
| 06 | Fuel Drain Tank | 1 | 1 | 1 | Safety, Salt |
| 07 | Freeze Valves | 0 | 2 | 0 | Safety, I&C, Salt |
| 08 | Off-Gas System | 1 | 0 | 1 | Fuel Cycle, I&C |
| 09 | Control Rods | 0 | 2 | 1 | Reactor Design, Safety, Materials |
| 10 | Reactor Cell | 0 | 2 | 1 | Safety |
| 11 | Coolant Radiator | 0 | 0 | 1 | Materials |
| 12 | Instrumentation & Control | 1 | 3 | 0 | I&C, Safety |
| **TOTAL** | | **3** | **16** | **13** | |

---

## Critical Findings (3)

| ID | Component | Finding |
|----|-----------|---------|
| C-01 | 06 Fuel Drain Tank | B₄C neutron absorber loading (FDT-006) has no specified mass — "as req'd, kg" — for a safety-critical criticality control component |
| C-02 | 08 Off-Gas System | No tritium monitoring equipment in the off-gas BOM; tritium exits the primary loop through the off-gas stream and requires continuous measurement |
| C-03 | 12 I&C | No tritium monitoring system items in the I&C BOM; no ionization chamber, Lucas cell, or catalytic oxidizer for tritium quantification anywhere in system |

---

## Full Review

See [`consolidated_bom_review.md`](consolidated_bom_review.md) for the complete component-by-component
review with detailed findings, agent reasoning, and recommended corrective actions.
