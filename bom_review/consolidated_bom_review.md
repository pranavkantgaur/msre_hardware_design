# MSRE Hardware Design — Consolidated BOM Review Report

**Multi-agent review produced by:** msr-gstack  
**Skill definitions source:** https://github.com/pranavkantgaur/msr-gstack/tree/copilot/setup-multi-agent-system  
**Hardware BOM source:** `components/*/bom.csv` (12 components, 171 line items)  
**Review date:** 2026-03-17  

---

## How This Review Was Produced

Each component BOM was reviewed by instantiating the relevant msr-gstack domain agents. The
agent skill files define structured review workflows with domain-specific checklists. For each
component, the applicable agent(s) were invoked with the BOM CSV as input and applied their
checklists to identify findings. Findings are classified as CRITICAL / SIGNIFICANT / MINOR
per the severity definitions in each SKILL.md.

---

## Component 01 — Reactor Vessel

**Agents:** `review-reactor-design`, `review-materials`  
**BOM file:** `components/01_reactor_vessel/bom.csv` (19 line items)

### Materials Review Checklist (`review-materials`)

- ✅ **Alloy identification:** All salt-wetted components correctly specified as Hastelloy-N, UNS N10003, per ASTM B575 (plate), B622 (pipe/tube), B574 (bar). Consistent throughout all 19 items.
- ✅ **Gaskets:** RV-018 correctly specified as annealed pure nickel (ASTM B162 Ni201) — no organic gaskets. Correct for fluoride salt service.
- ✅ **Weld filler:** RV-019 ERNiMo-1 is the correct Hastelloy-N matching composition filler wire.
- ✅ **Post-weld heat treatment:** "Solution anneal 1175°C post-weld" noted on RV-001. Matches `docs/materials_guide.md` requirement.

### 🟠 SIGNIFICANT — RV-016: Incorrect Stud Specification Reference

**Item:** RV-016, Upper head stud  
**Issue:** Specification column reads "ASTM A193 Grade B8 N equiv. (Hastelloy-N bolting)." ASTM A193
Grade B8 is a Type 316 austenitic stainless steel bolt specification, not a Hastelloy-N
specification. ASTM A193 does not include Hastelloy-N. The correct procurement standard for
Hastelloy-N bolting is ASTM B574 bar (machined studs) or a project-specific specification
referencing UNS N10003.

**Recommended action:** Replace "ASTM A193 Grade B8 N equiv." with "Machined from ASTM B574
bar; UNS N10003" to match the material actually intended and to avoid procurement of
wrong-alloy fasteners.

### 🟠 SIGNIFICANT — RV-012/RV-013: Duplicate Grid Plates vs. RC-005/RC-006

**Items:** RV-012 (Core support grid, lower), RV-013 (Core hold-down grid, upper)  
**Issue:** These two items are also listed in the Reactor Core BOM as RC-005 and RC-006 with
identical descriptions, dimensions, and specifications. Both BOMs specify 1380 mm dia,
25.4 mm thick Hastelloy-N grid plates. Having the same physical parts in two separate BOMs
creates double-counting risk in procurement and a scope-of-supply ambiguity between the
vessel fabricator and the core assembler.

**Recommended action:** Remove RV-012 and RV-013 from the Reactor Vessel BOM and retain them
only in the Reactor Core BOM (RC-005, RC-006) with a cross-reference note in the vessel BOM.
Alternatively, designate the grid plates as a separate "core internals" assembly with a single
master BOM.

### 🟡 MINOR — RV-005: Weld Transition Ring

**Item:** RV-005, Shell-to-lower-head weld transition ring  
**Issue:** ORNL-TM-728 describes the vessel as a cylindrical shell welded directly to the lower
ellipsoidal head using a standard girth weld (no transition ring). A separate forged weld
transition ring would be unusual for this geometry. The purpose of this item should be
clarified — if it is a backing ring or weld reinforcement, the notes should state this
explicitly, as backing rings in nuclear service are typically prohibited or require specific
justification.

### 🟡 MINOR — RV-011: Distributor Plate Hole Pattern

**Item:** RV-011, Lower plenum distributor plate  
**Issue:** BOM note states "hole pattern matches core stringer grid" without specifying the
actual hole diameter, number, or open-area fraction. For procurement, the distributor plate
drawing reference or a complete hole specification should be included.

---

## Component 02 — Reactor Core (Graphite Moderator Assembly)

**Agents:** `review-reactor-design`, `review-materials`, `review-fuel-cycle`  
**BOM file:** `components/02_reactor_core/bom.csv` (10 line items)

### Reactor Design Review Checklist (`review-reactor-design`)

- ✅ **Graphite grade:** AGOT nuclear-grade graphite, <25 ppm ash, <5 ppm B-equivalent. Adequate for thermal neutron economy.
- ✅ **Control rod thimbles:** RC-004, Hastelloy-N ASTM B622, 3 off. Correct material and count.
- ✅ **Support grids:** RC-005 and RC-006, Hastelloy-N ASTM B575. Correct.

### 🟠 SIGNIFICANT — RC-001/RC-002: Stringer Counts Still Require Primary Source Verification

**Items:** RC-001 (226 Zone I stringers), RC-002 (283 Zone II stringers)  
**Issue:** Both counts were recently corrected from 876/264 (geometrically impossible values)
to 226/283 using geometric calculation. The BOM notes correctly flag "Verify exact count
against ORNL-TM-728 Table 3.1." Until this verification is performed, the graphite procurement
quantity is uncertain. Ordering 509 stringers when the actual count is different would either
result in core assembly failure (too few) or waste of costly nuclear-grade graphite (too many).

**Recommended action:** Access ORNL-TM-728 Table 3.1 and confirm exact stringer counts before
issuing the BOM for procurement. Add a "HOLD — pending ORNL-TM-728 verification" flag to
RC-001 and RC-002.

### 🟠 SIGNIFICANT — RC-010: Furfuryl Alcohol — No Hazard Classification or Storage Specification

**Item:** RC-010, Furfuryl alcohol monomer (sealing agent)  
**Issue:** Furfuryl alcohol is a flammable liquid (flash point 75°C, autoignition ~490°C) and
a suspected carcinogen (IARC Group 2B). The BOM specifies "Technical grade >98% purity" and
"as req'd, L" but includes no:
- Hazmat classification (UN 2874, Class 3, PG III)
- Storage specification (flammable liquid cabinet, temperature limit)
- Maximum inventory limit (for fire code compliance)
- PPE/handling requirements reference
- Shelf-life specification (furfuryl alcohol polymerizes in storage; shelf life ~12 months)

For a fabrication BOM, these are procurement and facility requirements, not merely chemistry notes.

**Recommended action:** Add hazmat classification, storage limit, shelf-life spec, and reference
to applicable OSHA/facility safety plan for furfuryl alcohol handling.

### Fuel Cycle Review (`review-fuel-cycle`)

- ✅ **Noble gas removal:** The core BOM does not include noble gas removal equipment (correctly — that is in the Off-Gas System BOM, Component 08). Cross-component consistency confirmed.
- ✅ **Graphite boron limit:** <5 ppm B-equivalent on RC-001/RC-002/RC-003. Adequate for neutron economy in a thermal reactor. Cross-referenced with `docs/materials_guide.md`.

### 🟡 MINOR — RC-003: Reflector Block Count Approximate

**Item:** RC-003, 120 graphite reflector blocks  
**Issue:** Notes state "Count approximate — verify against ORNL-TM-728." For a nuclear-grade
graphite procurement, the block count and shape types (wedge, rectangle, etc.) must be specified
exactly to ensure correct shielding geometry. Approximate counts are not acceptable for the
actual procurement document.

### 🟡 MINOR — RC-009: Alignment Pin Count Basis

**Item:** RC-009, 100 alignment pins  
**Issue:** The quantity of 100 pins is stated without a calculation basis. If one pin locates
every 4th stringer precisely (as the notes state), the required count would be approximately
509 ÷ 4 ≈ 128 pins (rounded to account for grid boundaries). The stated quantity of 100 pins
appears insufficient. Suggest recalculating based on the corrected stringer count.

---

## Component 03 — Primary Heat Exchanger

**Agents:** `review-reactor-design`, `review-materials`, `review-salt-chemistry`  
**BOM file:** `components/03_primary_heat_exchanger/bom.csv` (13 line items)

### Materials Review

- ✅ **All pressure-boundary items:** Hastelloy-N, UNS N10003, ASTM B622/B575 throughout. Correct for fluoride salt service on both shell (fuel salt) and tube (coolant salt) sides.
- ✅ **Tube specification:** PHX-002, 9.525 mm OD × 0.889 mm wall (3/8-in × 0.035-in), ASTM B622. Matches specifications.md.

### 🟠 SIGNIFICANT — PHX-009: Baffle Count Inconsistency

**Item:** PHX-009, 22 segmental baffle plates  
**Issue:** Shell length is 5030 mm (PHX-001 notes: "5030 lg"). Specification states baffle spacing
of 203 mm (8 in). At 203 mm spacing in a 5030 mm shell:

  Number of baffle spaces = 5030 / 203 ≈ 24.8 → requires **25 baffles** (or 24 with slightly
  adjusted end spacing), not 22.

With 22 baffles: average baffle spacing = 5030 / 22 ≈ 229 mm. This 13% increase in baffle
spacing reduces the shell-side heat transfer coefficient by approximately 6–8%, potentially
reducing the overall U below the 4,200 W/(m²·K) design value and the effective heat transfer
area below 36.5 m².

**Recommended action:** Recalculate baffle count at 203 mm spacing and update BOM to 25 baffles.
Alternatively, confirm that 229 mm spacing is acceptable based on revised thermal calculation,
and update both the BOM and specifications.md.

### 🟡 MINOR — PHX-012: Carbon Steel Support Saddle — Galvanic Isolation

**Item:** PHX-012, Carbon steel support saddle  
**Issue:** Notes state "insulated exterior" but do not specify the insulation type or material
separating the carbon steel saddle from the Hastelloy-N shell. In a high-temperature reactor
cell environment, standard elastomeric insulators may degrade. A ceramic pad or Hastelloy-N
liner between saddle and shell should be specified.

### 🟡 MINOR — PHX-002: Total Tube Length for Procurement

**Item:** PHX-002, 159 U-tubes  
**Issue:** The dimension field shows "~9960 lg (U-tube unrolled)" which is approximate. For
procurement, the total ordered length of B622 tube (in metres or feet) should be specified,
including bend loss and cut allowance. Suggest adding: "Total order quantity: 159 tubes × 10.2 m
each (with 2% waste allowance) = ~1,625 m of ASTM B622 seamless tube."

### Salt Chemistry Review (`review-salt-chemistry`)

- ✅ **Both sides Hastelloy-N:** Correct. Fluoride salt (fuel) on shell side, Flibe (coolant) on tube side — both require Hastelloy-N wetted surfaces.
- ✅ **No organic seals or gaskets** identified in HX BOM. Correct for fluoride salt service.

---

## Component 04 — Fuel Salt Pump

**Agents:** `review-materials`, `review-salt-chemistry`  
**BOM file:** `components/04_fuel_salt_pump/bom.csv` (17 line items)

### Materials Review

- ✅ **All salt-wetted components:** FSP-001 through FSP-006, FSP-013–FSP-015, Hastelloy-N UNS N10003. Correct.
- ✅ **Face seal materials:** FSP-007, Carbon graphite (GA90) rotating vs. Hastelloy-N stationary. Standard approach for molten salt face seals.
- ✅ **Motor spec:** FSP-010, 75 hp / 460 V / 1750 rpm matches specifications.md.
- ✅ **Sparge line:** FSP-013, 6.35 mm OD Hastelloy-N tube extending to 50 mm below salt surface.

### 🟡 MINOR — FSP-007: Single-Source Face Seal Grade

**Item:** FSP-007, Carbon graphite face seal  
**Issue:** Grade "GA90" is a proprietary Mersen (formerly Carbone-Lorraine) designation. No
alternative vendor or generic specification (e.g., density, hardness, tensile strength) is
given. For nuclear-grade components requiring qualified material substitutions, the BOM should
include either a generic functional specification or at least two qualified supplier grades
(e.g., "GA90 or SGL Carbon RG-series equivalent").

### 🟡 MINOR — FSP-013: He Sparge Line Cross-Reference

**Item:** FSP-013, He sparge dip tube, 500 mm long  
**Issue:** The pump bowl internal volume is ~150 L with a gas space of ~15 L. The note states
the dip tube extends "50 mm below salt surface." However, the salt surface position (~150 mm
below the cover plate) is only stated in specifications.md, not in the BOM. The BOM should
cross-reference the pump bowl internal layout drawing or specifications.md to confirm the
500 mm dip tube length is consistent with the as-installed salt level.

---

## Component 05 — Coolant Salt Pump

**Agents:** `review-materials`  
**BOM file:** `components/05_coolant_salt_pump/bom.csv` (13 line items)

### Materials Review

- ✅ **All salt-wetted components:** Hastelloy-N, UNS N10003. Correct for LiF-BeF₂ coolant salt.
- ✅ **Face seal:** CSP-007, same carbon graphite vs. Hastelloy-N design as fuel pump. Consistent.

### 🟠 SIGNIFICANT — CSP-008: Bearing Bore vs. Shaft Diameter Mismatch

**Item:** CSP-008, Upper shaft bearing, "SKF 6308 or equivalent; 40 mm bore"  
**Issue:** The pump shaft (CSP-004) is specified as 38.1 mm (1.5 in) diameter. SKF 6308 has a
40 mm bore. This is a 1.9 mm dimensional mismatch — the bearing will not fit directly on the
shaft without an adapter sleeve.

- If an adapter sleeve (e.g., SKF AH type) is intended, it must be added to the BOM.
- Alternatively, specify a bearing with 38 mm or 1.5-in bore (SKF 6308/C3 is not available
  in 38 mm bore; the closest metric standard is SKF 6307 — 35 mm bore — which is too small,
  or specify a custom bore bearing).

**Recommended action:** Either: (a) specify an adapter sleeve in the BOM; or (b) change the
shaft diameter from 38.1 mm to 40 mm and update CSP-004; or (c) specify a bearing with
38 mm bore explicitly.

---

## Component 06 — Fuel Drain Tank

**Agents:** `review-safety`, `review-salt-chemistry`  
**BOM file:** `components/06_fuel_drain_tank/bom.csv` (16 line items)

### Safety Review (`review-safety`)

- ✅ **Annular geometry for criticality control:** FDT-001 outer shell 1219 mm OD, FDT-002 inner cylinder 914 mm OD. Annular salt layer = (1219 − 914) / 2 = 152.5 mm ≈ 152 mm. Consistent with specifications.md criticality safety basis.
- ✅ **Overflow tank:** FDT-013/FDT-014 included with criticality control column. Correct.
- ✅ **Heat tracing:** FDT-012, 12 independently-powered zones. Good redundancy for passive heat removal.

### 🔴 CRITICAL — FDT-006: B₄C Absorber Loading Not Specified

**Item:** FDT-006, Boron carbide neutron absorber fill  
**Issue:** The BOM specifies "as req'd, kg" for the B₄C loading, with no baseline mass stated.
This is unacceptable for a safety-critical criticality control component. The center column B₄C
loading is the primary criticality control feature of the drain tank. Without a minimum specified
mass:

- Procurement could deliver insufficient B₄C, resulting in a drain tank that does not meet
  its criticality safety basis
- QA cannot verify that the as-built drain tank satisfies the safety analysis

The specification section (specifications.md) states "50–100 g ¹⁰B per meter of tank height"
but does not state a firm minimum, and this information is absent from the BOM.

**Recommended action:**
1. Determine the minimum B₄C mass from the criticality safety analysis (ORNL-TM-1647 or
   equivalent)
2. Specify the minimum mass in FDT-006 quantity field (e.g., "≥XX kg per tank, as specified
   in criticality safety analysis [document number]")
3. Add a QA hold point: "Do not close center column without QA verification of B₄C mass
   as-installed"

### 🟠 SIGNIFICANT — FDT-012: Heat Trace Zone Coverage Not Validated

**Item:** FDT-012, 12 electric heat trace zones  
**Issue:** The BOM lists "12 zones" for a tank that is 1524 mm tall × 1219 mm OD. At 12 zones
for a cylindrical tank, the zone coverage (number of zones in axial vs. circumferential
directions) is not specified. The specifications.md requires natural convection air cooling
at t=24h to maintain wall temperature below 800°C. Whether 12 zones provide uniform coverage
of the 7.0 m² tank surface is not verified in the BOM.

**Recommended action:** Add a note specifying the zone layout (e.g., "3 axial levels × 4
circumferential zones") and confirm coverage against the tank surface area calculation.

### 🟡 MINOR — FDT-015/FDT-016: "As req'd, m" Without Baseline

**Items:** FDT-015 (drain line), FDT-016 (fill line)  
**Issue:** Both drain and fill lines are specified "as req'd, m" without a baseline length
derived from the reactor cell layout. For procurement planning and heat trace design, the
total length of each line should be estimated from the cell layout and stated as a baseline
quantity (e.g., "estimated 6 m, verify against cell layout drawing").

---

## Component 07 — Freeze Valves

**Agents:** `review-safety`, `review-instrumentation`, `review-salt-chemistry`  
**BOM file:** `components/07_freeze_valves/bom.csv` (10 line items)

### Safety Review (`review-safety`)

- ✅ **Fail-safe design basis confirmed in BOM:** Freeze valve heaters de-energize on loss of power → plug melts → passive drain initiated. This passive safety function is the correct implementation.
- ✅ **Heater material:** FZV-004, NiCr 80/20 resistance wire, rated 1200°C. Correct material for high-temperature duty.
- ✅ **Cooling air nozzle:** FZV-007, tangential impingement for forced-air freeze. Correct approach.

### 🟠 SIGNIFICANT — FZV-001/FZV-003: FV-104 Undefined

**Items:** FZV-001 specifies "FV-101 FV-103 FV-104" (4 freeze sections), FZV-003 specifies "FV-201"  
**Issue:** The specifications.md discusses only FV-101 (drain valve) and FV-103 (fill valve),
and the system overview references the secondary loop drain valve. FV-104 is not defined
anywhere in the specifications.md, flow_diagram.md, or system/integration.md. The BOM
therefore includes a freeze valve with an undefined function and unspecified operating
requirements.

**Recommended action:** Either: (a) add a specification section for FV-104 defining its function,
normal state (open/closed), and actuation logic; or (b) remove FV-104 from FZV-001 if it is
not required and reduce freeze section tube quantity from 4 to 3.

### 🟠 SIGNIFICANT — FZV-008: Type K Thermocouple Material — Salt Contact Risk

**Item:** FZV-008, Type K thermocouple with Inconel sheath  
**Issue:** Per the `review-instrumentation` SKILL checklist, Chromel (Ni-10%Cr alloy, the
positive element of Type K) is attacked by fluoride salt environments. The freeze section tube
(FZV-001) is part of the salt-wetted piping. While the TC is mounted on the exterior of the
freeze section tube (not in the salt flow), the exterior surface may reach the salt liquidus
temperature (~450°C) during valve operation. At these temperatures in a fluoride-contaminated
atmosphere (salt vapors, salt aerosols), Chromel can suffer preferential Cr oxidation/fluoride
attack.

The BOM does not include service life data or replacement interval for the freeze valve TCs.
Per the instrumentation SKILL: "Is there a thermocouple calibration program with replacement
interval based on drift data at operating temperature?"

**Recommended action:** Specify a TC replacement interval (e.g., "replace every 18–24 months
or on drift > 10°C from reference"). Consider Type N thermocouples (Nicrosil-Nisil) which have
better oxidation resistance at this temperature range, or specify a Hastelloy-N outer protection
tube over the Inconel sheath if the TC is to be used near the salt-wetted zone.

---

## Component 08 — Off-Gas System

**Agents:** `review-fuel-cycle`, `review-instrumentation`  
**BOM file:** `components/08_off_gas_system/bom.csv` (13 line items)

### Fuel Cycle Review (`review-fuel-cycle`)

- ✅ **Noble gas removal confirmed:** OGS-005 (500 kg primary charcoal) + OGS-007 (750 kg secondary charcoal). The specifications.md demonstrates >10 half-life delays for all short-lived noble gas isotopes. Xe-135 removal is addressed. ✓
- ✅ **Sintered metal HEPA:** OGS-009, radiation-resistant for off-gas service. Correct selection.
- ✅ **He sparge flow controller:** OGS-012, mass flow controller for pump bowl sparge. Consistent with off-gas design.

### 🔴 CRITICAL — OGS: No Tritium Monitoring in Off-Gas BOM

**Issue:** The MSRE fuel salt (LiF-BeF₂-ZrF₄-UF₄) contains ⁶Li at <0.01% after ⁷Li enrichment.
Even at ≥99.99% ⁷Li enrichment, the tritium production from ⁶Li + n → T + ⁴He is non-zero.
Additionally, ternary fission produces tritium. For the MSRE at 8 MWt, the estimated tritium
production rate is approximately 50–200 Ci/year depending on ⁶Li content.

Tritium exits the primary system preferentially through the off-gas stream (as HT or HTO).
The off-gas BOM contains no:
- Tritium-in-gas analyzer (ionization chamber or liquid scintillation sampling)
- Catalytic oxidizer to convert HT → HTO for trapping
- Cold trap or molecular sieve for HTO retention
- Stack tritium monitor for effluent measurement

Without tritium monitoring in the off-gas system, there is no regulatory pathway to demonstrate
compliance with tritium effluent limits, and no way to quantify the tritium source term for
safety analysis.

**Recommended action:** Add to the off-gas BOM:
- OGS-0XX: Tritium-in-air monitor (ionization chamber type, range 10⁻³ to 10³ µCi/m³)
- OGS-0XX: Catalytic oxidizer unit (Pt catalyst, operating ~150°C) for HT → HTO conversion
- OGS-0XX: Molecular sieve or silica gel desiccant trap for HTO capture
- OGS-0XX: Stack tritium monitor at final exhaust point

Cross-reference: Same gap exists in I&C BOM (finding C-03).

### 🟡 MINOR — OGS-004: Material Specification Ambiguity

**Item:** OGS-004, Primary charcoal delay bed vessel  
**Issue:** Material specified as "304L SS or Hastelloy-N lined." The word "or" creates procurement
ambiguity — the fabricator may choose 304L SS without any lining, which may be inadequate if
there is any condensate carryover from the off-gas stream containing trace fluoride salt aerosol.
The specifications.md states "316L SS inner surfaces lined."

**Recommended action:** Change BOM to match specifications.md: "304L SS outer shell; 316L SS
inner lining on all salt-contact or condensate-contact surfaces."

---

## Component 09 — Control Rods

**Agents:** `review-reactor-design`, `review-safety`, `review-materials`  
**BOM file:** `components/09_control_rods/bom.csv` (12 line items)

### Safety Review (`review-safety`)

- ✅ **Fail-safe drop:** CRS-008 solenoid latch, "De-energize to drop (fail-safe)." Correct nuclear safety implementation — trip on loss of power.
- ✅ **3 rods:** 2 regulating (CRS-003) + 1 safety (CRS-004, CRS-008). Matches system design.
- ✅ **Drive travel:** CRS-007, 508 mm travel. Consistent with specifications.md.

### 🟠 SIGNIFICANT — CRS-007: Procurement Basis "See ORNL-TM-728 drawing"

**Item:** CRS-007, Regulating rod drive assembly (rack & pinion)  
**Issue:** The BOM specification states "Custom assembly; see ORNL-TM-728 drawing." ORNL-TM-728
is a 1964 ORNL internal report. The drawings from this report are not included in this repository
and are not publicly available in electronic form as fabrication drawings. A modern fabricator
cannot procure or fabricate this assembly using only a 60-year-old ORNL report reference.

**Recommended action:** The drive assembly specification must be expanded to include:
- Functional requirements: travel 508 mm, speed 0.1–2.5 mm/s, position accuracy ±0.2 mm
- Interface dimensions: shaft diameter, nozzle flange bolt circle, housing OD
- Environmental requirements: temperature at seal (~200°C), radiation dose rate
- These are the minimum requirements for a vendor to design a compliant assembly to modern standards.

### 🟠 SIGNIFICANT — CRS-002: Pellet Count Inconsistency

**Item:** CRS-002, Gd₂O₃/Al₂O₃ poison pellets  
**Issue:** BOM quantity shows "~110 per rod" but the notes state "1422 mm active stack height
needs ~112 pellets." With pellet height = 12.7 mm: 1422 / 12.7 = 111.97 → **112 pellets**,
not 110. The BOM quantity field should state "112 per rod" for accurate procurement (3 rods ×
112 = 336 total pellets, plus spares).

### 🟡 MINOR — CRS-001: Inconel 625 vs. Hastelloy-N for Absorber Tube

**Item:** CRS-001, Control rod absorber tube, Inconel 625  
**Issue:** Inconel 625 (UNS N06625) is specified for the absorber tube. The tube is inside the
Hastelloy-N thimble and does not contact fuel salt. Inconel 625 is acceptable for this
application (no salt contact, temperatures ~200°C max in thimble). However, the `review-materials`
SKILL notes: "is there a clear specification or procurement standard referenced?" ASTM B446 is
listed, which is correct for Inconel 625 seamless tube. ✓

The minor issue is that no irradiation embrittlement data is referenced for Inconel 625 in the
thimble environment. At the fast neutron fluence expected in the thimble (~10²¹ n/cm² over MSRE
lifetime), Inconel 625 irradiation behaviour should be documented as an open item.

---

## Component 10 — Reactor Cell

**Agents:** `review-safety`  
**BOM file:** `components/10_reactor_cell/bom.csv` (16 line items)

### Safety Review (`review-safety`)

- ✅ **Biological shielding:** RCL-001, baritic concrete up to 2440 mm thick for side walls. Adequate for gamma attenuation from 8 MWt core.
- ✅ **Inert atmosphere:** RCL-009/RCL-010/RCL-011, N₂ supply manifold + O₂ and dew point analyzers. Complete system for N₂ cell atmosphere.
- ✅ **Cell negative pressure:** RCL-013, cell differential pressure transmitter, −25 to −75 Pa range. Correct for contamination control.
- ✅ **Lead glass windows:** RCL-005, 600 mm equivalent lead glass, density ≥4.8 g/cc. Adequate for visual inspection during shutdown.

### 🟠 SIGNIFICANT — RCL-008: Crane Capacity Insufficient

**Item:** RCL-008, Overhead bridge crane, 10-tonne SWL  
**Issue:** The validation report (`docs/validation_report.md`) confirms the loaded vessel weight
is approximately 10,065 kg. A 10-tonne (10,000 kg) crane operating at 100.65% of its Safe
Working Load has zero margin. Nuclear facility overhead cranes typically require a minimum
safety factor of 1.25× the maximum working load (ASME B30.2).

Maximum lift weight ~10,065 kg → Required SWL ≥ 10,065 × 1.25 = **12,582 kg → specify 15-tonne crane**.

Additionally, the crane must accommodate slings, spreader bar, and any rigging hardware
(typically 200–400 kg), further reducing the effective working load of a 10-tonne crane.

**Recommended action:** Increase crane SWL specification to minimum 15 tonnes. Confirm maximum
single-lift weight including rigging hardware.

### 🟠 SIGNIFICANT — RCL-002: Removable Roof Sections Not in BOM

**Item:** RCL-002, Reactor cell roof slab  
**Issue:** RCL-002 notes "removable sections over reactor vessel for head removal" but there
are no separate BOM line items for the removable plug sections (number of plugs, dimensions,
weight, handling provisions). In an operating reactor cell, the removable roof plugs are
major structural and shielding elements that require individual fabrication specifications.
Without separate BOM items, these components have no procurement specification.

**Recommended action:** Add BOM line items for:
- Removable roof plug sections (quantity, dimensions, weight, concrete specification)
- Plug lifting hardware (embedded lifting lugs, rated for plug weight × 2)
- Plug seating/gasketing specification (for N₂ atmosphere integrity at joints)

### 🟡 MINOR — RCL-001: Wall Thickness Range Without Calculation Reference

**Item:** RCL-001, Primary shielding wall, thickness "1524–2440 mm"  
**Issue:** The BOM correctly notes "thickness per radiation transport calculation" but does not
cite the specific calculation document. For nuclear facility licensing, the shielding calculation
document number and revision should be traceable from the BOM.

---

## Component 11 — Coolant Radiator

**Agents:** `review-materials`  
**BOM file:** `components/11_coolant_radiator/bom.csv` (12 line items)

### Materials Review

- ✅ **All salt-wetted components:** RAD-001 through RAD-005, RAD-010–RAD-012, Hastelloy-N, ASTM B622. Correct for LiF-BeF₂ coolant salt at 546–621°C.
- ✅ **Fin material:** RAD-001, Hastelloy-N ASTM B622 strip for fins. Correct — same alloy avoids galvanic corrosion between tube and fin.
- ✅ **Fans:** RAD-007, 2 operating + 2 standby with individual dampers. Adequate redundancy for safety-related air flow.
- ✅ **Dampers fail-closed:** RAD-009, "fail-closed on loss of power." Retains heat in system on power loss, protecting salt from freezing. ✓
- ✅ **Heat trace:** RAD-012, MI cable rated 650°C, applied to all tubes and headers. Correct for freeze prevention.

### 🟡 MINOR — RAD-001: Fin Attachment Method — Brazing Filler Not Specified

**Item:** RAD-001, Finned tube, "high-frequency resistance welding or brazing"  
**Issue:** "Or brazing" implies brazing is an acceptable alternative to HFR welding. For
Hastelloy-N, brazing requires a filler metal compatible with both Hastelloy-N and the fluoride
salt service. Ni-base brazing fillers (e.g., BNi-2, BNi-7) are typically used for Hastelloy-N
joints. However, the BOM does not specify the brazing filler composition or the resulting
joint strength requirements.

**Recommended action:** If brazing is to be an option, add a note specifying: brazing filler
grade (e.g., AWS A5.8 BNi-2 or BNi-7), joint clearance, brazing temperature, and minimum joint
shear strength. If HFR welding is the primary method, remove "or brazing" to eliminate ambiguity.

---

## Component 12 — Instrumentation & Control

**Agents:** `review-instrumentation`, `review-safety`  
**BOM file:** `components/12_instrumentation_control/bom.csv` (24 line items)

### I&C Review (`review-instrumentation`)

- ✅ **Temperature measurement:** IC-007 and IC-008, Type K TCs in Inconel sheaths, 58 total. Covers core in/out, HX, pump bowl, drain tanks, freeze valves, and vessel exterior.
- ✅ **Flow measurement:** IC-010 and IC-011, EM flowmeters with Hastelloy-N flow tubes and ceramic electrodes. Correct material selection for fuel and coolant salt service. Non-invasive approach avoids introducing non-Hastelloy-N wetted surfaces.
- ✅ **Neutron flux coverage:** IC-001 (startup BF₃), IC-002 (intermediate ion chambers), IC-003 (power range), IC-004 (independent safety fission chamber). Four flux ranges covered.
- ✅ **Level measurement:** IC-013 (pump bowl), IC-014 (drain tanks). Hastelloy-N wetted diaphragm, appropriate for fluoride salt.
- ✅ **Safety relay panel:** IC-020, hardwired SIL-2 relay panel, independent of DCS. Correct nuclear safety architecture.

### 🔴 CRITICAL — IC: No Tritium Monitoring System

**Issue:** As identified in the Off-Gas BOM review (C-02), the MSRE generates tritium from
⁶Li + n and ternary fission. The I&C BOM contains 24 line items covering all standard nuclear
process instruments but includes no tritium monitoring equipment anywhere in the system.

Per `review-instrumentation` SKILL Step 6 ("Tritium Monitoring System Review"):
- [ ] Are tritium monitors specified at the primary off-gas system? **NO**
- [ ] Are tritium monitors at building ventilation exhaust? **NO**
- [ ] Are tritium monitors at the stack? **NO** (OGS-011 is a gamma/beta radiation monitor, not
  a tritium-specific monitor)
- [ ] Is there a tritium removal system for the off-gas? **NO**

This is a regulatory-disqualifying omission. No regulatory body would approve operation of an
MSR with a tritium-bearing salt loop without tritium effluent monitoring.

**Recommended action:** Add BOM entries for a minimum tritium monitoring suite:
- IC-0XX: Tritium-in-air monitor × 2 (off-gas exhaust and building ventilation)
  Specification: ionization chamber type; range 10⁻³ to 10³ µCi/m³; 4–20 mA output
- IC-0XX: Tritiated water monitor × 1 (cooling water return from heat exchangers)
  Specification: liquid scintillation flow counter or electrolytic enrichment + ionization chamber
- IC-0XX: Stack tritium monitor × 1

Cross-reference: OGS BOM also needs catalytic oxidizer and cold trap (see C-02 finding).

### 🟠 SIGNIFICANT — IC-007/IC-008: Type K TC Sheath Material — Fluoride Compatibility

**Items:** IC-007 and IC-008, Type K thermocouples with Inconel 600 sheath  
**Issue:** Per `review-instrumentation` SKILL Step 2 ("Thermocouple Selection for Salt Service"):

> Chromel (Ni-10%Cr alloy, positive element of Type K) is "Not suitable — Cr oxidizes in
> fluoride salt environment." Type K thermocouples in Inconel 600 sheaths are used in
> gas-phase and non-salt applications, but the MSRE operating environment exposes TC sheaths to:
> - Salt vapors at pump bowl, HX, and vessel exit temperatures (~640°C)
> - Salt contact in the case of any sheath pinhole

Inconel 600 contains 14–17% Cr — subject to Cr leaching in fluoride salt service. For salt-contact
or salt-adjacent applications, the correct sheath material is either:
- Hastelloy-N (UNS N10003, low Cr ~7%) — preferred
- Molybdenum or nickel — acceptable for specific cases

The BOM specifies 30 thermocouples at IC-007 and 28 at IC-008 (58 total). Not all of these
are in salt-contact positions, but the BOM does not distinguish which TCs are salt-wetted vs.
gas-phase vs. ambient-temperature locations.

**Recommended action:** Classify TCs by service:
- Salt-wetted or salt-adjacent (core inlet/outlet, pump bowl, HX salt-side): specify
  Hastelloy-N sheath, Type N element, or protected element
- Gas phase or ambient (cell exterior, freeze valve exterior): Inconel 600 sheath is acceptable

### 🟠 SIGNIFICANT — IC-001: Startup Channel Redundancy

**Item:** IC-001, BF₃ proportional counter, "2 redundant startup-range channels"  
**Issue:** For nuclear reactor startup, IEC 61513 and IAEA NS-G-1.3 recommend a minimum of
3 independent safety channels for any safety-relevant measurement (to support 2-of-3 trip
logic without disabling protection during a single channel failure for testing). Providing
only 2 startup-range channels means that any single channel failure during startup either:
(a) forces operation with degraded flux monitoring, or (b) forces a shutdown.

**Recommended action:** Add a third BF₃ startup-range channel (quantity from 2 to 3 on IC-001)
with a corresponding third dry-well (IC-005 qty from 8 to 10). Update IC-020 safety relay panel
specification to accommodate 3-channel 2-of-3 trip logic for startup-range channels.

### 🟠 SIGNIFICANT — IC-020: Trip Voting Logic Not Specified

**Item:** IC-020, Safety system relay panel  
**Issue:** The BOM notes "redundant 1oo2 or 2oo3 voting." For a nuclear safety system, the
trip logic must be specified definitively — "or" is not acceptable in a procurement document.
- 1oo2 (one-out-of-two) is more sensitive but gives higher spurious trip rate
- 2oo3 (two-out-of-three) is more common for nuclear protection systems (NRC RG 1.53)

The voting architecture determines the panel design (relay count, test provisions, channel
independence). A procurement document with "or" in the logic specification will result in a
vendor-determined design that may not meet the final design intent.

**Recommended action:** Specify "2-of-3 voting for SCRAM trip parameters where 3 measurement
channels exist; 1-of-2 for parameters where only 2 channels are installed, pending upgrade to
3 channels." Remove the "or" from IC-020.

---

## Cross-Cutting Findings

The following issues span multiple components and are captured here for completeness:

### XC-01 — Tritium Monitoring Gap (Components 08 and 12) 🔴 CRITICAL

Both the Off-Gas BOM (OGS) and the I&C BOM (IC) completely omit tritium monitoring and control
equipment. This is a systematic gap that affects the reactor's ability to meet regulatory tritium
effluent limits. The combined recommendation from findings C-02 and C-03 requires:

1. **Off-gas tritium control train** (Component 08):
   - Catalytic oxidizer (HT → HTO), ~150°C, Pt catalyst
   - Cold trap or desiccant bed for HTO capture
   - Tritium-in-gas monitor at inlet and outlet of control train

2. **Tritium monitoring network** (Component 12):
   - Off-gas system tritium monitor
   - Building ventilation tritium monitor
   - Stack tritium effluent monitor
   - Coolant system tritium monitor (leak detection through HX)

3. **Tritium waste management** (no current component):
   - Tritiated water disposal pathway
   - HTO accumulator/sampling system

### XC-02 — Duplicate Core Grid Plates (Components 01 and 02) 🟠 SIGNIFICANT

RV-012/RV-013 (Vessel BOM) and RC-005/RC-006 (Core BOM) specify identical grid plates.
This must be resolved to avoid double procurement. Recommended: remove from Vessel BOM,
retain in Core BOM only.

### XC-03 — No Master BOM or Parts Count Roll-Up

The 12 individual BOMs have no cross-reference master BOM that totals quantities across
components. For example, the total quantity of Hastelloy-N ASTM B622 pipe across all components
is not calculable without manual summation. For procurement efficiency and material tracking,
a master BOM roll-up (or a simple Python/spreadsheet aggregation script) should be added to
the repository.

---

## Recommended Actions by Priority

### Immediate (before any procurement)

| # | Component | Item | Action |
|---|-----------|------|--------|
| 1 | 06 FDT | FDT-006 | Specify minimum B₄C mass from criticality safety analysis |
| 2 | 08 OGS | New items | Add tritium control train to off-gas BOM |
| 3 | 12 I&C | New items | Add tritium monitoring suite to I&C BOM |
| 4 | 01 Vessel | RV-016 | Correct stud specification from A193 B8 to ASTM B574 UNS N10003 |
| 5 | 01/02 | RV-012/013 | Resolve grid plate duplication with RC-005/006 |
| 6 | 05 CSP | CSP-008 | Resolve bearing bore vs. shaft diameter mismatch |
| 7 | 03 PHX | PHX-009 | Recalculate baffle count at 203 mm spacing (22 → 25) |

### Before Detail Design Sign-Off

| # | Component | Item | Action |
|---|-----------|------|--------|
| 8 | 02 Core | RC-001/002 | Verify stringer counts against ORNL-TM-728 Table 3.1 |
| 9 | 07 FZV | FZV-001 | Define FV-104 function or remove from BOM |
| 10 | 07 FZV | FZV-008 | Add TC replacement interval; consider Type N or Hastelloy-N sheath |
| 11 | 09 CRS | CRS-007 | Expand drive assembly spec beyond ORNL-TM-728 reference |
| 12 | 09 CRS | CRS-002 | Correct pellet count from ~110 to 112 per rod |
| 13 | 10 Cell | RCL-008 | Increase crane SWL from 10 to ≥15 tonnes |
| 14 | 10 Cell | RCL-002 | Add separate BOM items for removable roof plug sections |
| 15 | 12 I&C | IC-001 | Increase startup channel count from 2 to 3 |
| 16 | 12 I&C | IC-020 | Specify definitive trip voting logic (remove "or") |
| 17 | 12 I&C | IC-007/008 | Classify TCs by service; specify Hastelloy-N sheath for salt-adjacent |

### Before Final BOM Release

| # | Action |
|---|--------|
| 18 | Produce master BOM roll-up spreadsheet across all 12 components |
| 19 | Resolve RC-010 furfuryl alcohol hazmat classification |
| 20 | Add procurement notes for PHX-002 total tube length |

---

## Agent Review Sign-Off

| Agent | Skill Version | Status |
|-------|--------------|--------|
| `review-reactor-design` v1.0.0 | Applied to Components 01, 02, 03, 09 | Complete |
| `review-materials` v1.0.0 | Applied to all 12 components | Complete |
| `review-safety` v1.0.0 | Applied to Components 06, 07, 09, 10 | Complete |
| `review-instrumentation` v1.0.0 | Applied to Components 07, 08, 12 | Complete |
| `review-salt-chemistry` v1.0.0 | Applied to Components 01, 03, 04, 05, 06 | Complete |
| `review-fuel-cycle` v1.0.0 | Applied to Components 02, 08 | Complete |

Not invoked for this BOM-focused review: `plan-program-review`, `plan-cto-review`, `retro-rd`.
