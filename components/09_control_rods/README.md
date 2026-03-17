# Component 09: Control Rod System

## Overview

The MSRE control rod system provides reactivity control for startup, normal operation, and shutdown. Three control rods are used: two regulating rods for normal power control, and one safety rod for rapid shutdown (SCRAM).

**Primary Reference:** ORNL-TM-728, Section 3.11; ORNL-TM-1490

---

## System Configuration

| Rod | Type | Function | Worth |
|-----|------|----------|-------|
| Rod #1 | Regulating rod | Normal power/reactivity control | ~0.35% Δk/k |
| Rod #2 | Regulating rod | Normal power/reactivity control | ~0.35% Δk/k |
| Rod #3 | Safety rod | SCRAM / emergency shutdown | ~1.25% Δk/k |
| **Total** | | | **~1.95% Δk/k** |

---

## Rod Design

### Neutron Absorber Elements
- **Material:** Gadolinium oxide (Gd₂O₃) mixed with aluminum oxide (Al₂O₃), formed into cylindrical pellets.
- **Cladding:** Inconel 625 (or Hastelloy-N) tubes, butt-welded and sealed — keeps absorber out of contact with fuel salt.
- **Alternate absorber considered:** Eu₂O₃ (less neutron capture per atom than Gd but more uniform worth profile).

### Absorber Element Dimensions

| Parameter | Metric | Imperial |
|-----------|--------|----------|
| Element OD | 25.4 mm | 1.0 in |
| Element wall thickness | 1.65 mm | 0.065 in |
| Element active length | 1,422 mm | 56 in |
| Total rod length (including drive extension) | ~2,032 mm | 80 in |
| Gd₂O₃ content | ~50 wt% Gd₂O₃ + 50 wt% Al₂O₃ | — |
| Element material (cladding) | Inconel 625 | ASTM B446 |

### Poison Pellets
- **Composition:** 50 wt% Gd₂O₃ + 50 wt% Al₂O₃ (co-sintered pellets).
- **Pellet diameter:** 23.6 mm (0.93 in) — loose fit in cladding.
- **Pellet height:** ~12.7 mm (0.5 in).
- **Enrichment:** Natural gadolinium (~14.7% ¹⁵⁷Gd, very high thermal neutron cross section ~255,000 barns).

### Rod Assembly
Each control rod assembly consists of:
- Neutron absorber element (sealed tube with poison pellets).
- Hastelloy-N drive rod extension (connects absorber element to drive mechanism).
- Anti-rotation key (prevents rod from rotating during insertion/withdrawal).
- Dashpot section at rod lower end (buffer for gravity drop of safety rod).

---

## Control Rod Thimbles (In-Core)

See Component 02 (Reactor Core) for thimble dimensions. Summary:
- 3 × Hastelloy-N sealed tubes (44.45 mm OD, 38.05 mm ID) extending full core height.
- Salt does not enter the thimble interior.
- Control rod slides inside thimble without salt contact.

---

## Control Rod Drive Mechanisms

### Regulating Rod Drives (Rods #1 and #2)

| Parameter | Value |
|-----------|-------|
| Drive type | Electric motor-driven rack and pinion |
| Position range | 0 mm (full out / most reactivity) to 508 mm (full in / maximum negative reactivity) |
| Travel speed (normal) | ~1 mm/s (adjustable) |
| Position readout | Linear potentiometer; 0.1 mm resolution |
| Drive motor | AC servo motor, 24 V, 50 W |
| Manual override | Handwheel for manual position adjustment |
| Location | Above reactor vessel top head (outside radiation shielding) |
| Magnetic coupling? | No — mechanical shaft through sealed gland |

### Safety Rod Drive (Rod #3)

| Parameter | Value |
|-----------|-------|
| Drive type | Electromagnetic (solenoid) latch |
| Normal state | Rod held UP (withdrawn) by energized solenoid; reactivity available |
| SCRAM / drop | Solenoid de-energized → rod falls by gravity into core |
| Drop time (full insertion) | <1.0 second |
| Drop distance | 508 mm |
| Reset (re-latch) | Motor-driven winch re-lifts rod; solenoid re-energizes to hold |
| SCRAM triggers | Loss of power; high neutron flux; short reactor period; manual |

---

## SCRAM Logic (Simplified)

```
Any of the following → Safety Rod DROP:
  1. Loss of AC power (solenoid de-energizes)
  2. High neutron flux setpoint exceeded (>110% full power)
  3. Short reactor period (<3 seconds)
  4. Manual SCRAM pushbutton
  5. Loss of primary flow (FI-101 < 80% setpoint)
```

---

## Rod Worth Measurement and Calibration

- Rod worth is measured during initial startup by rod-drop technique (comparing flux decay rate to known β_eff).
- Regulating rod worth is calibrated by inverse multiplication method.
- Worth curves (rod position vs. Δk/k) are generated for each rod and used by the control system.

---

## Interfaces

| Interface | Connected To | Type |
|-----------|-------------|------|
| Control rod lower end | Control rod thimble (in-core) | Sliding fit; clearance ~0.5 mm |
| Control rod upper end | Drive shaft extension | Threaded or pinned connection |
| Drive mechanism | Reactor vessel top head nozzle N3/N4/N5 | Sealed drive housing bolted to nozzle flange |
| Drive motor power | Electrical power system | 24 V DC servo amplifier |
| Position signal | I&C system | 4–20 mA (potentiometer); DCS input |
| SCRAM signal | Safety system relay | 24 V DC relay; de-energize to drop |
