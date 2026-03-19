# Component 01: Reactor Vessel

## Overview

The reactor vessel is the primary Hastelloy-N pressure boundary that contains the graphite moderator core and directs the flow of fuel salt through the core. It is the heart of the MSRE primary loop.

**Primary Reference:** ORNL-TM-728, Section 3.2

---

## Operating Conditions

| Parameter | Value |
|-----------|-------|
| Operating temperature (fuel salt) | 632–654 °C (1170–1210 °F) |
| Maximum design temperature | 704 °C (1300 °F) |
| Operating pressure (max) | 172 kPa gauge (25 psig) |
| Design pressure | 345 kPa gauge (50 psig) |
| Radiation environment | High neutron and gamma flux inside core region |
| Atmosphere outside vessel (reactor cell) | Dry N₂ |

---

## Key Dimensions

| Parameter | Metric | Imperial |
|-----------|--------|----------|
| Vessel outside diameter (cylindrical shell) | 1.410 m | 55.5 in |
| Vessel wall thickness (cylindrical shell) | 12.7 mm | 0.5 in |
| Overall vessel height (including heads) | ~2.90 m *(corrected from 2.44 m — see note)* | ~114 in |
| Core region height (fuel-bearing zone) | 1.626 m | 64 in |
| Core region diameter | 1.372 m *(corrected from 1.397 m)* | 54.0 in |
| Lower head thickness | 19.1 mm | 0.75 in |
| Upper head thickness | 19.1 mm | 0.75 in |
| Fuel outlet nozzle OD | 114.3 mm (4-in SCH40) | 4.5 in |
| Fuel inlet nozzle OD | 114.3 mm (4-in SCH40) | 4.5 in |
| Control rod penetrations (3×) | 60.3 mm (2-in SCH40) | 2.375 in |
| Thermocouple penetrations | 12.7 mm | 0.5 in |

---

## Material Specifications

| Part | Material | Specification |
|------|----------|--------------|
| Cylindrical shell | Hastelloy-N (INOR-8) | ASTM B619/B622; UNS N10003 |
| Upper and lower heads | Hastelloy-N | Forged or formed from plate, ASTM B575 |
| Nozzles | Hastelloy-N | Seamless pipe/tube, ASTM B622 |
| Weld filler | Hastelloy-N matching composition | ERNiMo-1 or equivalent |
| Gaskets (if any flanges) | Annealed nickel | ASTM B162 Ni201 |

---

## Design Details

### Shell Construction
- Cylindrical shell fabricated from rolled and seam-welded Hastelloy-N plate, or from a seamless forging (preferred to minimize welds in neutron field).
- All longitudinal and circumferential welds inspected by radiography (100%) and dye penetrant.
- Post-weld solution anneal at 1175 °C (2150 °F) in Ar or He atmosphere, followed by water quench.

> **Overall height note:** Shell tan-to-tan = 2134.6 mm (84 in); each 2:1 semi-ellipsoidal
> head adds ≈ 346 mm (13.6 in) internally plus wall thickness ≈ 19 mm; upper flange
> adds ≈ 80 mm. Calculated total ≈ 2134.6 + 2 × 365 + 80 ≈ 2945 mm ≈ 2.90 m (114 in).
> Previous value of 2.44 m (96 in) was a shell-only approximation. Verify against
> ORNL-TM-728 Figure 3.1 general arrangement drawing.
- Both upper and lower heads are ellipsoidal (2:1 semi-ellipsoidal) Hastelloy-N forgings.
- Upper head is removable (bolted flange with annealed nickel ring gasket) to allow core removal.
- Upper head bolting: 24 × M32 (1.25-in) Hastelloy-N studs and nuts; torque to achieve seal without yielding gasket.

### Internal Flow Distribution
- **Lower plenum:** Fuel salt enters through bottom nozzle, distributed across the core lower face by a perforated distributor plate.
- **Graphite core region:** Fuel salt flows upward through channels machined in graphite stringers (~22.5% void fraction).
- **Upper plenum:** Fuel salt collects above the graphite and exits through the top outlet nozzle.
- Plenum height (lower): ~254 mm (10 in)
- Plenum height (upper): ~305 mm (12 in)

### Core Support Structure
- Graphite core is supported by a Hastelloy-N grid plate at the bottom of the core region.
- Grid plate has holes matching the cross-section of each graphite stringer (2 in × 2 in nominal).
- Upper restraint: graphite held in place by the upper grid/hold-down structure attached to upper head.
- Thermal expansion differential between Hastelloy-N vessel (~13.1 × 10⁻⁶/°C) and graphite (~2–4 × 10⁻⁶/°C) is accommodated by sliding fit in the grid plate.

### Penetrations and Nozzles
| Nozzle | Location | Size | Purpose |
|--------|----------|------|---------|
| Fuel inlet | Lower head | 4 in SCH40 | Fuel salt inlet from HX |
| Fuel outlet | Upper head | 4 in SCH40 | Fuel salt exit to pump |
| Control rod #1 (regulating) | Upper head | 2 in SCH40 | Rod drive penetration |
| Control rod #2 (regulating) | Upper head | 2 in SCH40 | Rod drive penetration |
| Control rod #3 (safety) | Upper head | 2 in SCH40 | Rod drive penetration |
| Neutron source | Upper head | 0.5 in | Startup source |
| Thermocouple wells | Upper head (×6), lower head (×4) | 0.5 in | Temperature measurement |

---

## Fabrication Process

1. **Plate procurement:** Order ASTM B575 Hastelloy-N plate in required thickness; obtain certified material test reports (CMTR) confirming composition and properties.
2. **Plate rolling:** Roll cylindrical shell sections to required curvature; fit-up and tack-weld longitudinal seams.
3. **Shell welding:** Complete longitudinal seam welds by GTAW process; inspect 100% by radiography.
4. **Head forging:** Procure or forge 2:1 ellipsoidal heads; trim and machine to final dimensions.
5. **Nozzle attachment:** Machine nozzle set-on holes in shell and heads; fit nozzles; complete fillet-and-groove welds.
6. **NDE:** 100% radiographic and dye-penetrant inspection of all welds.
7. **Post-weld heat treatment:** Full assembly anneal at 1175 °C in Ar/He furnace.
8. **Final machining:** Machine upper flange seating face; drill and tap stud holes.
9. **Dimensional inspection:** Verify all dimensions per drawing.
10. **Pressure test:** Pneumatic test at 1.5× design pressure (518 kPa / 75 psig) with N₂; no hydrostatic test (water contamination risk).
11. **Internal surface inspection:** Borescope inspection of internal surfaces.

---

## Quality Requirements

- All Hastelloy-N material must have CMTR with composition, hardness, and tensile test data.
- Welder qualification per ASME BPVC Section IX.
- Welding procedure specification (WPS) for Hastelloy-N GTAW, qualified per Section IX.
- All welds: RT (radiographic test) to ASME B31.3 Severity Level 1 (zero linear indications in final film).
- Post-weld heat treatment: record furnace temperature chart; maintain 1175 ±14 °C for 30 minutes minimum.

---

## Interfaces

| Interface | Connected To | Connection Type |
|-----------|-------------|-----------------|
| Fuel inlet nozzle | Primary HX return pipe | Butt weld, 4-in SCH40 |
| Fuel outlet nozzle | Fuel salt pump inlet | Butt weld, 4-in SCH40 |
| Control rod penetrations | Control rod drive assemblies | Welded seal + drive shaft coupling |
| Upper head flange | Reactor cell crane (for removal) | Lifting lugs, 4× Hastelloy-N |
| Vessel exterior | Reactor cell structure | Support skirt welded to lower head |
| Thermocouple penetrations | Instrumentation cables | MI thermocouple, welded fitting |
