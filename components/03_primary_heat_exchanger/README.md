# Component 03: Primary Heat Exchanger

## Overview

The primary heat exchanger (PHX) transfers thermal energy from the fuel salt (radioactive, primary loop) to the coolant salt (clean, secondary loop). It is a shell-and-tube design with fuel salt on the shell side and coolant salt in the tubes, to minimize the volume of radioactive salt inside tubes (which would increase the activated-material inventory).

**Primary Reference:** ORNL-TM-728, Section 3.4

---

## Operating Conditions

| Parameter | Value |
|-----------|-------|
| Thermal duty | ~7.34 MWt (design); 8 MWt max |
| Fuel salt inlet temperature (shell) | 654 °C (hot from core) |
| Fuel salt outlet temperature (shell) | 632 °C (cold return to core) |
| Coolant salt inlet temperature (tube) | 546 °C (cold from radiator) |
| Coolant salt outlet temperature (tube) | 621 °C (hot to radiator) |
| Fuel salt flow rate | ~75.7 L/s (1200 USgpm) |
| Coolant salt flow rate | ~47.3 L/s (750 USgpm) |
| Operating pressure (both sides) | ≤172 kPa gauge (25 psig) |
| Design pressure (both sides) | 345 kPa gauge (50 psig) |

---

## Heat Exchanger Design

### Type
- **Configuration:** Single-pass shell, U-tube bundle
- **Orientation:** Horizontal (shell axis horizontal)
- **Counterflow arrangement:** Fuel salt and coolant salt flow in opposite directions to maximize LMTD

### Thermal Design Parameters
| Parameter | Value |
|-----------|-------|
| Log-mean temperature difference (LMTD) | ~50.6 °C |
| Overall heat transfer coefficient (U) | ~4,200 W/(m²·K) (estimated for salt-to-salt) |
| Required heat transfer area | ~34.6 m² (372 ft²) |
| Actual heat transfer area (provided) | ~36.5 m² (393 ft²) |
| Design margin | ~5% |

### Tube Bundle
| Parameter | Value |
|-----------|-------|
| Tube OD | 9.53 mm (3/8 in) |
| Tube wall thickness | 0.889 mm (0.035 in) |
| Tube ID | 7.75 mm (0.305 in) |
| Tube material | Hastelloy-N, ASTM B622, UNS N10003 |
| Tube layout | Triangular pitch |
| Tube pitch | 12.7 mm (0.5 in) center-to-center |
| Number of tubes | ~159 |
| Tube active length | ~4,877 mm (192 in; 16 ft) |
| Tube U-bend radius (at far end) | ~25.4 mm (1.0 in) minimum |
| Tubes per row | ~14 |
| Number of tube rows | ~12 |

### Shell
| Parameter | Value |
|-----------|-------|
| Shell OD | ~457 mm (18 in) |
| Shell ID | ~444 mm (17.5 in) |
| Shell wall thickness | 6.35 mm (0.25 in) |
| Shell material | Hastelloy-N, ASTM B622 pipe or rolled plate |
| Shell length (tube sheet to tube sheet) | ~5,030 mm (198 in) |

### Tube Sheets
| Parameter | Value |
|-----------|-------|
| Tube sheet material | Hastelloy-N, ASTM B575 plate |
| Tube sheet thickness | 63.5 mm (2.5 in) |
| Tube-to-tubesheet joint | Strength-welded (no rolled joints) |
| Tube sheet OD | ~470 mm (18.5 in) |

### Baffles
- **Type:** Segmental baffles on shell side to direct fuel salt across tube bundle
- **Baffle cut:** 25%
- **Baffle spacing:** ~203 mm (8 in)
- **Baffle material:** Hastelloy-N, 6.35 mm (0.25 in) thick plate
- **Number of baffles:** ~22

---

## Fuel Salt Flow Path (Shell Side)
1. Enters shell through inlet nozzle (4-in) at the U-bend end of the shell.
2. Flows axially across tube bundle, directed by baffles.
3. Exits shell through outlet nozzle (4-in) at the tube-sheet end.

## Coolant Salt Flow Path (Tube Side)
1. Enters tube-side channel head (cold side) through inlet nozzle (3-in).
2. Flows through tube straight legs to U-bend.
3. Returns through opposite legs back to the same tube sheet.
4. Exits through outlet nozzle (3-in) adjacent to inlet.

---

## Material Specifications

| Part | Material | Specification |
|------|----------|--------------|
| Shell | Hastelloy-N | ASTM B622 seamless pipe or rolled B575 plate |
| Tubes | Hastelloy-N | ASTM B622 seamless tube, 3/8 in × 0.035 in wall |
| Tube sheets (2×) | Hastelloy-N | ASTM B575 plate, 63.5 mm thick |
| Baffles | Hastelloy-N | ASTM B575 plate, 6.35 mm thick |
| Channel heads (2×) | Hastelloy-N | ASTM B575 plate / formed |
| Shell nozzles | Hastelloy-N | ASTM B622 seamless pipe |
| Channel head nozzles | Hastelloy-N | ASTM B622 seamless pipe |
| Weld filler | Hastelloy-N composition | ERNiMo-1 |

---

## Fabrication Requirements

1. All tubes: 100% eddy-current test before installation to check for defects.
2. All tubes: hydrostatic test at 1.5× design pressure before installation.
3. Tube-to-tubesheet weld: full-strength weld (1 pass minimum); 100% visual + dye penetrant.
4. Shell welds: 100% radiograph.
5. Final assembly: pneumatic test at 1.5× design pressure (no hydrostatic testing).
6. Leak test between shell side and tube side: differential pressure test; zero leakage acceptance.
7. Post-weld heat treatment per vessel procedure (1175 °C anneal).

---

## Interfaces

| Interface | Connected To | Connection Type |
|-----------|-------------|-----------------|
| Shell inlet (fuel hot) | Primary loop pipe from reactor vessel outlet | Butt weld, 4-in SCH40 |
| Shell outlet (fuel cold) | Primary loop pipe to reactor vessel inlet | Butt weld, 4-in SCH40 |
| Tube inlet (coolant cold) | Secondary loop pipe from radiator | Butt weld, 3-in SCH40 |
| Tube outlet (coolant hot) | Secondary loop pipe to radiator | Butt weld, 3-in SCH40 |
| Shell exterior | Reactor cell structure | Support saddles, 2× welded |
