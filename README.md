# MSRE Hardware Design Repository

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

Detailed, reproducible hardware component designs for the **Molten Salt Reactor Experiment (MSRE)** — designed, built, and operated at Oak Ridge National Laboratory (ORNL) from 1965 to 1969.

This repository is structured as an open-hardware reference analogous to Texas Instruments hardware design releases or [echomods](https://github.com/kelu124/echomods/), enabling any organization or startup to replicate MSRE hardware in their workshop using robots or human technicians.

---

## Vision

The goal of this repository is to:

1. **Preserve and version** the detailed hardware designs of the MSRE from ORNL's declassified technical reports.
2. **Enable reproducibility** — any sufficiently equipped workshop (using a fleet of robots or human machinists) should be able to fabricate MSRE components from these designs.
3. **Feed into the MSR Physical-AI layer** ([msr_physical_ai_layer](https://github.com/pranavkantgaur/msr_physical_ai_layer)) for automated fabrication guidance.
4. **Support the MSR multi-agent organization** ([msr-gstack](https://github.com/pranavkantgaur/msr-gstack)) with the first reproducible MSR product.
5. **Integrate with the MSR data layer** ([msr_data_layer](https://github.com/pranavkantgaur/msr_data_layer)) for training physical-AI models.

---

## Repository Structure

```
msre_hardware_design/
├── README.md                        ← This file (system overview & quick start)
├── docs/
│   ├── system_overview.md           ← Full MSRE system description
│   ├── safety_considerations.md     ← Nuclear safety, radiological controls
│   ├── materials_guide.md           ← Hastelloy-N, graphite, salt specifications
│   └── references.md                ← ORNL reports and source documents
├── system/
│   ├── flow_diagram.md              ← Process flow and P&ID description
│   └── integration.md               ← How components connect and interface
└── components/
    ├── 01_reactor_vessel/           ← Hastelloy-N pressure vessel
    ├── 02_reactor_core/             ← Graphite moderator assembly
    ├── 03_primary_heat_exchanger/   ← Fuel-to-coolant salt HX
    ├── 04_fuel_salt_pump/           ← Primary loop centrifugal pump
    ├── 05_coolant_salt_pump/        ← Secondary loop pump
    ├── 06_fuel_drain_tank/          ← Emergency and scheduled drain storage
    ├── 07_freeze_valves/            ← No-moving-part salt freeze valves
    ├── 08_off_gas_system/           ← Fission-gas handling and delay system
    ├── 09_control_rods/             ← Reactivity control assemblies
    ├── 10_reactor_cell/             ← Biological shielding & containment
    ├── 11_coolant_radiator/         ← Air-cooled heat rejection system
    └── 12_instrumentation_control/  ← Nuclear & process instrumentation
```

Each component directory contains:
- `README.md` — design intent, operating principles, and key parameters
- `specifications.md` — full dimensional, material, and performance specifications
- `bom.csv` — bill of materials with material grades and vendor guidance

---

## Quick System Summary

| Parameter | Value |
|---|---|
| Reactor type | Circulating-fuel, graphite-moderated, thermal MSR |
| Design thermal power | 7.34 MWt (operated at up to 8 MWt) |
| Fuel salt | LiF-BeF₂-ZrF₄-UF₄ (65-29.1-5-0.9 mol %), later ²³³UF₄ |
| Coolant salt | LiF-BeF₂ (66-34 mol %) |
| Structural material | Hastelloy-N (INOR-8) |
| Moderator | AGOT nuclear-grade graphite |
| Core inlet temperature | 632 °C (1170 °F) |
| Core outlet temperature | 654 °C (1210 °F) |
| Primary loop flow rate | ~75.7 L/s (1200 USgpm) |
| Primary loop pressure | ~172 kPa (25 psig) max |
| Fuel salt inventory | ~1993 L (70.4 ft³) total |
| Reactor vessel OD | ~1.41 m (55.5 in) |
| Reactor vessel height | ~2.44 m (96 in) overall |

---

## How to Use This Repository

### For Fabrication Teams
1. Start with [`docs/system_overview.md`](docs/system_overview.md) to understand the full system.
2. Read [`docs/safety_considerations.md`](docs/safety_considerations.md) — nuclear and chemical hazards are significant.
3. Review [`docs/materials_guide.md`](docs/materials_guide.md) for material procurement guidance.
4. Navigate to each `components/XX_*/` directory in assembly order.
5. Use `bom.csv` files to generate purchase orders.
6. Use `specifications.md` files as shop drawings reference.

### For Physical-AI Layer Integration
- Component BOM CSV files follow a consistent schema for machine parsing.
- All dimensions are given in both SI (primary) and Imperial (secondary) units.
- Material designations use ASTM/UNS standards where applicable.

### For Researchers
- All designs are traced to primary ORNL sources listed in [`docs/references.md`](docs/references.md).
- Uncertainty or approximation in any specification is noted inline.

---

## Source Information

All hardware specifications are derived from declassified ORNL technical reports, primarily:

- **ORNL-TM-728** — MSRE Design and Operations Report, Part I: Description of Reactor Design (Haubenreich et al., 1964)
- **ORNL-3832** — MSRE Design and Operations Report, Part IIA: Nuclear and Process Instrumentation
- **ORNL-TM-517** — Design and Operating Experience, Fuel and Coolant Pumps
- **ORNL-3014** — MSRE Design Study
- **ORNL-4119** — Operation of MSRE
- **ORNL-4832** — Experience with the MSRE

See [`docs/references.md`](docs/references.md) for the full bibliography.

---

## License

Hardware designs and documentation in this repository are released under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to share and adapt these materials for any purpose, provided you give appropriate credit to ORNL and this repository.

---

## Contributing

Improvements, corrections, and additions from nuclear engineers, materials scientists, and fabrication experts are welcome. Please open an issue or pull request with:
- A reference to the primary ORNL source supporting the change.
- The specific parameter or specification being updated.
- Before/after values with units.

---

*"The MSRE was perhaps the most successful of the early reactor experiments… it demonstrated that a molten-salt reactor could be built, operated, and maintained safely."*
— ORNL-4832
