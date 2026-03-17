# Component 11: Coolant Radiator (Air-Cooled Heat Rejection)

## Overview

The coolant radiator rejects heat from the LiF-BeF₂ coolant salt to the atmosphere via forced-air convection. It is the final heat sink for the MSRE's thermal output during normal operation. It also provides decay-heat removal after shutdown.

**Primary Reference:** ORNL-TM-728, Section 3.7

---

## Operating Conditions

| Parameter | Value |
|-----------|-------|
| Heat duty | 7.34 MWt (design), up to 8 MWt operating |
| Coolant salt inlet temperature | ~621 °C (from primary HX) |
| Coolant salt outlet temperature | ~546 °C (to primary HX) |
| Coolant salt flow rate | ~47.3 L/s (750 USgpm) |
| Air inlet temperature (design summer) | 38 °C (100 °F) |
| Air flow rate | ~70.8 m³/s (150,000 cfm) |
| Air-side pressure drop | ~125 Pa (0.5 in H₂O) |
| Coolant salt pressure drop | ~35 kPa (5 psi) |
| Tube-side operating pressure | ≤172 kPa gauge (25 psig) |
| Design pressure (tube side) | 345 kPa gauge (50 psig) |

---

## Radiator Design

### Type
- Finned-tube, forced-draft or induced-draft air cooler (similar to industrial air-cooled heat exchanger).
- Multiple tube passes; salt flows inside tubes; air flows across finned exterior.

### Tube Bundle Parameters

| Parameter | Value |
|-----------|-------|
| Tube OD | 25.4 mm (1.0 in) |
| Tube wall thickness | 1.65 mm (0.065 in) |
| Tube ID | 22.1 mm (0.870 in) |
| Tube material | Hastelloy-N |
| Fin type | Wound spiral fins (Hastelloy-N or nickel alloy) |
| Fin OD | 50.8 mm (2.0 in) |
| Fin thickness | 0.89 mm (0.035 in) |
| Fin pitch | 4 fins/cm (10 fins/in) |
| Tube pitch (triangular) | 63.5 mm (2.5 in) |
| Number of tubes per pass | ~36 |
| Number of tube passes | ~4 |
| Active tube length | ~6,096 mm (20 ft) |
| Total finned tube count | ~144 tubes |
| Total air-side heat transfer area | ~2,800 m² (including fin area) |

### Headers
- **Material:** Hastelloy-N
- **Coolant salt inlet header:** 3-in SCH40 Hastelloy-N pipe, manifold distributing to tube bundle inlet
- **Coolant salt outlet header:** 3-in SCH40 Hastelloy-N pipe
- Header wall thickness: 9.53 mm (0.375 in)
- Header internal volume: ~40 L (minimizes salt inventory outside heat exchanger tubes)

---

## Fan and Air-Side System

| Parameter | Value |
|-----------|-------|
| Fan type | Forced-draft centrifugal or axial fan |
| Number of fans | 4 (2 operating + 2 standby) |
| Fan capacity (each operating fan) | ~17.7 m³/s (37,500 cfm) at design pressure drop |
| Fan motor | 30 kW (40 hp) each; 460 V AC, 3-phase |
| Fan speed | ~900 rpm (variable speed preferred for power control) |
| Air dampers | Motorized inlet dampers, one per fan |
| Fan structure | Carbon steel ductwork; galvanized or painted |

### Decay Heat Removal
- After shutdown, decay heat is initially ~7% of operating power (~560 kW at t=0).
- The air-cooled radiator can remove this heat with reduced coolant flow.
- If coolant salt pump is not running (extended power failure), natural convection of coolant salt through the radiator and primary HX provides some heat removal.
- Natural convection requires radiator to be *above* the primary HX by ≥0.5 m vertical separation.

---

## Radiator Location and Orientation

- Located in the pump house, separated from the reactor cell.
- Oriented vertically (tubes horizontal; air flows horizontally through the bundle).
- The pump house is adjacent to but separated from the reactor cell; radioactivity level is low (coolant salt is clean during normal operation).
- Air inlet: outside building face (screened against insects/debris).
- Air outlet: through roof or opposite building face (directed away from personnel areas).

---

## Heat Tracing

- Coolant salt in radiator must remain above liquidus (~460 °C) during standby.
- All radiator tubes and headers are heat-traced with resistance wire or MI cable.
- Heat tracing power: ~50 kW total for full radiator assembly at ambient temperature.
- Radiator tubes must be preheated before admitting coolant salt to prevent thermal shock.

---

## Materials

| Component | Material | Specification |
|-----------|----------|--------------|
| Tubes | Hastelloy-N | ASTM B622 seamless, 1.0 in OD × 0.065 in WT |
| Fins | Hastelloy-N or nickel 200 | ASTM B622 strip or ASTM B162 |
| Headers | Hastelloy-N | ASTM B575 plate |
| Air ductwork and housing | Galvanized carbon steel | ASTM A653 G90 |
| Fan blades | Aluminum alloy | ASTM B209 6061-T6 |
| Fan motor | TEFC AC induction | NEMA MG1 |

---

## Interfaces

| Interface | Connected To | Type |
|-----------|-------------|------|
| Coolant salt inlet | Secondary loop pipe from primary HX tube outlet | 3-in SCH40 butt weld |
| Coolant salt outlet | Secondary loop pipe to coolant salt pump inlet | 3-in SCH40 butt weld |
| Air inlet | Outdoor air (through louvers/screens) | Ductwork connection |
| Air outlet | Building exhaust (through roof or wall) | Ductwork connection |
| Fan motors | 460 V AC electrical panel | Conduit, motor starters |
| Damper actuators | I&C system | 24 V DC, 4-20 mA control |
