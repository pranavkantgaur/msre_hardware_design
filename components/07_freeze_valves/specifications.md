# Freeze Valve — Detailed Specifications

**Reference:** ORNL-TM-728, Section 3.9; ORNL-TM-1647 (safety analysis)

---

## 1. Thermal Analysis — Freeze / Thaw Cycle

### Salt Properties (Fuel Salt at Freeze Valve)

| Property | Value |
|----------|-------|
| Liquidus temperature (fuel salt) | ~450 °C |
| Solidus temperature | ~434 °C |
| Heat of fusion | ~490 kJ/kg |
| Thermal conductivity (liquid) | ~1.0 W/(m·K) |
| Thermal conductivity (solid) | ~1.5 W/(m·K) |
| Density (liquid at 460 °C) | ~2.28 g/cm³ |

### FV-101 (Drain Valve) — Thaw Time Analysis

| Condition | Parameters |
|-----------|-----------|
| Initial plug temperature | 380 °C (heaters maintaining frozen state) |
| Heat source after power loss | Decay heat conducted from adjacent piping: ~300 W |
| Mass of salt plug | ~0.8 kg (2-in SCH40 pipe, 152 mm frozen length) |
| Energy to thaw (sensible + latent) | ~400 kJ |
| Thaw time estimate | ~22 min (without active heater — acceptable) |
| Thaw time with emergency heater (300 W auxiliary) | ~8 min |

> Note: ORNL required <30 min drain initiation time. 22 min by passive decay heat alone satisfies this.

### FV-103 (Fill Valve) — Freeze Time Analysis

| Condition | Parameters |
|-----------|-----------|
| Initial plug temperature | 530 °C (fully melted / valve open) |
| Cooling source | 10 L/min instrument air at 25 °C impinging on freeze section |
| Heat removal rate | ~200 W (air jet, forced convection) |
| Time to freeze | ~20 min |

---

## 2. Heater Design Details

### FV-101 Heater (Type A — maintains CLOSED state)

| Parameter | Value |
|-----------|-------|
| Function | Keep plug frozen; de-energize to open (drain) |
| Heater type | NiCr resistance wire, 18 AWG (1.6 Ω/m) |
| Total heater resistance | 29 Ω |
| Voltage | 120 V AC |
| Power | ~500 W |
| Surface heat flux | ~3.5 W/cm² (adequate to maintain plug at 380 °C against decay heat) |
| Number of zones | 2 (primary + backup) |
| Primary power | Normal AC; energized to keep valve closed |
| Backup power | UPS-backed AC; same circuit |
| Trip condition | De-energize on loss of AC; de-energize on SCRAM signal |

### FV-103 Heater (Type B — opens only when energized)

| Parameter | Value |
|-----------|-------|
| Function | Melt plug to allow fill; de-energize to close (freeze) |
| Heater type | NiCr resistance wire, 18 AWG |
| Total heater resistance | 29 Ω |
| Voltage | 120 V AC |
| Power | ~500 W |
| Normal state | De-energized (valve frozen/closed) |
| Open condition | Heater energized; plug melts in ~10 min |
| Close condition | Heater de-energized; air jet applied; plug freezes in ~20 min |

### FV-104 Heater (Type A — secondary drain isolation, in series with FV-101)

| Parameter | Value |
|-----------|-------|
| Function | Second passive drain isolation valve in series with FV-101; provides defence-in-depth for passive drain actuation |
| Location | Drain line between reactor vessel lower nozzle and FV-101 (~300 mm upstream of FV-101) |
| Normal state | De-energized (valve frozen/closed) — both FV-101 and FV-104 must thaw to allow drain |
| Heater type | NiCr resistance wire, 18 AWG; same design as FV-101 |
| Total heater resistance | 29 Ω |
| Voltage | 120 V AC |
| Power | ~500 W |
| Trip condition | De-energize on loss of AC; de-energize on SCRAM signal (same interlock as FV-101) |
| Thaw time (passive only) | ~22 min (same thermal analysis as FV-101) |

> **Safety rationale:** Having two freeze valves in series (FV-104 → FV-101) on the drain line
> ensures that a single passive valve failure (stuck frozen due to local cold spot or heater
> malfunction) does not prevent drainage. Both valves de-energize simultaneously on SCRAM,
> so both must fail-frozen to prevent drainage — probability ≪ 10⁻⁴ per demand.

---

## 3. Freeze Section Material and Geometry

| Parameter | Value |
|-----------|-------|
| Tube material | Hastelloy-N, UNS N10003 |
| Tube OD (drain line valves) | 60.3 mm (2.375 in) — 2-in SCH40 |
| Tube wall | 3.91 mm (0.154 in) |
| Frozen section length | 152 mm (6.0 in) |
| Section roughness (exterior) | Mill finish (no special finish needed) |
| Heater wire spacing | ~3 mm pitch (wound helically on exterior) |
| Refractory cement thickness (over wire) | 6.35 mm (0.25 in) |
| Thermocouple (Type N) | 2 per valve; Hastelloy-N sheath; welded to exterior between heater wire turns |
| TC replacement interval | 18 months or on drift >10 °C — whichever comes first |
| Air nozzle position | Mid-freeze-section; tangential impingement |
| Distance to nearest insulation | 25 mm (0.984 in) minimum clearance at each end |

---

## 4. Performance Testing Protocol

Before installation, each freeze valve shall be tested per the following protocol:

1. **Bench test (ambient conditions with Wood's metal):** Use Wood's metal (Bi-Pb-Sn alloy; melting point ~70 °C) as surrogate for salt. Verify heater can maintain plug and air jet can refreeze.
2. **Heater resistance check:** Measure resistance; verify within ±5% of design.
3. **Thermocouple calibration:** Verify TC reads within ±5 °C at 100 °C reference.
4. **10 cycle test:** Perform 10 freeze/thaw cycles; verify no heater failures, no cracking of refractory cement.
5. **High-temperature qualification (one valve per design per batch):** Test at 650 °C salt temperature (if hot test rig available); verify performance within specification.

---

## 5. Maintenance Guidelines

- **Inspection interval:** Every scheduled outage (every 2–3 years of operation).
- **Checks:** Visual inspection of heater leads for cracking; thermocouple continuity; cooling air nozzle free of blockage.
- **Replacement criteria:** Replace if heater resistance deviates >10% from initial value or if thermocouple fails.
- **Replacement approach:** Freeze valve section is flanged at both ends; remove spool piece with remote tooling; install new spool piece.
