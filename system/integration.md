# System Integration

This document describes how all MSRE components interface with each other — mechanically, thermally, and functionally — to form the complete reactor system.

---

## 1. Physical Layout and Mechanical Integration

### Reactor Cell Arrangement

All primary loop components are located within the reactor cell (heavily shielded reinforced-concrete room):

```
Plan View (approximate, not to scale):

    +-------------------------------------------+
    |           REACTOR CELL                    |
    |                                           |
    |    [Reactor Vessel]                       |
    |         |                                 |
    |    (fuel outlet pipe, top)                |
    |         |                                 |
    |    [Fuel Salt Pump]  ←→  [Pump Motor]    |
    |         |                  (above cell)   |
    |    (discharge pipe)                       |
    |         |                                 |
    |    [Primary Heat Exchanger]               |
    |         |                                 |
    |    (return pipe to vessel inlet)          |
    |                                           |
    |    [Freeze Valves FV-101, FV-103]        |
    |         |                                 |
    | [Fuel Drain Tank]    [Overflow Tank]      |
    |                                           |
    +-------------------------------------------+
```

### Elevation Notes
- Reactor vessel sits on a concrete pedestal.
- Fuel drain tank is located below and offset from the reactor vessel so fuel drains by gravity.
- Primary heat exchanger is located adjacent to the reactor vessel; elevation chosen to ensure adequate NPSH for the fuel salt pump.
- All primary loop piping slopes to allow complete drain to the drain tank (no low pockets that trap salt).

---

## 2. Mechanical Interface Summary

### Reactor Vessel ↔ Core
- Graphite core assembly is inserted into the reactor vessel as a unit through the vessel top head.
- Core support structure locates and holds the graphite stringers; provides lower and upper plenum separation.
- Thermal expansion of graphite and vessel must be accommodated by the core support design (sliding fit with graphite retaining structure).

### Reactor Vessel ↔ Piping
- Fuel outlet nozzle: top of vessel (DN125 / 5-in schedule-40 Hastelloy-N butt weld); 5-in main loop piping per ORNL MSRE film (ORNL, 1966)
- Fuel inlet nozzle: bottom of vessel lower plenum (DN125 / 5-in)
- Control rod nozzles: top head (3 × DN50 / 2-in penetrations with seal weldments)
- Thermocouple penetrations: multiple (DN12 / 0.5-in)
- Off-gas nozzle: top head (DN12 / 0.5-in)
- All nozzles are butt-welded; no flanged nozzles on primary loop vessels.

### Fuel Salt Pump ↔ Piping
- Pump bowl inlet: fuel return from heat exchanger (gravity-fed to pump suction)
- Pump discharge: top of pump bowl → 4-in piping to reactor vessel inlet
- Pump cover gas line: DN12 He sparge inlet at pump bowl top flange
- Off-gas outlet: DN12 line from pump bowl gas space to off-gas system

### Primary Heat Exchanger ↔ Piping
- Fuel salt (shell side): 5-in inlet/outlet nozzles, butt-welded; 5-in main loop pipe per ORNL MSRE film (ORNL, 1966)
- Coolant salt (tube side): 3-in inlet/outlet nozzles at tube sheet, butt-welded
- Shell is horizontal orientation; coolant enters cold leg (from radiator), exits hot leg (to radiator)

### Freeze Valve ↔ Piping
- Inserted inline in 1-in or 2-in drain lines
- Flanged at both ends with Hastelloy-N metal gaskets (to allow replacement)
- Electrical heater wires and cooling air nozzle terminate at junction box outside insulation

---

## 3. Thermal Interface Summary

### Heat Flow Paths

```
Fission Heat (in core fuel salt)
    → Fuel Salt (convection in primary loop)
        → Primary HX (conduction through tube walls)
            → Coolant Salt (convection in secondary loop)
                → Coolant Radiator (convection/radiation to air)
                    → Atmosphere
```

### Temperature Interface Points

| Interface | Fuel Side T | Coolant Side T | ΔT Driving |
|-----------|------------|----------------|-----------|
| Core inlet/outlet | 632/654 °C | N/A | — |
| Primary HX (hot end) | 654 °C (fuel in) | 621 °C (coolant out) | 33 °C |
| Primary HX (cold end) | 632 °C (fuel out) | 546 °C (coolant in) | 86 °C |
| Radiator (hot end) | N/A | 621 °C (coolant in) | Δ to ~38 °C air |
| Radiator (cold end) | N/A | 546 °C (coolant out) | Δ to ~24 °C air |

### Heat Tracing Integration
- All primary and secondary loop piping, vessels, and instruments are heat-traced.
- Heat tracing power zones are arranged so that each section can be independently powered for startup and maintenance.
- Minimum heat trace circuit: one electrical zone per pipe spool between support points.
- Set point: maintain pipe wall temperature ≥530 °C (80 °C above LiF-BeF₂ liquidus with margin).

---

## 4. Instrumentation Integration

### Signal Routing
- All thermocouple signals route to a central temperature monitoring panel in the control room.
- Flow signals (magnetic flowmeters, 4–20 mA outputs) route to the control room flow panel.
- Neutron flux signals (ionization chambers, fission chambers) route to the nuclear instrumentation panel.
- All analog signals are 4–20 mA or thermocouple mV, isolated at the cell penetration feed-through.

### Penetration Seals
- Instrumentation cables pass through the reactor cell wall via lead-filled multi-pin sealed connectors (radiation-resistant).
- Cable insulation: mineral-insulated (MI) cable inside the cell; standard instrumentation cable outside.

### Control System Architecture
```
Sensors (TCs, flowmeters, flux chambers)
    → Signal Conditioning (in local junction boxes)
        → Cell Wall Penetrations
            → Control Room Panels
                → Operator Interface (analog meters, chart recorders)
                → Safety Interlock System (hardwired relay logic)
                → Control Rod Drives (motor controllers)
                → Freeze Valve Heater Controllers
                → Pump Motor Starters
```

---

## 5. Electrical Power Integration

| Load | Power Type | Approximate Load |
|------|-----------|-----------------|
| Fuel salt pump motor | 480V AC, 3-phase | 75 hp (56 kW) |
| Coolant salt pump motor | 480V AC, 3-phase | 30 hp (22 kW) |
| Heat tracing (all) | 240V AC (single-phase zones) | ~150 kW total |
| Freeze valve heaters | 120V AC | ~500 W per valve |
| Radiator fans | 480V AC | ~15 kW total |
| Instrumentation | 24V DC (isolated supply) | ~5 kW |
| Emergency lighting | UPS-backed 120V AC | ~2 kW |

**Critical Safety Power:** Freeze valve heaters must be on emergency power such that a complete loss of AC power causes heaters to de-energize → valves begin thaw → passive drain.

---

## 6. Inert Gas System Integration

| Zone | Gas | Purpose |
|------|-----|---------|
| Reactor cell atmosphere | Dry N₂ | Exclude air/moisture; fire prevention |
| Primary loop cover gas | He (helium) | Sparge in pump bowl; noble gas blanket |
| Secondary loop cover gas | He (helium) | Blanket over coolant pump bowl |
| Salt preparation glove box | Dry N₂ or He | Salt mixing without moisture |
| Drain tank cover gas | He | Monitor drain tank condition |

---

## 7. Assembly Sequence (Top Level)

1. **Install reactor cell** — concrete walls, penetrations, crane, shielded windows.
2. **Set reactor vessel** on pedestal; connect support structure.
3. **Load graphite core** through top head; install top head.
4. **Install primary heat exchanger** — mount, connect fuel and coolant nozzles.
5. **Install fuel drain tanks** — set in drain tank cell; connect to freeze valves and drain lines.
6. **Install freeze valves** — inline in drain and fill lines; connect heaters.
7. **Install fuel salt pump** — connect discharge pipe; connect motor shaft coupling; connect cover gas and off-gas lines.
8. **Install coolant salt pump and radiator** — in pump house.
9. **Install off-gas system** — connect from pump bowl off-gas nozzle through cell wall to charcoal beds.
10. **Install control rod drives** — mount on top head penetrations; connect to drive motors.
11. **Install heat tracing** — all piping and vessels; zone-test each circuit.
12. **Install insulation** — over all heat-traced components.
13. **Install instrumentation** — thermocouples, flowmeters, flux detectors; route cables to control room.
14. **Pressure test** — pneumatic leak test of all primary loop at ambient temperature (cold conditions only; no hydraulic testing with water).
15. **Dry bake-out** — heat-trace all piping to ≥350 °C under flowing dry N₂ for ≥48 hours to remove moisture.
16. **Salt introduction** — load carrier salt (no uranium) first; verify flow; then add UF₄ to achieve criticality.
