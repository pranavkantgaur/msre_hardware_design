# Component 05: Coolant Salt Pump

## Overview

The coolant salt pump circulates the secondary (clean, non-radioactive) LiF-BeF₂ coolant salt through the secondary loop: primary heat exchanger → coolant radiator → back to primary heat exchanger.

It is similar in design to the fuel salt pump but smaller (lower flow rate and power) and less radiologically constrained.

**Primary Reference:** ORNL-TM-517; ORNL-TM-728, Section 3.6

---

## Operating Conditions

| Parameter | Value |
|-----------|-------|
| Fluid | LiF-BeF₂ (Flibe) coolant salt |
| Flow rate | ~47.3 L/s (750 USgpm) |
| Developed head | ~18.3 m (60 ft) |
| Pump inlet temperature | ~546 °C (cold from radiator) |
| Pump bowl temperature | ~580 °C |
| Operating pressure (suction) | ~35 kPa gauge (5 psig) |
| Operating pressure (discharge) | ~172 kPa gauge (25 psig) |
| Shaft speed | 1750 rpm |
| Motor power | 30 hp (22 kW) |
| Fluid density at operating T | ~1.94 g/cm³ |
| Fluid viscosity at operating T | ~6 cP |

---

## Pump Design

Identical design philosophy as the fuel salt pump (Component 04):
- Sump/bowl type centrifugal pump
- Cantilevered shaft, no submerged bearings
- Helium cover gas above salt surface in pump bowl
- Motor above reactor cell wall (secondary loop is in the pump house, not the reactor cell)

Since the coolant salt is not radioactive during normal operation (low activation), remote maintenance is less stringent than the fuel salt pump.

### Key Dimensions

| Parameter | Metric | Imperial |
|-----------|--------|----------|
| Pump bowl OD | ~457 mm | 18 in |
| Pump bowl height | ~457 mm | 18 in |
| Pump shaft length (total) | ~1,524 mm | 60 in |
| Pump shaft diameter | ~38.1 mm | 1.5 in |
| Impeller diameter | ~178 mm | 7 in |
| Pump bowl wall thickness | 7.94 mm | 0.313 in |
| Discharge pipe connection | 3-in SCH40 | 3-in SCH40 |

### Materials

| Part | Material | Specification |
|------|----------|--------------|
| Pump bowl | Hastelloy-N | ASTM B619/B622 or B575 |
| Impeller | Hastelloy-N | Cast or machined |
| Pump shaft | Hastelloy-N | ASTM B574 bar |
| Shaft seal | Face seal, carbon vs. Hastelloy-N | Similar to fuel pump |
| Bearing | Ball bearing, oil-lubricated | Standard |
| Motor | AC induction, 30 hp, 1750 rpm, TEFC | IEEE 841 |

---

## Differences from Fuel Salt Pump

| Aspect | Fuel Salt Pump | Coolant Salt Pump |
|--------|---------------|-------------------|
| Flow rate | 1200 USgpm | 750 USgpm |
| Motor power | 75 hp | 30 hp |
| Bowl OD | 609.6 mm | 457 mm |
| Shaft length | 1829 mm | 1524 mm |
| Radiation environment | High (reactor cell) | Low (pump house) |
| Remote maintenance required | Yes | Limited |
| Thermal barrier | More elaborate | Simpler |

---

## Interfaces

| Interface | Connected To | Type |
|-----------|-------------|------|
| Pump suction (bowl bottom) | Secondary loop return from radiator | 3-in SCH40 butt weld |
| Pump discharge | Secondary loop to primary HX tube inlet | 3-in SCH40 butt weld |
| Motor shaft | Pump shaft | Flexible coupling |
| He cover gas | Inert gas system | Compression fitting |
| Off-gas (if any activation) | Vent or off-gas | 12.7 mm tube |
