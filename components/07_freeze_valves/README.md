# Component 07: Freeze Valves

## Overview

Freeze valves are the primary flow-control device in the MSRE for radioactive salt lines. They contain no moving mechanical parts in contact with the salt. Flow control is achieved by freezing (solidifying) a plug of salt in a section of piping using active cooling, or allowing the plug to melt (open) using electric heaters or passive decay heat.

**Primary Reference:** ORNL-TM-728, Section 3.9; ORNL-TM-1647

---

## Operating Principle

```
CLOSED (Frozen) State:
  Salt flow line → [Cooled section] → salt solidifies → ZERO flow

OPEN (Thawed) State:
  Electric heater energized → salt plug melts → salt flows freely
```

### Key Properties
- **No mechanical seals, no packing, no stem, no actuator** — the solid salt plug IS the valve seat.
- **Fail-safe for drain:** If power is lost, drain valve FV-101 heaters turn off → decay heat melts plug → fuel drains to FDT (passive safety).
- **Fail-closed for isolation:** Non-drain isolation freeze valves default to CLOSED (frozen) on power loss.
- **Salt compatibility:** Any salt can be used as the freezing medium (fuel or coolant salt plug).
- **Leakage:** Zero leakage when frozen (solid metal plug); full flow when open.

---

## Design Types

### Type A: Drain Freeze Valve (Fail-Open — Safety Valve)
Used on: Drain lines (FV-101, fuel loop to FDT)

| Feature | Description |
|---------|-------------|
| Normal state | CLOSED (frozen) — heaters energized keep salt frozen |
| Fail mode (power loss) | OPEN — heaters de-energize; decay heat melts plug → fuel drains |
| Heater control | Energized to maintain frozen; de-energize to open |
| Cooling | Active cooling (air jets) assist freezing; NOT required after power loss |
| Opening time | ~5–15 min after heaters off (depends on decay heat) |

### Type B: Isolation Freeze Valve (Fail-Closed)
Used on: Fill lines, sample lines, maintenance isolation

| Feature | Description |
|---------|-------------|
| Normal state | CLOSED (frozen) — no heaters |
| Open mode | Heaters energized → plug melts → flow begins |
| Fail mode | CLOSED (frozen) — heaters de-energize |
| Closing time | ~5–15 min after heaters off |

---

## Valve Construction

### Freeze Section (the valve body)
- A short section (~152 mm / 6 in) of small-bore Hastelloy-N tubing is the "valve body."
- This section is thermally isolated from the rest of the piping.
- External provisions: electric heater wires (resistance wire wound on tube) AND cooling air nozzle.

### Dimensions

| Parameter | Metric | Imperial |
|-----------|--------|----------|
| Tube OD (valve body) | 25.4–60.3 mm | 1–2.4 in (same size as drain line) |
| Tube wall thickness | 3.18 mm | 0.125 in |
| Tube material | Hastelloy-N | ASTM B622, UNS N10003 |
| Freeze section length | 152 mm | 6.0 in |
| Heater element power | ~500 W total per valve | — |
| Heater wire | NiCr resistance wire, 500 W/ft² surface heat flux | — |
| Cooling air nozzle OD | 12.7 mm | 0.5 in |
| Cooling air flow (closed state assist) | ~10 L/min | — |
| Insulation (freeze section) | NONE on freeze section (to allow heat rejection) | — |
| Insulation (adjacent piping) | Standard high-temp ceramic fiber | — |

### Heater Design
- Resistance wire (NiCr, 80/20 nichrome) wound on valve body tube.
- Wire embedded in refractory cement (Al₂O₃ or MgO) to maintain contact and electrical isolation.
- Total heater element resistance: ~29 Ω (500 W at 120 V AC).
- Leads exit through sealed conduit to junction box outside insulation.
- Multiple heater zones (typically 2 per valve — primary and backup) for redundancy.

### Thermal Analysis (Freeze/Thaw Cycle)

| Condition | Parameters |
|-----------|-----------|
| Salt liquidus (fuel) | ~450 °C |
| Salt liquidus (coolant) | ~459 °C |
| Frozen plug temperature | ~350–400 °C (heater keeps plug cold) |
| Open plug temperature | >480 °C (above liquidus with margin) |
| Heater power to maintain frozen state | ~250 W typical |
| Time to open (300 W heater, starting from 350°C) | ~5–10 min |
| Time to close (200 cfm cooling air, starting from 500°C) | ~10–20 min |

---

## Freeze Valve Inventory (MSRE Primary System)

| Tag | Size | Type | Location |
|-----|------|------|---------|
| FV-101 | 2-in | Type A (fail-open drain) | Primary loop → FDT drain line |
| FV-102 | 1-in | Type B (fail-closed) | Sampler/enricher isolation |
| FV-103 | 2-in | Type B (fail-closed) | FDT → primary loop fill line |
| FV-104 | 2-in | Type B (fail-closed) | FDT → overflow tank |
| FV-201 | 2-in | Type B (fail-closed) | Coolant loop drain line |

---

## Fabrication

1. Machine Hastelloy-N tube to form freeze section (no groove required; smooth exterior).
2. Wind NiCr resistance wire in spiral pattern around freeze section; secure with refractory cement.
3. Terminate heater leads in stainless steel conduit with mineral-insulated (MI) lead extension.
4. Weld cooling air nozzle (12.7 mm) to freeze section (tangential or impinging arrangement).
5. Weld freeze valve section inline in piping — butt-weld or flanged connection.
6. Leave freeze section uninsulated; apply ceramic fiber insulation to adjacent sections.
7. Route heater conduit and air line to junction box outside insulation.
8. Test: cool with air jets; verify salt freezes (monitored by thermocouple on freeze section); apply heaters; verify salt melts; cycle 10 times; check heater resistance.

---

## Interfaces

| Interface | Connected To | Type |
|-----------|-------------|------|
| Upstream pipe | Loop piping or drain line | Butt weld |
| Downstream pipe | Drain line or drain tank | Butt weld |
| Heater leads | Heater power supply (120 V AC) | Terminal strip in junction box |
| Cooling air nozzle | Instrument air supply (dry, clean) | Compression fitting, 12.7 mm |
| Thermocouple | Temperature monitoring | Type K TC, compression fitting |
