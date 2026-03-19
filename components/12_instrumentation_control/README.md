# Component 12: Instrumentation and Control System

## Overview

The MSRE instrumentation and control (I&C) system encompasses all sensors, signal processing, display, recording, and control equipment required to safely operate the reactor. It is divided into two subsystems:
1. **Nuclear Instrumentation** — measures neutron flux over a wide range for reactor power control.
2. **Process Instrumentation** — measures temperature, flow, level, pressure, and other process parameters.

**Primary Reference:** ORNL-3832 (nuclear and process instrumentation); ORNL-TM-0729 (electrical and mechanical instrumentation)

---

## 1. Nuclear Instrumentation

### Function
- Measures reactor neutron flux from subcritical (source level) to full power (8 MWt).
- Provides signals for automatic control, safety trips (SCRAM), and operator display.
- Coverage range: ~10 decades (10⁻⁴ to 10⁶ W equivalent power level).

### Neutron Flux Channels

| Channel | Type | Range | Function |
|---------|------|-------|---------|
| Start-up range (SUR-1, SUR-2) | ³He or BF₃ proportional counter | 10⁻⁴ to 10 W | Startup, approach to criticality |
| Intermediate range (IR-1, IR-2) | Compensated ion chamber (CIC) | 10⁻¹ to 10⁴ W | Bridging range |
| Power range (PR-1, PR-2) | Uncompensated ion chamber (UIC) | 10² to 10⁷ W | Normal operation and SCRAM |
| Safety channel (SAF-1) | Fission chamber | 10⁻² to 10⁵ W | Independent SCRAM channel |

### Detector Locations
- Detectors are located in dry wells (Hastelloy-N tubes) in the reactor cell shield wall, adjacent to the reactor vessel.
- Dry wells allow detector insertion/removal without cell entry.
- Each channel has a primary and backup detector.
- Detector cables route through cell wall penetrations via MI (mineral-insulated) cable.

### Neutron Detector Specifications

| Parameter | Startup Range | Power Range |
|-----------|--------------|-------------|
| Detector type | BF₃ proportional counter | Uncompensated ion chamber |
| Active length | 300 mm (12 in) | 400 mm (16 in) |
| Detector OD | 19 mm (0.75 in) | 38 mm (1.5 in) |
| Operating voltage | +300 to +600 V DC | +50 to +200 V DC |
| Temperature (detector location) | <65 °C | <65 °C |
| Manufacturer (MSRE era) | ORNL custom / Nuclear Chicago | Victoreen / ORNL custom |

### Nuclear Instrument System (NIS)

| Function | Signal | Trip Setpoint |
|----------|--------|--------------|
| High neutron flux SCRAM | Power range | >110% of full power |
| High flux rate (short period) | Period channel | <3 second doubling time |
| Low-low startup count rate | Startup range | <100 counts/second (interlock) |
| Power level indication | Power range | 0–110% full power (4-20 mA) |
| Power level recorder | Power range | Chart recorder, 24 h chart |

---

## 2. Temperature Instrumentation

### Thermocouple Types
- **All salt-wetted and high-temperature locations:** Type K (NiCr/NiAl), Inconel-sheathed, mineral-insulated.
- **Below 300 °C:** Type K or Type E acceptable.
- **Reference junction:** Electronic cold-junction compensation at terminal head.

### Temperature Points Summary

| Location | Count | Purpose |
|----------|-------|---------|
| Core inlet (primary loop) | 4 | Fuel temperature entering core |
| Core outlet (primary loop) | 6 | Fuel temperature leaving core |
| Heat exchanger (fuel side) | 4 | Fuel temperature in/out HX |
| Heat exchanger (coolant side) | 4 | Coolant temp in/out HX |
| Primary pump bowl | 3 | Salt temp in pump |
| Coolant loop piping | 6 | System temperatures |
| Radiator inlet/outlet | 4 | Coolant and air temperatures |
| Drain tanks (FDT + OFT) | 10 | Drain tank wall temperatures |
| Freeze valve sections | 10 | One per freeze valve × 2 redundant |
| Reactor vessel exterior | 4 | Vessel temperature profile |
| Graphite core (in-core TC) | 3 | Core moderator temperatures |
| **Total primary TCs** | **~58** | — |

### Thermocouple Specifications

| Parameter | Value |
|-----------|-------|
| Type | K (Chromel/Alumel) |
| Sheath OD | 3.2 mm or 6.35 mm |
| Sheath material | Inconel 600 (inside cell); SS316 (outside cell) |
| Insulation | MgO (mineral insulation) |
| Length | 300–600 mm (varies by location) |
| Accuracy | Class 1 per IEC 60584: ±1.5 °C or 0.4%, whichever is greater |
| Max temperature | 1260 °C (1.25× normal operating) |
| Cable extension | Matched TC extension wire to control room |

---

## 3. Flow Instrumentation

### Primary Loop Flow (Fuel Salt)
- **Type:** Electromagnetic (magnetic) flowmeter (no moving parts; non-invasive)
- **Principle:** AC-excited coils generate magnetic field across pipe; salt (electrolyte) flowing through field generates EMF proportional to velocity.
- **Tag:** FI-101
- **Range:** 0–120% design flow (0–1440 USgpm)
- **Accuracy:** ±2% of full scale
- **Material (wetted):** Hastelloy-N flow tube; ceramic-coated electrodes
- **Location:** Primary loop return pipe (HX outlet to vessel inlet)

### Coolant Loop Flow (Coolant Salt)
- **Type:** Electromagnetic flowmeter
- **Tag:** FI-201
- **Range:** 0–1000 USgpm
- **Accuracy:** ±2% FS

### Off-Gas Flow
- **Type:** Mass flow controller (thermal mass flow)
- **Tag:** FI-301 (He sparge)
- **Range:** 0–2 L/min
- **Accuracy:** ±1% FS

---

## 4. Level Instrumentation

### Pump Bowl Salt Level (FI-101)
- **Type:** Differential pressure (dP cell) measuring gas-space pressure vs. salt-column pressure.
- **Transmitter:** Force-balance dP cell; range 0–250 mm H₂O; 4-20 mA output.
- **Salt density correction:** Level calculated from dP and salt density at measured temperature.
- Additionally: Gamma densitometer (external to bowl) provides independent level check.

### Drain Tank Level
- **Type:** dP cell; same design as pump bowl level.

---

## 5. Pressure Instrumentation

| Tag | Location | Range | Type |
|-----|----------|-------|------|
| PI-101 | Primary loop pump discharge | 0–500 kPa | Flush-diaphragm dP transmitter; Hastelloy-N wetted |
| PI-201 | Coolant loop pump discharge | 0–500 kPa | Same |
| PI-301 | Off-gas line | 0–50 kPa gauge | SS Bourdon tube transmitter |
| PI-601 | FDT headspace | 0–50 kPa gauge | SS transmitter |

---

## 6. Control System Architecture

### Process Control
- **Type:** Analog hardwired control (MSRE era) — replicate with modern DCS if rebuilding.
- **Recommended modern equivalent:** Safety-qualified DCS (e.g., Emerson DeltaV SIS, Rockwell Allen-Bradley ControlLogix with SIL-2 qualification).
- **Analog loops:** Temperature controllers for heat trace setpoints (PID, 4-20 mA output).
- **Flow control:** No flow control valves — pump speed is fixed; flow is not controlled.

### Safety System (Hardwired Relay Logic)
- **Independent of process control** — separate relay panel.
- **Inputs:** High flux, high rate, low flow, manual SCRAM pushbutton.
- **Outputs:** Safety rod drop relay; pump coast-down relay; freeze valve heater cutoff relay.
- **Power supply:** UPS-backed 24 V DC (>1 hour backup).

### Operator Interface
- Mimic panel showing simplified plant diagram with analog meters.
- Chart recorders for key parameters (power, temperatures, flows).
- Alarm annunciator panel (individual lights for each alarm condition).
- Modern replacement: industrial HMI screens with historian and alarm management.

---

## 7. Calibration Requirements

| Instrument | Calibration Interval | Reference Standard |
|------------|---------------------|-------------------|
| Thermocouples | Replace every 2 years or on drift indication | NIST-traceable reference TC |
| Flux detectors | Annual gain/sensitivity check | NIST-traceable ionization standard |
| Flow transmitters | Annual; in-situ zero/span check | Calibrated flow reference |
| Pressure transmitters | Semi-annual; zero/span check | Calibrated pressure reference |
| Control logic relays | Annual functional test (trip actuation test) | Test procedure with acceptance criteria |
