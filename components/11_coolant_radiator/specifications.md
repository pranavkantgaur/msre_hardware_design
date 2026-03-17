# Coolant Radiator — Detailed Specifications

**Reference:** ORNL-TM-728, Section 3.7

---

## 1. Thermal Performance

### Heat Duty Verification

LMTD method:
- Hot end ΔT = Coolant in (621 °C) − Air out (≈315 °C) = 306 °C (estimated; depends on air flow)
- Cold end ΔT = Coolant out (546 °C) − Air in (38 °C) = 508 °C
- LMTD = (508 − 306) / ln(508/306) = 202 / 0.508 ≈ 397.6 °C (used as ~398 °C)

Overall heat transfer coefficient U (estimated for forced-air, finned-tube):
- U ≈ 40–60 W/(m²·K) referred to bare tube area (typical for air coolers)
- U ≈ 5–8 W/(m²·K) referred to finned area

Using U = 7 W/(m²·K) (referred to finned area) × 2,800 m² × 398 °C LMTD:
- Q = 7 × 2,800 × 398 = **7.81 MWt** (meets 7.34 MWt design duty ✓)

---

## 2. Tube-Side (Coolant Salt) Specifications

| Parameter | Value |
|-----------|-------|
| Tube material | Hastelloy-N, ASTM B622 |
| Tube OD | 25.4 mm (1.0 in) |
| Tube wall | 1.65 mm (0.065 in) |
| Tube ID | 22.1 mm (0.870 in) |
| Coolant flow area (per tube) | 383 mm² |
| Total tubes | 144 |
| Total flow area | ~55,200 mm² |
| Coolant salt velocity | 47.3 L/s ÷ 55,200 mm² = **0.86 m/s** |
| Reynolds number | Re = ρvD/µ = 1940×0.86×0.0221/0.006 = **6,130** (turbulent) |
| Tube-side h (coolant salt) | ~2,000 W/(m²·K) |
| Tube-side ΔP (4 passes × 6.1 m) | ~25 kPa (3.6 psi) |
| MAWP (tube side) | 345 kPa gauge at 650 °C |

---

## 3. Fin Specifications

| Parameter | Value |
|-----------|-------|
| Fin type | Wound spiral (L-foot or knurled embedded) |
| Fin material | Hastelloy-N, ASTM B622 strip |
| Fin height | 12.7 mm (0.5 in) |
| Fin thickness | 0.889 mm (0.035 in) |
| Fin pitch | 4 fins/cm (10 fins/in) |
| Fin OD | 25.4 + 2(12.7) = 50.8 mm (2.0 in) |
| Fins per tube | ~2,440 fins (at 4/cm × 610 cm active) |
| Fin attachment | High-frequency resistance weld to tube |
| Fin-to-tube contact resistance | <0.002 m²·K/W (weld quality requirement) |
| Fin efficiency (at 400 °C ΔT) | ~0.85 |

---

## 4. Air-Side Specifications

| Parameter | Value |
|-----------|-------|
| Total air flow | 70.8 m³/s (150,000 cfm) |
| Air-side face area | 70.8 / 3.5 m/s face velocity = ~20.2 m² |
| Face dimensions (approx.) | ~6 m wide × ~3.4 m tall |
| Tube bundle depth (direction of air flow) | ~0.45 m (one row of 50.8 mm finned OD tubes) |
| Air pressure drop | ~125 Pa (0.5 in H₂O) |
| Air-side h (forced convection, finned) | ~60 W/(m²·K) (referred to bare tube area) |
| Fan power | 4 × 30 kW = 120 kW (two fans operating normally; two standby) |

---

## 5. Header Specifications

| Parameter | Value |
|-----------|-------|
| Material | Hastelloy-N |
| Design | Box header (rectangular cross-section) |
| Header ID (cross-section) | 200 mm × 200 mm |
| Header wall thickness | 9.53 mm (0.375 in) |
| Number of headers | 2 main + 3 inter-pass = 5 total |
| Tube-to-header joint | Full-penetration butt or fillet weld; 100% PT |
| Inlet/outlet nozzle size | 3-in SCH40 (88.9 mm OD) |

---

## 6. Support Structure

| Parameter | Value |
|-----------|-------|
| Tube bundle support | Hastelloy-N tube support sheets every 1,000 mm |
| Tube support sheet material | Hastelloy-N, 6.35 mm |
| Tube hole diameter in support | 51.2 mm (0.2 mm clearance over fin OD) |
| Main structural frame | Carbon steel I-beam, hot-dip galvanized |
| Thermal expansion provision | Tube bundle floats on one end; fixed on inlet-header end |
| Axial expansion (design) | ~50 mm at 600 °C Δ from ambient; provided by sliding support |

---

## 7. Decay Heat Removal Capability

| Time after shutdown | Decay heat | Required cooling | Available (2 fans) | Available (natural convection) |
|--------------------|-----------|-----------------|-------------------|-------------------------------|
| t = 0 | 560 kW | 560 kW | ~1,500 kW ✓ | ~50 kW ✗ |
| t = 1 h | 120 kW | 120 kW | 300 kW ✓ | ~50 kW ✗ |
| t = 24 h | 40 kW | 40 kW | 300 kW ✓ | ~50 kW ✓ |
| t = 7 days | 16 kW | 16 kW | — | ~50 kW ✓ |

- Active fan cooling required for first ~12–24 h after shutdown.
- After ~24 h, natural convection through the radiator bundle (with fans off) is sufficient.
- Emergency fan power: each fan on separate circuit; at least one circuit on emergency generator.
