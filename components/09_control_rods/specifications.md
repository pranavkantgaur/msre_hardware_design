# Control Rod System — Detailed Specifications

**Reference:** ORNL-TM-728, Section 3.11; ORNL-TM-1490; ORNL-3679 (nuclear analysis)

---

## 1. Neutron Absorber Pellet Specifications

### Composition
| Component | Weight % | Purpose |
|-----------|---------|---------|
| Gd₂O₃ | 50% | Primary neutron absorber (¹⁵⁷Gd σ_th = 255,000 barns) |
| Al₂O₃ | 50% | Diluent; ceramic binder; controls reactivity worth per unit length |

### Pellet Physical Properties
| Property | Value |
|----------|-------|
| Pellet diameter | 23.6 mm (0.928 in) |
| Pellet height | 12.7 mm (0.5 in) |
| Sintered density | ≥4.5 g/cm³ (>90% theoretical density) |
| Porosity | <10% |
| Diametral clearance in tube | ~0.8 mm per side |
| Stack length (1422 mm active) | ~112 pellets per rod |

### Sintering Process
1. Mix Gd₂O₃ and Al₂O₃ powders (purity >99.5%) to correct weight ratio.
2. Ball mill to median particle size <5 µm.
3. Add ~2 wt% polyvinyl alcohol binder; granulate.
4. Press in die at ~70 MPa uniaxial; green density ~55% theoretical.
5. Burn off binder at 500 °C in air; 2 h hold.
6. Sinter at 1600 °C in air; 4 h hold; cool at <200 °C/h.
7. Inspect: dimensional check; density by Archimedes method; visual for cracks.

---

## 2. Absorber Tube (Clad) Specifications

| Parameter | Value |
|-----------|-------|
| Clad material | Inconel 625 (UNS N06625) |
| Clad OD | 25.4 mm (1.000 in) ± 0.05 mm |
| Clad wall thickness | 1.65 mm (0.065 in) |
| Clad ID | 22.1 mm (0.870 in) |
| Active length | 1,422 mm (56.0 in) |
| Total length (including end caps) | 1,448 mm (57.0 in) |
| End cap material | Inconel 625 |
| End cap thickness | 3.18 mm (0.125 in) |
| End cap weld | TIG full-penetration; 100% dye penetrant + He leak test |
| He leak test acceptance | <1 × 10⁻⁹ cm³/s at ambient |
| Tube straightness | ≤0.5 mm in full length |

---

## 3. Drive Mechanism Specifications

### Regulating Rod Drive

| Parameter | Value |
|-----------|-------|
| Type | Rack and pinion; electric motor drive |
| Travel range | 0 to 508 mm (0 to 20 in) |
| Drive speed (max) | 2.5 mm/s (0.1 in/s) |
| Drive speed (min) | 0.1 mm/s (0.004 in/s) — adjustable |
| Motor | DC servo or stepper; 24 V; 50 W |
| Gear ratio | Chosen to provide above speed range |
| Backlash | ≤0.5 mm |
| Position encoder | Potentiometer or encoder; resolution ≤0.1 mm |
| Position repeatability | ±0.2 mm |
| Limit switches | Hard stops at 0 mm and 508 mm travel |

### Safety Rod Drive

| Parameter | Value |
|-----------|-------|
| Type | Solenoid electromagnetic latch |
| Hold force | ≥2× rod weight (~30 N) |
| Solenoid voltage | 24 V DC |
| Solenoid power (holding) | ~10 W |
| Drop time (free fall from 508 mm) | 0.32 s (free fall only) + ~0.3 s friction = ~0.6 s total |
| Specification requirement | <1.0 s from de-energize to full insertion |
| Reset mechanism | DC motor-driven cable winch; 24 V; 50 W |
| Re-latch hold | Solenoid re-energized; rod held up for next operation |

---

## 4. Rod Worth Measurements (MSRE Actual Values, Reference)

| Rod | Condition | Measured Worth (% Δk/k) |
|-----|-----------|------------------------|
| Regulating rod #1 | Full travel (0→508 mm) | 0.348 |
| Regulating rod #2 | Full travel (0→508 mm) | 0.345 |
| Safety rod #3 | Full travel (0→508 mm) | 1.248 |
| All rods in | — | ~1.941 |

> Source: ORNL-4119, Table 3.3 (approximate values; exact values from MSRE measured rod worth calibration)

---

## 5. Drive Housing (Vessel Penetration Seal) Specifications

| Parameter | Value |
|-----------|-------|
| Material | Hastelloy-N |
| Drive housing OD | 73 mm (2.875 in) |
| Drive shaft diameter (in housing) | 19.05 mm (0.75 in) |
| Sealing method | Lip seal + He purge labyrinth; no O-ring in salt service |
| He purge pressure | 5 kPa above primary loop pressure |
| He purge flow | 0.2 L/min per drive |
| Temperature at seal | ~200 °C (thermal gradient along shaft) |
| Bolted mounting | 4 × M16 Hastelloy-N studs to vessel nozzle flange |

---

## 6. Reactivity Control Strategy

### Normal Operation
- Regulating rods 1 and 2 are used for:
  - Startup (withdraw from full in to achieve criticality)
  - Power control (partial insertion for setpoint control)
  - Load following (adjust rod position to maintain constant temperature)
- Safety rod 3 is maintained fully withdrawn during normal operation (held by solenoid).

### Automatic Control
- Reactor power controlled by core outlet temperature (TI-102) feedback.
- Setpoint: 654 °C core outlet temperature.
- Control rod drive speed: proportional to temperature error.
- No flow control — temperature maintained by reactivity alone.

### Shutdown Rod Worth Requirement
- Must maintain k-eff < 0.99 at hot zero power with all rods inserted.
- Must maintain k-eff < 0.98 at cold conditions with all rods inserted.
- Total rod worth of ~1.95% Δk/k provides sufficient shutdown margin for all conditions.
