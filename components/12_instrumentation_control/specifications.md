# Instrumentation and Control — Detailed Specifications

**Reference:** ORNL-3832; ORNL-TM-0729

---

## 1. Nuclear Instrumentation System (NIS) — Detailed

### Coverage Channels

| Channel | Detector | Principle | Range (counts or watts) | Location |
|---------|----------|-----------|-------------------------|---------|
| SUR-1, SUR-2, SUR-3 | BF₃ proportional counter | Neutron (α) counting | 1 – 10⁶ counts/s | Dry well, shield wall (3 channels for 2oo3 startup trip) |
| IR-1, IR-2 | Compensated ion chamber | Ionization current, gamma-compensated | 0.01 – 10⁴ W | Dry well, shield wall |
| PR-1, PR-2 | Uncompensated ion chamber | Ionization current | 100 – 1.5×10⁷ W | Dry well, closer to vessel |
| SAF-1 | Fission chamber | Fission fragment counting | 0.01 – 10⁵ W | Separate dry well (independent) |

### Channel Signal Processing

| Processing Function | Hardware |
|--------------------|----------|
| High-voltage power supply | +200 V to +900 V; regulated ±0.1%; separate per channel |
| Preamplifier (startup/intermediate) | Charge-sensitive; input at detector; output mV pulses |
| Log amplifier (all ranges) | Decade log amplifier; 8-decade range per module |
| Period circuit | Reactor period (seconds) = 1/(d(ln ϕ)/dt); alarm at <5 s; SCRAM at <3 s |
| Flux rate meter | First derivative of log flux; outputs in %/s |
| Output signal | 4–20 mA (0–110% full power for power range) |

### Detector Dry Well Dimensions

| Parameter | Value |
|-----------|-------|
| Dry well tube material | Hastelloy-N |
| Dry well tube OD | 50.8 mm (2.0 in) |
| Dry well tube wall | 3.18 mm (0.125 in) |
| Dry well length | 1,000 mm (into shield wall) |
| Sealed lower end | Welded Hastelloy-N cap |
| Upper end | Open to detector insertion from outside cell wall |
| Shielding gap-fill | Lead poured around dry well in concrete |
| Number of dry wells | 8 (2 per flux range channel) |

---

## 2. Thermocouple Loop Design

### Signal Chain

```
Type K TC (Inconel sheath, MgO insulation)
    → TC extension wire (matched alloy; MI cable inside cell)
        → Cell wall penetration (multi-pin sealed connector)
            → TC extension wire (standard; to control room)
                → Terminal block
                    → Transmitter (with cold-junction compensation)
                        → 4–20 mA to DCS / panel meter
```

### Transmitter Specifications
| Parameter | Value |
|-----------|-------|
| Type | Two-wire; 24 V DC loop powered |
| Input | Type K thermocouple, 0–1250 °C |
| Output | 4–20 mA (0–1250 °C range) |
| Accuracy | ±1.5 °C ± 0.15% of span |
| Cold-junction compensation | Electronic; 0–60 °C ambient |
| Isolation | 1,500 V AC (galvanic isolation) |
| Housing | DIN rail mount; IP20 |
| Examples | Endress+Hauser iTEMP TMT162 or equivalent |

---

## 3. Electromagnetic Flowmeter — Fuel Salt (FI-101)

| Parameter | Value |
|-----------|-------|
| Manufacturer (MSRE era) | Fisher & Porter / ORNL custom |
| Principle | Faraday induction (AC-excited, 60 Hz) |
| Pipe ID | 102.3 mm (4.03 in — 4-in SCH40 ID) |
| Flow tube material | Hastelloy-N |
| Electrode material | Hastelloy-N or Pt-10%Rh (radiation-resistant) |
| Electrode insulation | Ceramic (Al₂O₃) or fused silica sleeve |
| Excitation coils | Copper; air-cooled; external to flow tube |
| Signal (generated EMF) | ~0.1–5 mV full scale |
| Signal amplifier | High-impedance; located outside reactor cell |
| Output | 4–20 mA (0–100% flow) |
| Accuracy | ±2% of full scale |
| Max fluid temperature | 750 °C |
| Max fluid pressure | 700 kPa |
| Installation | Flanged spool piece in primary loop pipe |
| Straight run required | ≥10D upstream, ≥5D downstream |

---

## 4. Safety System Design Requirements

### Independence Requirements
- Safety system is fully independent from normal control system (separate panels, power supplies, and signal paths).
- No shared signal cards or shared power supplies between safety system and process control.
- Safety functions shall be operable on loss of all normal AC power (UPS-backed 24 V DC).

### Single Failure Criterion
- Any single component failure (sensor, signal cable, relay) shall not prevent the safety function from operating.
- Implemented via:
  - **2-out-of-3 (2oo3) logic** for SCRAM parameters where 3 independent channels exist
    (startup flux SUR-1/2/3; power range PR when upgraded to 3 channels).
  - **1-out-of-2 (1oo2) logic** for parameters where only 2 channels currently exist
    (IR-1/2, flow FI-101/manual backup, level), pending upgrade to 3 channels.
  - The specific trip voting logic for each parameter is defined in the safety relay panel
    design specification (IC-020) and shall not be "configurable" — it is fixed in hardware.
  - MSRE original design used 1oo2 for most SCRAM functions; this design retains 1oo2 for
    2-channel parameters and applies 2oo3 where 3 channels now exist.

### SCRAM Reset Requirements
- SCRAM can only be reset manually (no automatic reset).
- Reset requires:
  1. Identify and correct cause of SCRAM.
  2. Verify all flux channels below reset permissive level.
  3. Manual reset pushbutton actuation.

---

## 5. Control Room Layout

| Zone | Equipment |
|------|-----------|
| Nuclear panel | Flux level meters; period meters; NIS alarms; control rod position indicators |
| Temperature panel | 58× temperature indicators (4× selector switches for display); 4× chart recorders |
| Flow/pressure panel | FI-101, FI-201 flow indicators; pump speed/status; pressure indicators |
| Drain/freeze valve panel | Freeze valve status lights (frozen/thawed); heater on/off switches; drain tank level |
| Alarm annunciator | 48-point alarm panel; visible and audible; alarm acknowledge and reset |
| Control rod console | Rod position indicators; auto/manual control; setpoint control |
| Interlock/status | Cell atmosphere (O₂, moisture, pressure); pump status; power distribution |

---

## 6. Calibration Intervals Summary

| Instrument Type | Calibration Interval |
|----------------|---------------------|
| Type K thermocouples | Replace or in-situ check every 24 months |
| Flux detectors (NIS) | Sensitivity verification every 12 months |
| Electromagnetic flowmeters | In-situ zero/span check every 12 months |
| Level transmitters (dP) | Zero/span check every 6 months |
| Pressure transmitters | Zero/span check every 6 months |
| SCRAM logic (relay) | Full trip test every 6 months |
| He sparge mass flow controller | Calibration every 12 months with NIST-traceable standard |
| Type N thermocouples (salt-adjacent; IC-007) | Replace every 18 months or on drift >5 °C |
| Type K thermocouples (non-salt-contact; IC-008) | Replace or in-situ check every 36 months |
| Tritium-in-air monitors (IC-025) | Calibration every 6 months with certified standard; source check monthly |
| Tritiated water monitor (IC-026) | Calibration every 6 months |
| Stack tritium monitor (IC-027) | Calibration every 3 months; certified by regulatory-approved laboratory |

---

## 7. Tritium Monitoring System

Tritium monitoring is required for regulatory compliance and operational safety. Three monitoring
channels cover the complete tritium pathway from source to environment.

### 7.1 Tritium Monitoring Points

| Tag | Location | Type | Purpose |
|-----|----------|------|---------|
| IC-025A | Off-gas system (post-HEPA filter, pre-stack) | Ionisation chamber | Measures tritium release rate; primary regulatory compliance channel |
| IC-025B | Building ventilation exhaust | Ionisation chamber | Detects tritium in building atmosphere; operator safety |
| IC-026 | Coolant salt system sample port | Liquid scintillation | Detects tritium permeation through primary heat exchanger (early HX tube failure warning) |
| IC-027 | Stack exhaust point | Ionisation chamber + data logger | Legally binding annual release measurement; retained 5 years |

### 7.2 Alarm Logic for Tritium

| Channel | Pre-alarm (alert) | High alarm (action) | SCRAM |
|---------|-----------------|---------------------|-------|
| IC-025A off-gas | 10 µCi/m³ | 100 µCi/m³ | No (off-gas system — not a direct core safety parameter) |
| IC-025B building ventilation | 1 µCi/m³ | 10 µCi/m³ | No; evacuate building |
| IC-026 coolant system | 0.01 µCi/mL | 0.1 µCi/mL | Alarm to operator; manual SCRAM if rising trend |
| IC-027 stack | Integrated release >5 Ci/month | Integrated >20 Ci/month | Notify regulator; reduce power |

### 7.3 Integration with Off-Gas System

All tritium monitoring channels interface with the Off-Gas system tritium control train
(OGS-014 catalytic oxidizer, OGS-015 desiccant bed) described in Component 08 specifications.
The IC-025A monitor downstream of OGS-015 serves as both a breakthrough detector for the
desiccant bed and the primary regulatory compliance measurement channel.
