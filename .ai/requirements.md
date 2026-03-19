# MSRE Hardware Design — Project Requirements

**Version:** 1.0  
**Date:** 2026-03-17  
**Owner:** pranavkantgaur  

---

## 1. Project Goal

Produce a complete, reproducible, procurement-ready set of hardware designs for the
**Molten Salt Reactor Experiment (MSRE)** — the 7.34 MWt circulating-fluoride-fuel reactor
operated at Oak Ridge National Laboratory from 1965 to 1969.

The repository must enable:
1. A fabrication team (human machinists or robotic fabrication) to build MSRE components
   from these designs without access to the original ORNL drawings.
2. The msr-gstack multi-agent system to review and improve the designs autonomously.
3. The msr_physical_ai_layer to ingest BOM data for automated fabrication planning.
4. The msr_data_layer to store and retrieve design parameters via RAG queries.

---

## 2. In-Scope

- **12 primary MSRE components** as listed in `components/` (reactor vessel, core, primary
  heat exchanger, fuel salt pump, coolant salt pump, fuel drain tank, freeze valves, off-gas
  system, control rods, reactor cell, coolant radiator, instrumentation & control).
- **Bill of Materials (BOM)** for each component: part IDs, materials with ASTM/UNS specs,
  quantities, units, dimensions (mm), and procurement notes.
- **Detailed specifications** per component: dimensional, material, and performance parameters.
- **Multi-agent BOM review** using msr-gstack skills.
- **Supporting documentation**: system overview, safety considerations, materials guide,
  references, flow diagrams, integration notes.

---

## 3. Out of Scope

- **Nuclear fuel fabrication** — UF₄ and ThF₄ chemistry, enrichment, and fuel salt preparation
  are out of scope. Refer to the msr-gstack `/review-fuel-cycle` skill.
- **Civil/structural works** — foundation design, seismic qualification of the building,
  site-specific calculations.
- **Electrical single-line diagrams** — power distribution beyond what is referenced in the
  I&C component.
- **Software / firmware** for the control system — the I&C BOM lists hardware only.
- **Regulatory licensing documents** — this repo does not constitute a Preliminary or Final SAR.
- **Detailed shop drawings / CAD files** — specifications and BOM are sufficient for quote
  solicitation; CAD models are a future deliverable.
- **Vendor qualification** — selection between specific vendors requires a separate procurement
  process.

---

## 4. Safety Constraints

These constraints are non-negotiable and must be preserved by any agent or contributor:

| Constraint | Reason |
|-----------|--------|
| B₄C minimum loading ≥45 kg in drain tank (FDT-006) | Criticality safety — k_eff < 0.95 |
| Crane SWL ≥15 tonne (RCL-008) | Maximum vessel lift ~10.5 t; 1.25× safety factor |
| Type N / Hastelloy-N TC sheath for salt-adjacent sensors | Chromel attack in fluoride environment |
| Tritium monitoring suite mandatory (IC-025/026/027) | Regulatory compliance — cannot operate without |
| Freeze valve fail-to-drain (de-energise to open) | Passive safety — SCRAM on AC loss |
| Hastelloy-N (UNS N10003) for all salt-wetted surfaces | Only material with demonstrated fluoride salt compatibility at 650 °C |

---

## 5. Design Basis

- **Thermal power:** 7.34 MWt design; 8 MWt maximum operated
- **Fuel salt:** LiF-BeF₂-ZrF₄-UF₄ (65-29.1-5-0.9 mol %)
- **Coolant salt:** LiF-BeF₂ (66-34 mol %)
- **Primary loop operating temperature:** 632–654 °C
- **Primary loop pressure:** ≤172 kPa gauge
- **Structural material:** Hastelloy-N (INOR-8), UNS N10003
- **Moderator:** AGOT nuclear-grade graphite, <5 ppm B-equivalent
- **Primary source:** ORNL-TM-728 (Haubenreich et al., 1964)

---

## 6. Quality Requirements

- All BOM CSV files must conform to the 10-column schema in `CLAUDE.md`.
- All material changes require a primary ORNL source citation.
- Safety-critical specifications (B₄C loading, crane SWL, TC type) have QA hold points
  noted in the BOM.
- `make validate` must pass with zero errors on every commit.
