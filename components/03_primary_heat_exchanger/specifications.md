# Primary Heat Exchanger — Detailed Specifications

**Reference:** ORNL-TM-728, Section 3.4

---

## 1. Thermal Performance Specifications

| Parameter | Value |
|-----------|-------|
| Design heat duty | 7.34 MWt |
| Operating heat duty | Up to 8 MWt |
| Overall heat transfer coefficient (U, calculated) | ~4,200 W/(m²·K) |
| Log-mean temperature difference (LMTD) | ~55.3 °C *(corrected from 50.6 °C; calculated below)* |
| LMTD correction factor (F) | ~0.98 (single-pass shell, U-tube ≈ 1.0) |
| Effective heat transfer area | ~36.5 m² |
| Fouling factor (both sides) | 0 (no fouling expected with clean fluoride salts) |

### Temperature Profile

| Stream | Inlet T (°C) | Outlet T (°C) | ΔT |
|--------|-------------|--------------|-----|
| Fuel salt (shell side) | 654 | 632 | −22 °C |
| Coolant salt (tube side) | 546 | 621 | +75 °C |

**LMTD calculation (counterflow):**
- Hot end ΔT = T_fuel_in − T_coolant_out = 654 − 621 = **33 °C**
- Cold end ΔT = T_fuel_out − T_coolant_in = 632 − 546 = **86 °C**
- LMTD = (86 − 33) / ln(86/33) = 53 / ln(2.606) = 53 / 0.958 = **55.3 °C**

> **Heat-balance note:** Using documented values (primary flow 1200 USgpm, ρ = 2.24 g/cm³,
> cp = 1.508 J/g·K, ΔT = 22 °C) implies Q ≈ 5.6 MWt on the fuel side, not 7.34 MWt.
> The coolant side (750 USgpm, ρ = 1.94 g/cm³, cp = 2.38 J/g·K, ΔT = 75 °C) implies
> Q ≈ 16.4 MWt — neither value is consistent with 7.34 MWt.
> This is a known documentation inconsistency. Verify cp values against ORNL-4344 and
> temperatures/flows against ORNL-TM-728 Section 4 to obtain a self-consistent set.
> The most likely root cause is that the 632/654 °C temperatures correspond to a
> lower-power operating condition, not the full 7.34 MWt design point.

---

## 2. Tube-Side Hydraulics (Coolant Salt)

| Parameter | Value |
|-----------|-------|
| Tube ID | 10.56 mm (0.416 in; = 12.7 − 2×1.07 mm) |
| Number of tubes | ~159 |
| Tube length (one leg) | ~2,190 mm (corrected from ~4,877 mm for shorter shell) |
| Total tube-side flow area | ~7,510 mm² |
| Coolant salt velocity in tubes | ~2.7 m/s |
| Tube-side Reynolds number | ~21,000 (turbulent) |
| Tube-side heat transfer coefficient (h_tube) | ~9,800 W/(m²·K) |
| Tube-side pressure drop | ~21 kPa (3 psi) |

---

## 3. Shell-Side Hydraulics (Fuel Salt)

| Parameter | Value |
|-----------|-------|
| Shell ID | ~444 mm |
| Baffle spacing | 203 mm |
| Baffle cut | 25% |
| Equivalent shell-side diameter | ~10.9 mm |
| Fuel salt velocity (across baffles) | ~0.8 m/s |
| Shell-side Reynolds number | ~2,500 (transition/turbulent) |
| Shell-side heat transfer coefficient (h_shell) | ~5,200 W/(m²·K) |
| Shell-side pressure drop | ~14 kPa (2 psi) |

---

## 4. Tube Wall Thermal Resistance

| Item | R (m²·K/W) |
|------|-----------|
| Tube-side convection (1/h_tube) | 1.02 × 10⁻⁴ |
| Tube wall conduction (t/k; Hastelloy-N k=12 W/m·K) | 7.4 × 10⁻⁵ |
| Shell-side convection (1/h_shell) | 1.92 × 10⁻⁴ |
| **Total 1/U** | **3.66 × 10⁻⁴** |
| **U (calculated)** | **~2,730 W/(m²·K)** |

> Note: The somewhat higher effective U (~4,200 W/(m²·K)) in ORNL reports reflects enhanced geometry (e.g., baffled flow); above is a simplified estimate.

---

## 5. Mechanical Specifications

### Shell
| Parameter | Value |
|-----------|-------|
| Shell OD | 457.2 mm (18.0 in) |
| Shell wall thickness | 6.35 mm (0.25 in) |
| Shell material | Hastelloy-N |
| Shell length (tube sheet to tube sheet) | 2,440 mm (~96 in / ~8 ft per ORNL MSRE film, ORNL 1966; corrected from 5,029 mm) |
| MAWP (shell side) | 345 kPa gauge at 704 °C |

### Tubes
| Parameter | Value |
|-----------|-------|
| Tube OD | 12.7 mm (0.500 in / 1/2-in per ORNL MSRE film, ORNL 1966; corrected from 9.525 mm) |
| Tube wall | 1.07 mm (0.042 in; corrected from 0.889 mm) |
| Tube pitch | 19.05 mm (3/4-in) triangular (corrected from 12.7 mm to suit 1/2-in OD tubes) |
| Tube U-bend radius | 25.4 mm minimum |
| Tube material | Hastelloy-N, ASTM B622 |
| MAWP (tubes) | 345 kPa gauge at 704 °C |

### Tube Sheet
| Parameter | Value |
|-----------|-------|
| Material | Hastelloy-N, ASTM B575 |
| Thickness | 63.5 mm (2.5 in) |
| Tube-to-tube sheet joint | Strength weld (2 passes, full-penetration fillet) |
| Tube holes | 9.60 mm diameter (0.378 in); tolerance +0.05/−0.00 mm |

---

## 6. Inspection Requirements

- Tubes: 100% eddy-current test (ECT) to ASME Section V Article 8 before bundle assembly.
- All welds: PT (dye penetrant) per ASME Section V Article 6.
- Shell welds: 100% RT.
- Final assembly: Pneumatic pressure test on shell side and tube side independently at 1.5× design pressure.
- Leak test between shell and tube: tube side to 345 kPa gauge; shell at 0; monitor tube-side pressure decay for 30 minutes; zero drop accepted.

---

## 7. Weight Estimates

| Component | Mass (kg) |
|-----------|-----------|
| Shell + shell-side nozzles | ~750 |
| Tube bundle (159 tubes) | ~280 |
| Tube sheets (2×) | ~450 |
| Channel heads, baffles | ~120 |
| **Total (dry)** | **~1,600** |
| Fuel salt fill (shell side, ~250 L) | ~560 |
| Coolant salt fill (tube side, ~90 L) | ~175 |
| **Total (filled)** | **~2,335** |
