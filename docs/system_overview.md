# MSRE System Overview

## Introduction

The Molten Salt Reactor Experiment (MSRE) was a 7.34 MWt (design) / ~8 MWt (peak operated) graphite-moderated, circulating-fluoride-salt reactor operated at Oak Ridge National Laboratory (ORNL), Oak Ridge, Tennessee from June 1965 to December 1969. It was the first sustained operation of a fluid-fueled molten-salt reactor and validated the molten salt reactor concept for power generation.

The MSRE demonstrated:
- Stable operation of a circulating liquid-fluoride fuel system.
- Successful use of Hastelloy-N as the primary structural material in contact with fluoride salts at high temperature.
- Remote maintenance of radioactive components (pumps, heat exchanger) using shielded equipment.
- Fuel chemistry control (redox potential, fissile addition) in an operating reactor.
- Operation with both ²³⁵U and ²³³U fuels.

---

## System Architecture

The MSRE consists of three main fluid loops and the associated support systems:

### Primary Loop (Fuel Salt Loop)
Circulates fluoride fuel salt through the reactor core, primary heat exchanger, and back to the core. Fission heat is generated in the fuel salt within the graphite moderator core.

**Working fluid:** LiF-BeF₂-ZrF₄-UF₄ salt mixture  
**Temperature range:** 632 °C (inlet) to 654 °C (outlet)  
**Flow rate:** ~75.7 L/s (1200 USgpm)  
**Operating pressure:** ~172 kPa gauge (25 psig) maximum

### Secondary Loop (Coolant Salt Loop)
Transfers heat from the primary heat exchanger to the coolant radiator. Thermally isolated from the fuel salt and contains no fissile material.

**Working fluid:** LiF-BeF₂ (Flibe) salt  
**Temperature range:** 546 °C (inlet to HX) to 621 °C (outlet from HX)  
**Flow rate:** ~47.3 L/s (750 USgpm)  
**Operating pressure:** ~172 kPa gauge (25 psig) maximum

### Tertiary Loop (Air Cooling Loop)
Removes heat from the coolant radiator to the atmosphere via forced-air cooling. Used during normal operation and for decay-heat removal after shutdown.

**Working fluid:** Atmospheric air  
**Air flow rate:** ~70.8 m³/s (150,000 cfm) at full power  
**Heat rejection:** ~7.34 MWt (design), up to 8 MWt operated

---

## Primary System Components

| No. | Component | Function |
|-----|-----------|----------|
| 1 | Reactor Vessel | Houses graphite core; contains and directs fuel salt flow |
| 2 | Reactor Core (Graphite) | Moderates neutrons; provides flow channels for fuel salt |
| 3 | Primary Heat Exchanger | Transfers heat from fuel salt to coolant salt |
| 4 | Fuel Salt Pump | Circulates fuel salt around primary loop |
| 5 | Coolant Salt Pump | Circulates coolant salt in secondary loop |
| 6 | Fuel Drain Tanks | Emergency and scheduled storage of fuel salt |
| 7 | Freeze Valves | Control salt flow; no mechanical moving parts |
| 8 | Off-Gas System | Collects and delays fission product gases |
| 9 | Control Rods | Reactivity control (2 regulating + 1 safety rod) |
| 10 | Reactor Cell | Biological shielding, containment, inert atmosphere |
| 11 | Coolant Radiator | Air-cooled heat rejection from secondary loop |
| 12 | Instrumentation & Control | Nuclear and process measurement and control |

---

## Primary Loop Flow Path

```
Reactor Core (fuel salt heated by fission)
        ↓
Fuel Salt Pump (upper plenum → pump bowl)
        ↓
Primary Heat Exchanger (fuel salt shell side, coolant salt tube side)
        ↓
Lower plenum → Reactor Core inlet (loop repeats)
```

**Loop volume:** ~1993 L (70.4 ft³) total fuel salt in system  
**Pipe diameter (main):** ~101.6 mm (4 in) schedule-40 Hastelloy-N  
**Average fuel velocity in core channels:** ~0.22 m/s  
**Fuel residence time in core:** ~7.4 s (at design flow)

---

## Secondary Loop Flow Path

```
Primary Heat Exchanger (coolant salt heated, tube side)
        ↓
Coolant Salt Pump
        ↓
Coolant Radiator (air-cooled)
        ↓
Primary Heat Exchanger inlet (loop repeats)
```

**Loop volume:** ~378 L (100 USgal) coolant salt  
**Pipe diameter (main):** ~76.2 mm (3 in) Hastelloy-N

---

## Reactor Building Layout

The MSRE was housed in a reinforced concrete building. The main areas were:

| Area | Description |
|------|-------------|
| Reactor Cell | Heavily shielded room containing reactor vessel, primary HX, fuel pump, drain tanks, and all radioactive primary piping. N₂-purged atmosphere. |
| Drain Tank Cell | Adjacent cell housing fuel drain tanks and associated piping. |
| Pump House | Contains coolant salt pump, coolant radiator, and secondary loop equipment. |
| Off-Gas Cell | Isolated cell housing charcoal delay beds and off-gas processing equipment. |
| Control Room | Remote instrumentation and control consoles; no direct radiation exposure during normal operation. |
| Maintenance Area | Overhead crane, shielded viewing window, and remote-handling tools for maintenance. |

---

## Operating History Summary

| Period | Event |
|--------|-------|
| 1960–1964 | Design and construction |
| June 1965 | Initial criticality with ²³⁵U fuel |
| July 1966 | Reached full design power |
| 1968 | Fuel changed to ²³³U (first reactor to operate on ²³³U) |
| December 1969 | Final shutdown |
| 1969–1973 | Decontamination, post-operation surveillance |

Total operation: ~13,172 MWh(t) total thermal energy produced ≈ **1,795 EFPH at rated power (7.34 MWt)**. Some historical ORNL summaries express this as ~13,000 "equivalent full-power hours at 1 MWt" reference — a non-standard unit; verify exact figure against ORNL-4832.

---

## Key Design Principles

1. **Fuel salt as both fuel and coolant** — eliminates fuel element fabrication and radiation damage concerns for the fuel.
2. **Freeze valves instead of mechanical valves** — no moving parts in contact with radioactive salt; passive fail-safe drain capability.
3. **Hastelloy-N structural material** — specifically developed at ORNL for resistance to fluoride salt corrosion at high temperature.
4. **Graphite moderator** — chemically compatible with fuel salt; low neutron absorption; provides flow channels.
5. **Negative temperature coefficient of reactivity** — inherently self-regulating; power decreases as temperature rises.
6. **Atmospheric pressure operation** — primary loop pressure is low (only pump head), simplifying containment design.
