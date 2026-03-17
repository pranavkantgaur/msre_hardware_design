# MSRE CAD Review Report

**Date:** 2025-07-16
**Reviewer:** msr-gstack multi-agent system (Reactor Design / Safety / Materials / I&C skills)
**Components Reviewed:** 01–12 (all)
**CAD Scripts Location:** cad/scripts/

---

## Executive Summary

Review of all 12 CAD scripts against the corresponding `specifications.md` and `bom.csv` files
identified 14 CRITICAL findings including wrong pump bowl heights driven by
assignment of shaft-length values, a 10× fin-pitch error on the coolant radiator, an absent
main fuel drain tank (script models the overflow tank instead), tube-pitch and tube-sheet
thickness errors in the primary heat exchanger, and missing tritium monitors in the I&C assembly.
Eight SIGNIFICANT and three MINOR findings were also recorded.
All CRITICAL items must be corrected before the CAD models are used for fabrication, shielding
analysis, or procurement.

---

## 1. Reactor Design Skill Review

### 1.1 Reactor Vessel (01\_reactor\_vessel.py)

**CRITICAL — RD-01: Ellipsoidal head crown depth uses OD/4 instead of ID/4**

For a 2:1 semi-ellipsoidal head the depth of the inner (pressure-boundary) surface is ID/4,
not OD/4.

- CAD: `H_OUTER = OD / 4 = 1410 / 4 = 352.5 mm`
- Specification (§1): "head depth ≈ ID/4 = 346 mm"
  (ID = OD − 2 × WT = 1410 − 25.4 = 1384.6 mm; ID/4 = 346.15 mm)
- Error: 352.5 − 346.15 = 6.35 mm = **+1.8 %** (exceeds 1 % threshold)

An overcalculated crown depth inflates the modelled head volume and the computed total
assembled height, affecting nozzle-elevation datums for all connected piping.

**SIGNIFICANT — RD-02: Missing upper-head flange and bolt pattern**

The upper-head straight flange (76.2 mm), flange OD (1460 mm), 24 × M32 stud holes,
and nickel O-ring groove are absent. These features drive nozzle stand-out dimensions
and crane-lift rigging calculations. Specification §1 table and BOM items RV-003/RV-004/RV-014.

**SIGNIFICANT — RD-03: Missing vessel internals — TC nozzles, neutron source, lower plenum
distributor, and support skirt**

BOM items RV-009 (10× TC nozzles), RV-010 (neutron source nozzle), RV-011 (lower plenum
distributor plate ∅1380 mm), and RV-012 (support skirt ∅700 OD × 400 mm height) are all
absent from the CAD model.

### 1.2 Reactor Core (02\_reactor\_core.py)

**SIGNIFICANT — RD-04: Representative 5 × 5 stringer sub-array only**

The script explicitly notes this simplification (comment: "full 509-stringer array is too heavy
for a reference model"). The representative geometry is acceptable for a reference render but
must not be used for any spacing, pressure-drop, or neutronics mesh work.

**SIGNIFICANT — RD-05: Fuel channel modelled as circular bore (FUEL\_CH = 12.7 mm dia)**

Specification §2 defines cruciform semi-circular grooves on each stringer face:

- Zone I: 6.35 mm wide × 3.18 mm deep per face
- Zone II: 4.75 mm wide × 2.38 mm deep per face

The actual inter-stringer channel is non-circular. A cylindrical bore approximation distorts
flow-area and wetted-perimeter calculations.

**SIGNIFICANT — RD-06: Control rod thimbles absent from core assembly**

BOM item RC-004 specifies 3 × Hastelloy-N thimbles (44.45 mm OD × 3.18 mm wall × 1727 mm).
None are included in `02_reactor_core.py`, preventing thimble-to-stringer clearance verification.

### 1.3 Primary Heat Exchanger (03\_primary\_heat\_exchanger.py)

**CRITICAL — RD-07: Tube pitch 15.9 mm vs specification 12.7 mm (25.2 % error)**

- CAD: `TUBE_PITCH = 15.9 mm` (script comment: "≈ 1.67 × OD")
- Specification §5 (Tubes): "Tube pitch: 12.7 mm triangular"
- BOM PHX-003: tube holes "on 12.7 mm pitch"
- Error: (15.9 − 12.7) / 12.7 = **+25.2 %**

At 15.9 mm pitch the script can fit only 159 tubes if the tube-sheet OD (444 mm ID) is
respected, whereas 12.7 mm pitch would pack the same count with significantly reduced
tube-sheet area, changing the LMTD and velocity calculations.

**CRITICAL — RD-08: Tube-sheet thickness 38.1 mm vs specification 63.5 mm (40 % error)**

- CAD: `TS_THICK = 38.1 mm` (corresponds to 1.5 in; no basis for this value)
- Specification §5 (Tube Sheet): "Thickness: 63.5 mm (2.5 in)"
- BOM PHX-003/PHX-004: "63.5 thk"
- Error: (63.5 − 38.1) / 63.5 = **−40 %**

Under-thickness tube-sheets cannot sustain the full-penetration strength-weld loads specified
for 159 tube joints and will produce incorrect assembly length models.

**CRITICAL — RD-09: Tube wall 0.875 mm vs specification 0.889 mm (1.6 % error)**

- CAD: `TUBE_WT = 0.875 mm`
- Specification §5 (Tubes): "Tube wall: 0.889 mm (0.035 in)"; BOM PHX-002: "0.889 wall"
- Error: (0.889 − 0.875) / 0.889 = **−1.6 %**

The nominal wall for 3/8-in × 0.035-in ASTM B622 tube is 0.889 mm. Even a small wall
error affects tube-side pressure rating and corrosion-allowance calculations.

**SIGNIFICANT — RD-10: Baffles absent; only 12 of 159 tubes represented**

Specification §3 calls for 25 segmental baffles (25 % cut, 440 mm dia, 6.35 mm thick,
203 mm spacing). The model uses no baffles and only 12 representative tubes. Shell-side
velocity and pressure-drop verification is not possible from this model.

### 1.4 Fuel Salt Pump (04\_fuel\_salt\_pump.py)

**CRITICAL — RD-11: Bowl height 1829 mm vs specification / BOM 609.6 mm (+200 % error)**

The variable `BOWL_H = 1829.0` has been set to the pump shaft total length, not the bowl height.

- CAD: `BOWL_H = 1829.0 mm`
- Specification §3 (Pump Bowl): "Height: 609.6 mm (24.0 in)"
- BOM FSP-001: "609.6 OD, 9.53 wall, 609.6 ht"
- Correct shaft length: specification §4: "Total length: 1,829 mm" (matches BOM FSP-004: "1829 lg")
- Error: (1829 − 609.6) / 609.6 = **+200 %**

The entire pump model (bowl, impeller position, shaft, neck, nozzle) is geometrically invalid
because of this root-cause assignment error.

### 1.5 Coolant Salt Pump (05\_coolant\_salt\_pump.py)

**CRITICAL — RD-12: Bowl height 1524 mm vs specification / BOM 457 mm (+233 % error)**

The same error pattern as the fuel pump:

- CAD: `BOWL_H = 1524.0 mm`
- Specification §3 (Pump Bowl): "Height: 457 mm (18.0 in)"
- BOM CSP-001: "457 OD, 7.94 wall, 457 ht"
- Correct shaft length: specification §4: "Total length: 1,524 mm" (BOM CSP-004: "1524 lg")
- Error: (1524 − 457) / 457 = **+233 %**

**CRITICAL — RD-13: Shaft diameter 44.45 mm vs BOM 40 mm (spec table 38.1 mm)**

- CAD: `SHAFT_D = 44.45 mm`
- BOM CSP-004: shaft diameter revised to "40 dia" (note: "revised from 38.1 mm to match
  standard metric bearing bore SKF 6308, 40 mm bore")
- Specification §4 table: "Diameter (submerged): 38.1 mm"
- Neither authoritative value (38.1 mm spec text or 40 mm BOM revision) matches CAD 44.45 mm
- Error vs BOM: (44.45 − 40) / 40 = **+11.1 %**

### 1.6 Fuel Drain Tank (06\_fuel\_drain\_tank.py)

**CRITICAL — RD-14: Script models Overflow Tank (OFT) geometry, not the Main Fuel Drain Tank**

The script title and docstring say "Fuel Drain Tank" but every key dimension matches the
Overflow Tank (OFT) listed in specification §4, not the Main FDT:

| Parameter | CAD script | Main FDT (BOM FDT-001/002) | OFT (Spec §4 / BOM FDT-013/014) |
| --- | --- | --- | --- |
| Outer OD | 610 mm | 1219 mm | 610 mm |
| Height | 762 mm | 1524 mm | 762 mm |
| Inner column OD | 304 mm | 914 mm (FDT-002) | 304 mm (FDT-014) |

The Main FDT (OD 1219 mm, H 1524 mm) holds the full primary loop inventory (~1993 L) and
is the primary passive drain safety system. Modelling only the OFT leaves the principal
criticality-safety vessel unrepresented.

**CRITICAL — RD-15: OFT annular salt layer 143 mm vs specification 128 mm (criticality safety)**

Even for the OFT that the script does model, the computed salt layer does not match the spec:

- Script: OUTER\_OD=610 mm, OUTER\_WT=9.53 mm → outer ID = 590.94 mm; INNER\_OD=304 mm
  → salt annulus = (590.94 − 304) / 2 = **143 mm**
- Specification §4 (OFT): "Annular salt thickness: 128 mm (5 in)"
- BOM FDT-013: outer WT = 7.94 mm (not 9.53 mm)
  → correct outer ID = 610 − 2×7.94 = 594.12 mm
  → correct salt annulus = (594.12 − 304) / 2 = **145 mm** (still ≠ 128 mm)

The annular geometry is the primary criticality-safety control. A 12–15 mm excess salt
thickness above the design basis could push k-eff beyond the accepted limit under
worst-case moderation scenarios.

### 1.7 Freeze Valves (07\_freeze\_valves.py)

**SIGNIFICANT — RD-16: Only one generic spool piece modelled; three distinct valve types required**

Specification §2–§3 and BOM FZV-001 define three functionally distinct valves:

- FV-101: primary drain (de-energise-to-open)
- FV-103: fill valve (energise-to-open)
- FV-104: secondary drain isolation (series with FV-101; defence-in-depth)

A single generic spool piece cannot be used for routing or interlock verification.

**MINOR — RD-17: TC wells absent from freeze valve model**

Specification §3 (Thermocouple): 2 × Type-N TCs per valve (3.2 mm sheath). BOM FZV-008:
10 TCs total. Not represented in CAD.

### 1.8 Off-Gas System (08\_off\_gas\_system.py)

**SIGNIFICANT — RD-18: HEPA vessel dimensions match secondary cooled charcoal bed, not HEPA filter**

- CAD `make_hepa()`: `HEPA_ID = 500 mm`, `HEPA_H = 2400 mm`
- Specification §4 (Secondary Cooled Charcoal Bed): "500 mm ID × 2,400 mm length" ✓
- Specification §5 (HEPA Filter): element OD = 150 mm, element length = 250 mm (no housing
  OD/length matching 500 × 2400)

The vessel labelled "HEPA" is actually the secondary cooled Kr-retention bed. The true HEPA
housing dimensions are unspecified by the specs but are clearly not 500 mm × 2400 mm.

**SIGNIFICANT — RD-19: Tritium control train components excluded from final exported model**

`make_ogs()` assembles trap, two charcoal beds, and HEPA vessel but the `return` statement
discards all except `make_charcoal_bed()`. Components OGS-014 (catalytic oxidizer) and
OGS-015 (desiccant cold trap) — which the tritium control specifications (§8) explicitly
require — are neither modelled nor exported.

**MINOR — RD-20: Condensation trap orientation not reflected in final model**

The trap is assembled in `make_ogs()` with an X-offset of −1200 mm but is not in the
exported geometry. BOM items OGS-001 and OGS-002 should appear in the STEP output.

### 1.9 Control Rods (09\_control\_rods.py)

**SIGNIFICANT — RD-21: Rod placement radius 200 mm vs reactor vessel nozzle pattern 400 mm**

`make_control_rod_assembly()` places rods at r = 200 mm:

```python
x = 200 * math.cos(a); y = 200 * math.sin(a)
```

Script `01_reactor_vessel.py` places the three control-rod nozzles at r = 400 mm:

```python
x = 400 * math.cos(a); y = 400 * math.sin(a)
```

This 200 mm offset mismatch means a combined assembly model would show rods not aligned
with the vessel penetrations.

### 1.10 Reactor Cell (10\_reactor\_cell.py)

**CRITICAL — RD-22: Roof thickness 1520 mm vs specification 2440 mm (−37.7 % shielding deficit)**

- CAD: `ROOF_T = 1520 mm` (uniform for all surfaces)
- Specification §1 (Shielding Dimensions): "Roof/ceiling: 2.44 m" and
  "Side walls adjacent to reactor vessel: 2.44 m"
- The minimum 1.52 m applies only to far side-walls
- Error on roof: (2440 − 1520) / 2440 = **−37.7 %**

With 1520 mm roof concrete (μ = 0.048 cm⁻¹ for 2-MeV gamma in baritic concrete):
attenuation = e^(−0.048 × 152) ≈ e^(−7.3) = ~6.7 × 10⁻⁴, giving ~6 HVLs.
The specification requires >10 HVLs. This is a safety-critical shielding shortfall.

### 1.11 Coolant Radiator (11\_coolant\_radiator.py)

**CRITICAL — RD-23: Fin pitch 25.4 mm vs specification 2.5 mm (factor of 10 error)**

- CAD: `FIN_PITCH = 25.4 mm` (script docstring also states "fin pitch ~25 mm")
- Specification §3 (Fin Specifications): "Fin pitch: 4 fins/cm (10 fins/in)" = **2.54 mm pitch**
- BOM RAD-001: "4 fins/cm"
- Error factor: 25.4 / 2.54 = **10×**

At 25.4 mm pitch the tube effective surface area is reduced by a factor of ~10, making the
modelled radiator grossly insufficient for the 7.34 MWt design duty. Any heat-transfer area
calculation using this model would produce completely erroneous results.

**SIGNIFICANT — RD-24: 8 representative tubes vs specification / BOM 144 tubes**

Specification §2: "Total tubes: 144". BOM RAD-001: quantity 144. CAD: `N_TUBES = 8`.
Tube-bundle face area and pressure-drop calculations require the full-count model.

### 1.12 I&C Assembly (12\_instrumentation\_control.py)

Dimensional checks on represented components:

- EM flowmeter body OD 114.3 mm ✓ (spec, SKILL.md, BOM IC-010)
- Dry-well thimble OD 50.8 mm (spec §1 and SKILL.md; note BOM IC-005 discrepancy below)
- Dry-well length 1000 mm ✓ (spec §1, BOM IC-005)
- TC sheath OD 3.2 mm ✓ (BOM IC-007, SKILL.md)
- Flange OD 165.1 mm: no specification conflicts found

---

## 2. Safety Skill Review

**CRITICAL — SAF-01: Reactor cell roof thickness below minimum required shielding**

(See RD-22.) Roof modelled at 1520 mm; specification requires 2440 mm. The modelled geometry
does not provide the minimum >10-HVL attenuation required at the cell exterior for a 10⁶ Ci
fission-product source term.

**CRITICAL — SAF-02: Fuel Drain Tank not modelled — primary passive drain safety vessel absent**

(See RD-14.) The script `06_fuel_drain_tank.py` models the OFT geometry, not the FDT.
The FDT (OD 1219 mm, H 1524 mm) is the principal passive-drain criticality-safety vessel.
Its absence from the CAD set means drain-line routing, FV-101 / FV-104 freeze-valve placement,
and FDT-cell clearance cannot be verified.

**CRITICAL — SAF-03: OFT annular salt layer exceeds criticality-safe design basis**

(See RD-15.) The script gives a 143 mm annular salt layer; the specification basis (128 mm)
is derived from criticality analysis (k-eff < 0.95 under worst-case flooding). Excess salt
thickness could push k-eff above 0.95. BOM note FDT-006: "QA HOLD POINT — do not close
centre column without QA sign-off confirming as-installed mass."

**CRITICAL — SAF-04: Control rod absorber composition wrong in CAD documentation**

(See MAT-02.) The script docstring states "B₄C / Al₂O₃ pellets". Both the specification (§1)
and BOM (CRS-002) state Gd₂O₃/Al₂O₃ (50 %/50 % by weight). B₄C and Gd₂O₃ are
fundamentally different absorbers with different cross-sections and burnup behaviour.
A fabricator relying on the docstring would produce rods with the wrong reactivity worth.

**CRITICAL — SAF-05: Tritium monitors IC-025/026/027 absent from I&C model**

(See IC-01.) SKILL.md explicitly states: "Tritium monitors (IC-025, IC-026, IC-027): present in
I&C assembly geometry." BOM entries IC-025 (2 ea), IC-026 (1 ea), IC-027 (1 ea) are defined.
These monitors are a regulatory compliance requirement (10 CFR 20 / IAEA BSS) and their
positions must appear in the CAD for routing, penetration seal design, and dose assessment.

**SIGNIFICANT — SAF-06: Only one freeze valve spool piece modelled; FV-104 defence-in-depth
valve absent**

(See RD-16.) Specification §2 (FV-104) explicitly states that the series-redundant drain
isolation valve FV-104 "provides defence-in-depth for passive drain actuation." A single
spool-piece model cannot support safety-system layout review or single-failure analysis.

---

## 3. Materials Skill Review

**CRITICAL — MAT-01: Control rod cladding material wrong in CAD docstring**

- CAD docstring: "Three Hastelloy-N clad control rods"
- Specification §2 (Absorber Tube): "Clad material: Inconel 625 (UNS N06625)"
- BOM CRS-001: "Inconel 625, ASTM B446; UNS N06625; seamless tube"

Hastelloy-N (N10003) and Inconel 625 (N06625) have significantly different compositions
(Mo content, Nb content, corrosion-fatigue behaviour) and are not interchangeable.
A STEP file generated from this script would tag the material as Hastelloy-N, misleading
procurement and QA.

**CRITICAL — MAT-02: Control rod absorber composition wrong in CAD docstring**

- CAD docstring: "B₄C / Al₂O₃ pellets"
- Specification §1 and BOM CRS-002: "Gd₂O₃/Al₂O₃ co-sintered; 50 % Gd₂O₃ + 50 % Al₂O₃"

Boron carbide and gadolinium oxide have entirely different neutron absorption cross-sections.
Specifying B₄C where Gd₂O₃ is required would result in rods with incorrect reactivity worth.

**SIGNIFICANT — MAT-03: BOM / spec inconsistency on dry-well tube OD (IC-005)**

- Specification §1: dry-well tube OD = 50.8 mm (SKILL.md also states 50.8 mm)
- BOM IC-005: "44.5 mm OD × 3.18 mm wall × 1000 mm long"

The CAD uses 50.8 mm, consistent with the specification. The BOM discrepancy must be
resolved before procurement to ensure detectors fit. The BOM value (44.5 mm) may reflect
a more recent ORNL standard tube that was not propagated into the spec.

**SIGNIFICANT — MAT-04: PHX tube wall 0.875 mm rather than 0.889 mm**

(See RD-09.) The standard ASTM B622 3/8-in × 0.035-in seamless tube wall is 0.889 mm.
The CAD value of 0.875 mm (0.0345 in) is not a catalogued ASTM product dimension and would
not be procurable to that exact thickness.

**SIGNIFICANT — MAT-05: FDT outer-wall thickness 9.53 mm vs BOM OFT value 7.94 mm**

BOM FDT-013 specifies the OFT outer shell at 7.94 mm wall. The CAD uses 9.53 mm (the FDT
main vessel wall). While this is conservative for pressure containment, it produces the
wrong annular salt layer dimension (criticality-safety implication per SAF-03).

---

## 4. I&C Skill Review

**CRITICAL — IC-01: Tritium monitors IC-025, IC-026, IC-027 not present in I&C assembly geometry**

`make_ic_assembly()` renders only the EM flowmeter, dry-well, TC sheath, and pressure
transmitter. The three tritium monitoring instruments mandated by SKILL.md are absent.
These monitors must appear as positioned geometry to support:

- Cell-wall penetration seal design (IC-024 routing)
- Off-gas system interface (IC-025A ties to OGS-015 outlet)
- Dose-rate assessment around their deployment locations

**SIGNIFICANT — IC-02: EM flowmeter flange OD 165.1 mm lacks specification basis**

`FLANGE_OD = 165.1 mm` is coded without a reference. For a 4-in Schedule 40 line at 345 kPa /
704 °C service, the appropriate ASME B16.5 Class 300 flange (4-in) has an OD of ~273 mm
(raised face). The value 165.1 mm (6.5 in) appears to be Class 150 which is under-rated for
salt service. Specification §3 does not define flange class; BOM IC-010 does not give flange
OD — this must be resolved.

**SIGNIFICANT — IC-03: Pressure transmitter body (PT\_OD = 76.2 mm) modelled without wetted
diaphragm geometry**

SKILL.md specifies: "Pressure transmitters: diaphragm body geometry, Hastelloy-N wetted."
The model creates a plain cylinder without flush diaphragm. BOM IC-015 specifies a
Hastelloy-N wetted diaphragm; its geometry is needed for nozzle-interface verification.

---

## 5. Findings Summary Table

| ID | Script | Severity | Category | Description | Specification Value | CAD Value |
| --- | --- | --- | --- | --- | --- | --- |
| RD-01 | 01\_reactor\_vessel | CRITICAL | Dimensional | Head crown depth OD/4 vs ID/4 | 346.15 mm (ID/4) | 352.5 mm (OD/4) |
| RD-02 | 01\_reactor\_vessel | SIGNIFICANT | Feature | Upper-head flange, bolt circle, O-ring groove absent | 76.2 mm straight flange; 24× M32 holes | Not modelled |
| RD-03 | 01\_reactor\_vessel | SIGNIFICANT | Feature | TC nozzles, neutron-source nozzle, distributor plate, support skirt absent | BOM RV-009 to RV-012 | Not modelled |
| RD-04 | 02\_reactor\_core | SIGNIFICANT | Simplification | Only 5×5 representative stringer subarray | 509 full stringers (BOM RC-001/002) | 11×11 clipped subarray |
| RD-05 | 02\_reactor\_core | SIGNIFICANT | Dimensional | Fuel channel circular bore vs cruciform groove profile | Zone I: 6.35 mm × 3.18 mm groove per face | 12.7 mm cylindrical bore |
| RD-06 | 02\_reactor\_core | SIGNIFICANT | Feature | Control rod thimbles absent from core model | 3× 44.45 mm OD × 1727 mm (BOM RC-004) | Not modelled |
| RD-07 | 03\_primary\_heat\_exchanger | CRITICAL | Dimensional | Tube pitch 25.2 % too large | 12.7 mm triangular | 15.9 mm |
| RD-08 | 03\_primary\_heat\_exchanger | CRITICAL | Dimensional | Tube-sheet thickness 40 % too thin | 63.5 mm | 38.1 mm |
| RD-09 | 03\_primary\_heat\_exchanger | CRITICAL | Dimensional | Tube wall 1.6 % below standard | 0.889 mm | 0.875 mm |
| RD-10 | 03\_primary\_heat\_exchanger | SIGNIFICANT | Simplification | No baffles; 12 of 159 tubes only | 25 baffles, 159 tubes | 0 baffles, 12 tubes |
| RD-11 | 04\_fuel\_salt\_pump | CRITICAL | Dimensional | Bowl height assigned shaft length | 609.6 mm (BOM FSP-001) | 1829.0 mm |
| RD-12 | 05\_coolant\_salt\_pump | CRITICAL | Dimensional | Bowl height assigned shaft length | 457 mm (BOM CSP-001) | 1524.0 mm |
| RD-13 | 05\_coolant\_salt\_pump | CRITICAL | Dimensional | Shaft diameter matches neither spec nor BOM | 40 mm (BOM CSP-004) | 44.45 mm |
| RD-14 | 06\_fuel\_drain\_tank | CRITICAL | Wrong component | Script models OFT (610 mm OD × 762 mm) not main FDT | FDT: 1219 mm OD × 1524 mm H (BOM FDT-001) | OFT: 610 mm × 762 mm |
| RD-15 | 06\_fuel\_drain\_tank | CRITICAL | Dimensional (safety) | OFT salt annulus 143 mm vs spec 128 mm | 128 mm (Spec §4) | 143 mm computed |
| RD-16 | 07\_freeze\_valves | SIGNIFICANT | Feature | Three valve types (FV-101/103/104) merged into one spool | FV-104 series isolation (Spec §2) | Single spool only |
| RD-17 | 07\_freeze\_valves | MINOR | Feature | TC wells absent from freeze valve model | 2× TC per valve (BOM FZV-008) | Not modelled |
| RD-18 | 08\_off\_gas\_system | SIGNIFICANT | Labelling | "HEPA" vessel (500 mm × 2400 mm) is secondary charcoal bed | HEPA element OD 150 mm × 250 mm (Spec §5) | 500 mm ID × 2400 mm |
| RD-19 | 08\_off\_gas\_system | SIGNIFICANT | Feature | Tritium control train (OGS-014/015) not exported | Required by Spec §8 | Built but discarded in return statement |
| RD-20 | 08\_off\_gas\_system | MINOR | Feature | Condensation trap built but not in exported model | BOM OGS-001/002 | Built, not exported |
| RD-21 | 09\_control\_rods | SIGNIFICANT | Dimensional | Rod PCD 200 mm vs vessel nozzle PCD 400 mm | r = 400 mm (01\_reactor\_vessel.py) | r = 200 mm |
| RD-22 | 10\_reactor\_cell | CRITICAL | Dimensional (safety) | Roof thickness 1520 mm vs required 2440 mm | 2440 mm (Spec §1) | 1520 mm |
| RD-23 | 11\_coolant\_radiator | CRITICAL | Dimensional | Fin pitch factor of 10 too large | 2.54 mm (4 fins/cm; BOM RAD-001) | 25.4 mm |
| RD-24 | 11\_coolant\_radiator | SIGNIFICANT | Simplification | 8 representative tubes vs 144 design total | 144 (Spec §2; BOM RAD-001) | 8 |
| MAT-01 | 09\_control\_rods | CRITICAL | Material | Clad material stated as Hastelloy-N; should be Inconel 625 | Inconel 625 UNS N06625 (Spec §2; BOM CRS-001) | "Hastelloy-N" in docstring |
| MAT-02 | 09\_control\_rods | CRITICAL | Material (safety) | Absorber stated as B4C/Al2O3; should be Gd2O3/Al2O3 | Gd2O3/Al2O3 50/50 wt% (Spec §1; BOM CRS-002) | "B4C/Al2O3" in docstring |
| MAT-03 | 12\_instrumentation\_control | SIGNIFICANT | BOM/spec conflict | Dry-well OD: spec 50.8 mm vs BOM IC-005 44.5 mm | Spec/SKILL.md: 50.8 mm; BOM IC-005: 44.5 mm | CAD: 50.8 mm (matches spec) |
| MAT-04 | 03\_primary\_heat\_exchanger | SIGNIFICANT | Dimensional | Tube wall not a catalogued ASTM product dimension | 0.889 mm (ASTM B622 3/8-in × 0.035-in) | 0.875 mm |
| MAT-05 | 06\_fuel\_drain\_tank | SIGNIFICANT | Dimensional | OFT outer-wall thickness wrong | 7.94 mm (BOM FDT-013) | 9.53 mm |
| SAF-01 | 10\_reactor\_cell | CRITICAL | Safety-shielding | Roof thickness below minimum (see RD-22) | 2440 mm | 1520 mm |
| SAF-02 | 06\_fuel\_drain\_tank | CRITICAL | Safety-criticality | Main FDT not modelled (see RD-14) | 1219 mm OD FDT required | OFT only |
| SAF-03 | 06\_fuel\_drain\_tank | CRITICAL | Safety-criticality | OFT annular salt layer exceeds design basis (see RD-15) | 128 mm | 143 mm |
| SAF-04 | 09\_control\_rods | CRITICAL | Safety-reactivity | Wrong absorber material in docstring (see MAT-02) | Gd2O3/Al2O3 | "B4C/Al2O3" |
| SAF-05 | 12\_instrumentation\_control | CRITICAL | Safety-monitoring | Tritium monitors absent from I&C model | IC-025/026/027 required | Not modelled |
| SAF-06 | 07\_freeze\_valves | SIGNIFICANT | Safety-passive | FV-104 defence-in-depth valve absent (see RD-16) | FV-104 in series (Spec §2) | Not modelled |
| IC-01 | 12\_instrumentation\_control | CRITICAL | I&C | Tritium monitors IC-025/026/027 absent (see SAF-05) | Present per SKILL.md | Not modelled |
| IC-02 | 12\_instrumentation\_control | SIGNIFICANT | I&C | Flowmeter flange OD lacks specification basis | ASME B16.5 Class 300 required | 165.1 mm (Class 150 equivalent) |
| IC-03 | 12\_instrumentation\_control | SIGNIFICANT | I&C | Pressure transmitter missing flush-diaphragm geometry | Hastelloy-N wetted diaphragm (SKILL.md) | Plain cylinder only |

---

## 6. Verified Correct Items

The following dimensions and features were checked and found correct:

- **01 Reactor Vessel:** Cylindrical shell OD 1410 mm, wall 12.7 mm, height 2134.6 mm; head
  thickness 19.05 mm; salt inlet/outlet nozzle 114.3 mm OD × 6.02 mm WT; control-rod nozzle
  60.3 mm OD × 3.91 mm WT; three nozzles at 120° spacing; material Hastelloy-N in all
  comments and BOM entries.

- **02 Reactor Core:** Active zone OD 1372 mm; active height 1626.4 mm; radial reflector
  thickness 76 mm; axial reflector thickness 152 mm; stringer cross-section 50.8 × 50.8 mm;
  pitch 53.85 mm; graphite grade AGOT throughout.

- **03 PHX:** Shell OD 457.2 mm; shell wall 6.35 mm; shell length 5029 mm; U-bend radius
  25.4 mm; shell-side nozzle 114.3 mm OD / 6.02 mm WT; tube-side nozzle 88.9 mm OD /
  5.49 mm WT (both match spec and BOM).

- **04 Fuel Salt Pump:** Bowl OD 609.6 mm; bowl WT 9.53 mm; impeller OD 203 mm; shaft
  diameter (submerged) 50.8 mm; discharge nozzle 114.3 mm OD / 6.02 mm WT; all
  Hastelloy-N materials.

- **05 Coolant Salt Pump:** Bowl OD 457 mm; bowl WT 7.94 mm; impeller OD 178 mm; discharge
  nozzle 88.9 mm OD / 5.49 mm WT; material Hastelloy-N.

- **06 Fuel Drain Tank (OFT):** Inner column OD 304 mm; drain/vent nozzle 60.3 mm OD /
  3.91 mm WT; B4C fill represented; head thickness 12.7 mm; all Hastelloy-N materials.

- **07 Freeze Valves:** Tube OD 60.3 mm; tube WT 3.91 mm; frozen section length 152 mm;
  all values match specification §3 and BOM FZV-001. Heater coil envelope 76.2 mm OD
  (no spec conflict).

- **08 Off-Gas System:** Primary charcoal bed vessel ID 450 mm, height 1600 mm;
  condensation trap inner tube 12.7 mm OD / 1.65 mm WT; outer tube 25.4 mm OD /
  2.41 mm WT — all match specification §2 and §3.

- **09 Control Rods:** Clad OD 25.4 mm; clad WT 1.65 mm; active length 1422 mm; total
  rod length 1448 mm; drive housing OD 73 mm; drive shaft diameter 19.05 mm; pellet
  OD 23.6 mm; pellet height 12.7 mm — all match specification.

- **10 Reactor Cell:** Minimum wall thickness 1520 mm (matches far-wall minimum);
  internal clear height computed as 8000 − 600 − 1520 = 5880 mm ≈ 5.5 m spec value.
  Crane modelled at correct bay height.

- **11 Coolant Radiator:** Tube OD 25.4 mm; fin OD 50.8 mm; fin thickness 0.889 mm;
  header wall thickness 9.53 mm; inlet/outlet nozzle 88.9 mm OD / 5.49 mm WT — all match.

- **12 I&C Assembly:** EM flowmeter body OD 114.3 mm; dry-well OD 50.8 mm; dry-well
  length 1000 mm; dry-well wall 3.18 mm; TC sheath OD 3.2 mm — all match specification
  and SKILL.md requirements.
