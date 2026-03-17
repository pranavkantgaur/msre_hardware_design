# Component 10: Reactor Cell (Biological Shielding and Containment)

## Overview

The reactor cell is the reinforced-concrete room that houses all primary loop components — the reactor vessel, primary heat exchanger, fuel salt pump, drain tanks, and associated piping. It serves as:
1. **Biological shielding** to protect personnel from radiation during and after operation.
2. **Secondary containment** to prevent release of radioactive material.
3. **Inert atmosphere enclosure** (N₂ purge) to prevent air/moisture contact with hot salt.

**Primary Reference:** ORNL-TM-728, Section 4.1; ORNL-3014

---

## Cell Geometry

| Parameter | Metric | Imperial |
|-----------|--------|----------|
| Cell plan dimensions (approximate) | ~7.0 m × 7.0 m | ~23 ft × 23 ft |
| Cell clear height (inside) | ~7.6 m | ~25 ft |
| Primary concrete wall thickness | 1.52–2.44 m | 5–8 ft (varies by shielding analysis) |
| Roof/ceiling thickness | ~2.44 m | ~8 ft |
| Floor thickness (above drain tank cell) | ~1.22 m | ~4 ft |
| Concrete density (shield) | 2,307 kg/m³ (normal weight) or 3,520 kg/m³ (heavy) | 144 or 220 lb/ft³ |

---

## Shielding Design

### Shielding Goal
- Dose rate at cell exterior during full-power operation: <0.25 mSv/h (25 mrem/h).
- After shutdown (1 h, no entry required): cell dose rate acceptable for crane operations outside cell.
- Direct-entry maintenance in cell: only after >72 h decay cooling and detailed radiological survey.

### Shielding Materials and Thicknesses

| Location | Primary Material | Thickness | Secondary Material |
|----------|-----------------|-----------|-------------------|
| Side walls (biological shield) | Ordinary concrete (baritic concrete in some locations) | 1.52–2.44 m | — |
| Roof slab | Ordinary concrete | 2.44 m | — |
| Viewing windows | Dense glass (borosilicate leaded glass, several layers) | ~0.60 m total | Steel frame |
| Access door | Steel-faced lead-filled door | ~0.50 m | — |
| Penetrations (piping) | Concrete plugs + lead sleeves | Varies | — |

---

## Cell Atmosphere (Nitrogen Purge)

### Purpose
- Exclude air and moisture from the hot (>600 °C) Hastelloy-N and salt equipment.
- Prevent oxidation of graphite and metallic components.
- Provide inert blanket to reduce corrosion of uninsulated surfaces.

### Nitrogen System

| Parameter | Value |
|-----------|-------|
| Atmosphere | Dry nitrogen, dew point <−40 °C |
| Cell pressure | ~0.1–0.3 kPa below atmospheric (slightly negative) |
| N₂ supply pressure | ~150 kPa (20 psig) |
| Normal purge flow | ~2 m³/h (to make up for leakage) |
| Oxygen level (operating limit) | <100 ppm by volume |
| Moisture level (operating limit) | <100 ppm by volume |

### Cell Atmosphere Monitoring
| Tag | Parameter | Instrument |
|-----|-----------|-----------|
| AI-1001 | O₂ concentration | Zirconia O₂ analyzer |
| AI-1002 | Moisture (dew point) | Chilled-mirror dew point meter |
| RI-1001 | Cell gamma radiation | Ion chamber (range: 1 mR/h to 100 R/h) |
| PI-1001 | Cell differential pressure | Differential pressure transmitter |

---

## Penetrations

All penetrations through the reactor cell walls must be sealed to maintain containment and inert atmosphere.

### Electrical/Instrumentation Penetrations
- Multi-pin sealed connectors with lead-filled or epoxy-filled bodies.
- Radiation-resistant cable and connectors inside cell.
- MI (mineral-insulated) cable inside cell wall; standard cable outside.

### Piping Penetrations
- Annular gap between pipe and concrete sleeve is sealed with lead wool + grout.
- All penetrations are through the cell wall at an angle to prevent direct line-of-sight shine.
- Secondary coolant piping (lower activity) exits through side wall to pump house.

### Personnel Access Hatch
- Double-door airlock (one inner, one outer — never both open simultaneously).
- Inner door: 50 mm lead-filled steel.
- Outer door: standard industrial door with radiation contamination control mat.

---

## Overhead Crane

| Parameter | Value |
|-----------|-------|
| Crane capacity | ~10 tonnes (safe working load) |
| Crane type | Overhead bridge crane, 1 bridge + 1 trolley |
| Span | ~7.0 m (cell width) |
| Hook height | ~6.0 m (to lift reactor vessel head for removal) |
| Remote operation | Pendant (no person in cell during crane operation) |
| Shielding | Not required (operated from outside cell or outside shielded area) |

---

## Shielded Viewing Windows

- 3 windows in cell wall for visual inspection without entering cell.
- Each window: ~0.5 m × 0.5 m clear view.
- Material: 4 layers of lead glass (borosilicate, high-density) totaling ~0.6 m.
- Illumination: Remotely aimed flood lights inside cell.

---

## Heated Floor

- Cell floor and lower walls are heated to prevent moisture condensation and maintain salt above liquidus if spilled.
- Floor heat tracing: electric resistance elements embedded in concrete surface.
- Set point: ~150 °C floor surface.
- This limits freeze-up of any salt spill to a thin layer.

---

## Cell Dimensions and Interfaces

| Interface | Description |
|-----------|-------------|
| Reactor vessel pedestal | Reinforced concrete block, ~1 m diameter, 0.6 m high, at cell center |
| Primary HX support | Concrete floor pads with anchor bolts |
| Pump house (secondary loop) | Opening in shared wall; covered by removable concrete plug when not in use |
| Drain tank cell (below) | Access hatch through floor (1 m × 1 m) |
| Off-gas cell | Penetration for off-gas line through shared wall |
| Ventilation exhaust | Single exhaust duct through shield wall → HEPA filter → stack |
