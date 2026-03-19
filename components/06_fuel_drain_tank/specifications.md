# Fuel Drain Tank — Detailed Specifications

**Reference:** ORNL-TM-728, Sections 3.7, 3.8; ORNL-TM-1647

---

## 1. Main Fuel Drain Tank (FDT) — Criticality Safety Analysis Basis

### Geometry Basis
The annular geometry ensures the salt layer thickness is below the critical dimension for any fissile loading and moderator condition.

| Parameter | Value |
|-----------|-------|
| Annular salt layer thickness | 152 mm (6.0 in) |
| Uranium-235 density in salt | ~41 g U235/L salt |
| Maximum k-eff (salt only, dry) | <0.85 |
| Maximum k-eff (salt + reflected, dry) | <0.90 |
| Maximum k-eff (salt + full water flooding) | <0.95 |
| Safety margin | >5% Δk/k below critical |

### Center Column Neutron Absorber Loading
- Minimum ¹⁰B content in center column: determined by criticality analysis (typically 50–100 g ¹⁰B per meter of tank height).
- Minimum B₄C packing density: 1.2 g/cm³ (natural B₄C, 78% ¹⁰B by weight).
- Center column must be checked for long-term B₄C degradation / dissolution if any water ingress scenario is postulated.

---

## 2. FDT Thermal Analysis

### Decay Heat Load vs. Time

| Time after shutdown | Decay heat (fraction of operating power) | Heat load (at 8 MWt) |
|--------------------|------------------------------------------|----------------------|
| t = 0 | 7.0% | 560 kW |
| t = 1 min | 4.5% | 360 kW |
| t = 1 h | 1.5% | 120 kW |
| t = 6 h | 0.8% | 64 kW |
| t = 24 h | 0.5% | 40 kW |
| t = 7 days | 0.2% | 16 kW |

### Natural Convection Air Cooling

| Parameter | Value |
|-----------|-------|
| Tank outer surface area | ~7.0 m² |
| Air convection coefficient (h_air, natural) | ~10–15 W/(m²·K) |
| Maximum heat removal (natural convection, ΔT = 400 °C) | ~42–63 kW |
| Supplemental forced-air fans required at t = 0 | Yes — natural convection alone insufficient at t=0 |
| Forced air fans (supplemental) | 2 × 500 W fans per tank; total ~30 kW cooling boost |
| Tank wall temperature (at 24 h, no active cooling) | ~700–750 °C (material limit: <800 °C) |

---

## 3. Pressure Boundary Requirements

### FDT Vessel Design
| Parameter | Value |
|-----------|-------|
| Design pressure | 345 kPa gauge (50 psig) |
| Design temperature | 760 °C (maximum expected) |
| Hastelloy-N allowable stress (760 °C) | ~35 MPa |
| Required wall thickness (outer cylinder) | t = PD/(2S) = (0.345×1219)/(2×35) = 6.0 mm → 9.53 mm provided |
| Radiographic inspection | 100% of all welds |

---

## 4. Overflow Tank (OFT) Specifications

| Parameter | Value |
|-----------|-------|
| Design capacity | 454 L (120 USgal) |
| Tank OD | 610 mm (24 in) |
| Tank height | 762 mm (30 in) |
| Wall thickness | 9.53 mm (0.375 in) |
| Center column OD | 304 mm (12 in) |
| Annular salt thickness | 128 mm (5 in) |
| k-eff (worst case) | <0.95 |
| Heating | Electric trace; same approach as FDT |

---

## 5. Drain Time Analysis

Assuming:
- Drain line: 2-in SCH40, 3 m long, 25 mm/m slope
- Freeze valve FV-101 fully open (no resistance)
- Primary loop salt temperature: 640 °C
- FDT initially empty

| Parameter | Value |
|-----------|-------|
| Salt flow rate under gravity (estimated) | ~6–8 L/s |
| Total fuel salt inventory | ~1,993 L |
| Drain time (estimate) | ~250–330 s (~4–6 minutes) |
| Acceptable drain time (ORNL requirement) | <30 minutes |

Margin is very comfortable; actual MSRE drain time was ~10–15 minutes.

---

## 6. Fill (Return) Procedure

1. Primary loop heat-traced to ≥ 550 °C and pumping.
2. FDT salt at ≥ 480 °C (above liquidus with margin).
3. Open fill line freeze valve FV-103 by applying heater power; allow ~10 min to fully open.
4. Salt returns by gravity from FDT bottom nozzle to primary loop suction.
5. Monitor FDT level (LI-601) dropping and pump bowl level (LI-101) rising.
6. When FDT empty (LI-601 at zero) and pump bowl at normal operating level, close FV-103 by removing heater power.
7. Allow FV-103 to refreeze (~15 min).

---

## 7. Inspection and Testing

| Activity | Frequency |
|----------|----------|
| Visual inspection of tank exterior | After each drain/fill cycle |
| Thermocouple calibration check | Annual |
| Freeze valve open/close functional test | Semi-annual (warm-up test on FV-103; FV-101 cold test only) |
| Criticality safety analysis revalidation | After any change to fissile loading or geometry |
| Wall thickness ultrasonic measurement | Every 5 years |
