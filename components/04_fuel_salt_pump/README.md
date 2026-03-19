# Component 04: Fuel Salt Pump

## Overview

The fuel salt pump circulates the radioactive fuel salt around the primary loop. It is a centrifugal sump-type (canned) pump with a cantilevered shaft — no bearings below the salt surface, eliminating submerged bearing lubrication challenges with hot salt.

**Primary Reference:** ORNL-TM-517; ORNL-TM-728, Section 3.5

---

## Operating Conditions

| Parameter | Value |
|-----------|-------|
| Fluid | LiF-BeF₂-ZrF₄-UF₄ fuel salt |
| Flow rate | ~75.7 L/s (1200 USgpm) |
| Developed head | ~18.3 m (60 ft) |
| Pump inlet temperature | ~632 °C (1170 °F) |
| Pump bowl temperature | ~640 °C |
| Operating pressure (suction) | ~35–55 kPa gauge (5–8 psig) |
| Operating pressure (discharge) | ~172 kPa gauge (25 psig) |
| Shaft speed | 1750 rpm |
| Motor power | 75 hp (56 kW) |
| Fluid density at operating T | ~2.24 g/cm³ |
| Fluid viscosity at operating T | ~9 cP |

---

## Pump Design — Sump (Bowl) Type

### Design Concept
The pump is a sump-type centrifugal pump where:
- The impeller is at the *bottom* of a long vertical shaft, submerged in the fuel salt.
- The motor is at the *top*, outside the reactor cell, in an ambient-temperature environment.
- The shaft is cantilevered — the upper bearing is the only bearing (above the salt); there are no submerged bearings.
- The pump bowl (reservoir) holds a free surface of fuel salt, maintaining a gas (helium) blanket above the salt for cover gas and off-gas removal.
- The long shaft (typically ~1.8 m / 72 in) thermally isolates the bearing and motor from the hot salt.

### Key Dimensions

| Parameter | Metric | Imperial |
|-----------|--------|----------|
| Pump bowl OD | ~609.6 mm | 24 in |
| Pump bowl height | ~609.6 mm | 24 in |
| Pump shaft length (total) | ~1,829 mm | 72 in |
| Pump shaft diameter | ~50.8 mm | 2 in |
| Impeller diameter | ~203 mm | 8 in |
| Pump bowl wall thickness | 9.53 mm | 0.375 in |
| Discharge pipe connection | 4-in SCH40 | 4-in SCH40 |
| Suction opening | ~152 mm (6 in) (open bottom of bowl to loop) | 6 in |

### Materials

| Part | Material | Specification |
|------|----------|--------------|
| Pump bowl | Hastelloy-N | ASTM B622 / B619 pipe or rolled B575 plate |
| Impeller | Hastelloy-N | Investment casting or machined from B575 bar |
| Pump shaft | Hastelloy-N | ASTM B574 bar, UNS N10003 |
| Volute/casing | Hastelloy-N | Cast or fabricated |
| Shaft seal (upper) | Face seal, carbon/graphite vs. Hastelloy-N | Dry-running; helium purge above salt |
| Bearing (upper) | Ball bearing, oil-lubricated, in ambient environment | Standard 80 mm bore bearing |
| Motor | Air-cooled induction motor, 75 hp, 1750 rpm, TEFC | IEEE 841 motor or equivalent |
| Coupling (motor to shaft) | Flexible coupling (Lovejoy or equivalent), rated for temperature gradient | — |

---

## Pump Bowl Features

### Gas Space
- Helium cover gas maintained above fuel salt surface in pump bowl.
- Gas space volume: ~15 L (to absorb thermal expansion of salt in loop without overpressure).
- He sparge gas: introduced below salt surface at ~0.5 L/min to strip dissolved noble gases.
- Off-gas line: ~12.7 mm (0.5 in) pipe from gas space to off-gas system.

### Salt Level Monitoring
- Differential pressure taps at top and bottom of gas space.
- Gamma densitometer: detects salt level by measuring density of gas vs. liquid zones.

### Overflow Protection
- If salt level in pump bowl rises above design high-level, overflow line routes excess salt back to loop suction piping.
- Overflow line: ~25.4 mm (1 in) Hastelloy-N tube, heat-traced, with freeze valve.

---

## Shaft Seal and Thermal Barrier

- The shaft passes through the pump bowl cover gas space; a labyrinth seal (non-contact) at the bowl cover plate limits helium leakage to the pump housing.
- A purge flow of helium (≥1 L/min) maintains positive pressure toward the salt side, preventing salt vapor or aerosol from reaching the upper bearing.
- A thermal barrier (actively cooled or long thermal path) keeps the upper bearing/motor environment below 100 °C while salt is at 640 °C.
- Thermal barrier: ~500 mm (20 in) of un-insulated Hastelloy-N shaft in stagnant N₂ reduces shaft temperature gradient; additional water-cooled collar at shaft midpoint.

---

## Motor and Drive

| Parameter | Value |
|-----------|-------|
| Motor type | AC induction, squirrel cage |
| Power rating | 75 hp (56 kW) |
| Voltage | 460 V AC, 3-phase, 60 Hz |
| Speed | 1750 rpm (4-pole motor) |
| Enclosure | TEFC (Totally Enclosed Fan Cooled) |
| Motor mounting | Vertical, flange-mounted to pump housing top plate |
| Variable speed? | No (fixed speed at 1750 rpm; flow cannot be throttled during operation) |

---

## Flow Control
- No flow throttling during normal operation; pump runs at constant speed.
- Primary loop flow rate set by pump speed and system hydraulic resistance.
- During startup, primary loop is cold; salt viscosity higher → slightly lower flow until design temperature reached.

---

## Maintenance Approach
- Pump is located in the reactor cell (high radiation after operation).
- Pump motor assembly (above shielding) can be accessed directly.
- Pump bowl and impeller require remote maintenance with shielded tools.
- The pump is designed with a bolted cover plate (top) that can be remotely removed to access internals.
- Pump replacement: full pump assembly lifted out of cell by overhead crane; spare assembly installed.

---

## Interfaces

| Interface | Connected To | Type |
|-----------|-------------|------|
| Pump suction (bowl bottom) | Primary loop return from HX | Open annulus; loop pipe connects to bowl base |
| Pump discharge | Primary loop pipe to reactor vessel inlet | 4-in SCH40 butt weld |
| Motor shaft | Pump shaft | Flexible coupling |
| He cover gas supply | Inert gas system | 12.7 mm compression fitting |
| Off-gas outlet | Off-gas system | 12.7 mm tube, butt weld |
| Thermal barrier cooling | Facility cooling water or N₂ | Compression fitting, ½-in tube |
