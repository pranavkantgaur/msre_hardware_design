# System Flow Diagram and P&ID Description

This document describes the Process Flow Diagram (PFD) and the Piping and Instrumentation Diagram (P&ID) of the MSRE in textual form, as a reference for creating actual engineering drawings.

---

## 1. Primary Loop (Fuel Salt Circuit)

### Flow Path (Normal Operation)

```
[Reactor Vessel — Core Outlet Plenum]
          |
          | (4-in Hastelloy-N pipe, ~650 °C)
          ↓
[Fuel Salt Pump — Bowl/Sump]
  - Centrifugal, sump-type
  - 1750 rpm, 75 hp motor
  - Pump discharge: ~170 kPa (25 psi) above suction
          |
          | (4-in pipe, pump discharge)
          ↓
[Primary Heat Exchanger — Shell Side (fuel salt)]
  - Single-pass shell, U-tube bundle
  - Fuel salt enters top, exits bottom of shell
  - Heat transferred to coolant salt (tube side)
          |
          | (4-in pipe, ~632 °C)
          ↓
[Reactor Vessel — Core Inlet Plenum]
  - Fuel salt distributed to graphite core channels
  → [Reactor Core Channels] → Core Outlet Plenum (loop closes)
```

### Primary Loop Instrumentation Points

| Tag | Parameter | Location | Type |
|-----|-----------|----------|------|
| TI-101 | Fuel Salt Temperature (core inlet) | Core inlet pipe | Thermocouple (Type K, Inconel sheath) |
| TI-102 | Fuel Salt Temperature (core outlet) | Core outlet pipe | Thermocouple (Type K) |
| TI-103 | Fuel Salt Temperature (pump bowl) | Pump bowl | Thermocouple (Type K) |
| TI-104 | Fuel Salt Temperature (HX outlet) | HX fuel outlet | Thermocouple (Type K) |
| FI-101 | Fuel Salt Flow Rate | Primary loop pipe | Magnetic flowmeter (AC excitation) |
| PI-101 | Fuel Salt Pressure | Pump discharge | Differential pressure cell |
| LI-101 | Fuel Salt Level (pump bowl) | Pump bowl | Differential pressure / gamma densitometer |

---

## 2. Secondary Loop (Coolant Salt Circuit)

### Flow Path (Normal Operation)

```
[Coolant Salt Pump — Bowl/Sump]
  - Centrifugal, sump-type
  - 1750 rpm, 30 hp motor
          |
          | (3-in Hastelloy-N pipe, ~621 °C)
          ↓
[Primary Heat Exchanger — Tube Side (coolant salt)]
  - Coolant salt in tubes (U-tube)
  - Coolant salt enters at ~546 °C, exits at ~621 °C
          |
          | (after HX, now at ~621 °C... wait)
```

> **Clarification:** Coolant salt is *heated* in the primary HX (absorbs heat from fuel salt), then *cooled* in the radiator.

```
[Primary Heat Exchanger — Tube Side]
  Coolant enters at ~546 °C (cold), exits at ~621 °C (hot)
          |
          ↓
[Coolant Radiator]
  - Air-cooled finned-tube heat exchanger
  - Removes heat to atmosphere
  - Coolant exits at ~546 °C
          |
          ↓
[Coolant Salt Pump — Suction] (loop closes)
```

### Secondary Loop Instrumentation Points

| Tag | Parameter | Location | Type |
|-----|-----------|----------|------|
| TI-201 | Coolant Salt Temp (HX inlet) | Coolant inlet to HX | Thermocouple (Type K) |
| TI-202 | Coolant Salt Temp (HX outlet) | Coolant outlet from HX | Thermocouple (Type K) |
| TI-203 | Coolant Salt Temp (radiator outlet) | Radiator outlet | Thermocouple (Type K) |
| FI-201 | Coolant Salt Flow Rate | Secondary loop pipe | Magnetic flowmeter |
| TI-204 | Air Inlet Temperature | Radiator air inlet | RTD |
| TI-205 | Air Outlet Temperature | Radiator air outlet | RTD |

---

## 3. Fuel Drain System

### Normal Drain (Scheduled Maintenance)

```
[Primary Loop]
        |
        | (freeze valve FV-103 — thawed to allow drain)
        ↓
[Fuel Drain Tank (FDT)]
  - Gravity drain; primary loop runs 0.6 m above drain tank top
  - Tank capacity: full primary loop inventory + thermal expansion margin
  - Tank heated to keep salt molten (>460 °C)
        |
        ↓ (via overflow line + freeze valve FV-104)
[Overflow Tank (OFT)]
  - Captures any overfill from FDT
```

### Emergency Drain (Passive Safety)

```
Loss of power / reactor trip signal
        ↓
Heaters on freeze valve FV-103 de-energize
        ↓
FV-103 thaws (decay heat from adjacent piping melts salt plug)
        ↓
Fuel salt drains by gravity to FDT (subcritical geometry)
        ↓
Reactor shutdown achieved passively (~30 minutes for complete drain)
```

### Freeze Valve Designations

| Tag | Location | Function |
|-----|----------|---------|
| FV-101 | Fuel loop drain line, main | Primary loop → FDT |
| FV-102 | Sampler/enricher loop | Fuel additions |
| FV-103 | FDT → loop refill | Return fuel from FDT to loop |
| FV-104 | FDT overflow | FDT → overflow tank |
| FV-201 | Coolant drain | Coolant loop → coolant drain tank |

---

## 4. Off-Gas System

```
[Pump Bowl Cover Gas (He sparge)]
  - Helium introduced below fuel salt surface in pump bowl
  - Strips volatile fission products (Xe, Kr, etc.) from fuel salt
        |
        ↓
[Off-Gas Line] — 12.7 mm (0.5 in) Hastelloy-N tubing
        |
        ↓
[Water-Cooled Trap]
  - Condensed water and some aerosols removed
        |
        ↓
[Activated Charcoal Delay Beds]
  - Bed 1: ambient temperature charcoal, ~250 L volume
  - Bed 2: water-cooled charcoal (for longer Xe/Kr decay)
  - Decay time for ¹³³Xe: >10 half-lives in beds
        |
        ↓
[HEPA Filter] — sintered metal
        |
        ↓
[Stack / Vent]  (only after adequate decay)
```

### Off-Gas System Instrumentation

| Tag | Parameter |
|-----|-----------|
| FI-301 | He sparge gas flow rate |
| PI-301 | Off-gas line pressure |
| RI-301 | Off-gas line radiation monitor |
| TI-301 | Charcoal bed temperature |

---

## 5. Control Rod System

```
[Control Rod Drives — above reactor vessel]
  - Vertical shaft, magnetic coupling through vessel top head
  - Motor/magnetic drive (2× regulating, 1× safety rod)
        |
        ↓ (rods extend downward into core)
[Control Rod Thimbles — inside graphite core]
  - Gd₂O₃/Al₂O₃ neutron absorber elements
  - Rod position: 0 (fully withdrawn) to 50.8 cm (fully inserted)
        |
        ↓ (safety rod)
[Gravity Drop Mechanism]
  - Safety rod falls by gravity on loss of power or SCRAM signal
  - Drop time: <1 second for full insertion
```

### Reactivity Worth (approximate)

| Rod | Worth |
|-----|-------|
| Regulating rod #1 | ~0.35% Δk/k (full travel) |
| Regulating rod #2 | ~0.35% Δk/k (full travel) |
| Safety rod | ~1.25% Δk/k (full travel) |
| Total (all rods in) | ~1.95% Δk/k |

---

## 6. Reactor Cell Atmosphere Control

```
[N₂ Supply] (dry, oil-free)
        ↓
[Reactor Cell]
  - Maintained at slight negative pressure (~0.5 in H₂O below atmospheric)
  - N₂ sweep prevents air/moisture ingress
        ↓
[Cell Atmosphere Exhaust Monitors]
  - Radiation monitor (gamma) on cell exhaust
  - Smoke/aerosol detector
        ↓
[Cell Exhaust HEPA Filter + Charcoal]
        ↓
[Stack Vent]
```

---

## 7. Key Interlock Logic (Simplified)

| Condition | Action |
|-----------|--------|
| Loss of AC power | Safety rod drops; pump coast-down; freeze valves begin thaw |
| High reactor period (<3 s) | SCRAM: safety rod drops |
| High neutron flux (>110% FP) | SCRAM |
| Loss of primary flow (FI-101 < 80%) | SCRAM |
| Reactor cell high radiation | Alarm; operator action |
| Pump bowl level high | Alarm; check for freeze valve leak |
| Drain tank overpressure | Relief to off-gas system |

---

*Detailed instrument loop diagrams and electrical schematics are referenced in ORNL-3832 (nuclear & process instrumentation) and ORNL-TM-0729 (electrical & mechanical instrumentation).*
