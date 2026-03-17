# Brainstorm: Using openmsr/msre as a Validation Source for CAD Drawings

**Date:** 2026-03-17  
**Scope:** How `https://github.com/openmsr/msre` can cross-validate the parametric CAD
models in `cad/scripts/` and the dimensional specifications in `components/*/specifications.md`.

---

## 1. What openmsr/msre Contains (Inventory)

| Asset | Location | Relevance |
|-------|----------|-----------|
| OnShape CAD model v24 | [cad.onshape.com link](https://cad.onshape.com/documents/4f04f63bfd4138a61a54b3f8/v/88d7fcc8417e56a4ac5f9154/e/a2eb55ebc566613c79946855) | Full MSRE including vessel, core, primary circuit, thermal shield, reactor pit. Parts named by material (graphite, salt, inor-8). Thermally expanded to zero-power operating temperature. |
| Core dimensional reference | `core/docs/msrecore.tex` | ~52 kB LaTeX doc compiling exact ORNL report quotes with specific dimensions from ORNL-TM-3229, ORNL-3708, ORNL-4233, ORNL-TM-3039, ORNL-4676 — independent of our ORNL-TM-728 primary source |
| PHX OnShape model | [heatexchanger/hx.md](heatexchanger/hx.md) | Detailed primary heat exchanger + radiator CAD, with construction notes referencing original MSRE reports |
| CFD validation | Malcolm Akner thesis (LTU, 2021) | Turbulent CFD of PHX and radiator; results compared to MSRE operating data in Chapter 7 — the only publicly available CFD-vs-experiment validation for these components |
| OpenMC benchmark notebooks | `openmc_notebooks/` | Criticality test + depletion + isothermal temperature coefficient — use CAD-derived h5m geometry |
| DAGMC geometry | `h5m/msre_full.h5m`, `msre_control_rod.h5m` | Independently meshed MSRE geometry for particle transport |
| Dynamic nodal model | `dynamic_model/` | Non-linear delay-differential model (Singh et al.) — geometry-derived parameters (loop transit time τ_C, heat transfer coefficients, node masses) |

---

## 2. Five Validation Pathways

### 2.1 Dimensional Cross-Check (Highest Priority, Zero Cost)

**Method:** Parse `core/docs/msrecore.tex` for numerical values; compare against
`components/*/specifications.md` and `cad/scripts/*.py` parameter constants.

**What it catches:** Discrepancies between ORNL-TM-728 (our primary source) and the
multi-report synthesis in msrecore.tex, which draws from ORNL-TM-3229, ORNL-3708, etc.

**Known discrepancies already visible from inspection:**

| Parameter | openmsr/msre value | Our value | Notes |
|-----------|-------------------|-----------|-------|
| Vessel lower/upper head OD | 60 in (1524 mm) ← ORNL-TM-3229: *"standard 60 in. od asme flanged and dished head"* | 55.5 in (1410 mm) ← ORNL-TM-728 | **CONFLICT** — may reflect different measurement basis (vessel cylinder OD vs. head flange OD) or a design revision between reports. Requires resolution against original drawings. |
| Graphite stringer count | 617 (full + fractional) ← ORNL-TM-3039 | HOLD — ORNL-TM-728 Table 3.1 needed | openmsr independently resolves this open item in our BOM |
| Graphite stringer total length | ~67 in (1702 mm) ← ORNL-TM-3039 | 64 in (1626.4 mm) active height | Our value is active height; 67 in includes spike/dowel end — consistent |
| Vessel wall (upper section) | 1 in (25.4 mm) for top 16 in of shell ← ORNL-TM-3229 | 12.7 mm (0.5 in) uniform | **CONFLICT** — upper shell thickened for 84 orifice holes; our script uses uniform wall |
| Salt inlet nozzle | 6-in tangential volute ← ORNL-TM-3229 | 4-in SCH40 axial ← ORNL-TM-728 | **CONFLICT** — may be different connections (volute entry vs. nozzle stub) |

**Automation path:**
```python
# cad/validation/cross_check_openmsr.py (proposed)
# 1. Fetch msrecore.tex via GitHub API or local clone
# 2. Regex-extract all numeric patterns with units (e.g., r'(\d+\.?\d*)\s*in\.')
# 3. Map extracted values to component parameter names
# 4. Diff against our specifications.md values
# 5. Output discrepancy report with ORNL source citations
```

---

### 2.2 CAD Geometry Comparison (Geometric Diff)

**Method:** Export our STEP files and the openmsr OnShape model to the same format;
compare bounding boxes, cross-sectional areas, and volume at key Z-heights.

**Pipeline:**
1. Download openmsr OnShape model as STEP (Onshape has a free STEP export API)
2. Import both into a common frame using `cadquery` or `pythonOCC`
3. Compute bounding box comparison, volume comparison, and cross-section overlays
4. Plot overlay PNG: our model (blue, semi-transparent) vs. openmsr model (red, semi-transparent)

**What it catches:**
- Head geometry errors (our polyline approximation vs. OnShape spline)
- Missing features (anti-swirl vanes, bypass flow slots, strainer basket, core can)
- Positional offsets (nozzle locations, control rod thimble positions)
- Overall assembly envelope discrepancies

**Key geometry the openmsr model has that ours lacks:**
- Core wall cooling annulus (1-in gap between vessel wall and core can)
- Core can itself (separate Hastelloy-N cylindrical shell inside vessel)
- 84 inlet orifice holes on upper vessel wall
- Anti-swirl vanes (48 plates in lower head)
- Graphite strainer ring at vessel outlet
- Nozzle plug (9.77 in OD removable plug with 3 control rod thimbles)
- Thermal shield and insulation

These omissions are acceptable in our reference model but should be documented as
known simplifications (see `cad/cad_review/cad_review_report.md`).

---

### 2.3 OpenMC k-eff as Physics-Based Geometry Validator

**Method:** Use the `CAD_to_openMC` pipeline (same toolchain as openmsr) to convert
our STEP files to h5m and run the same criticality notebook.

**Rationale:** k-eff is extremely sensitive to core geometry (stringer pitch, void
fraction, active height, fuel channel dimensions). A geometry error of even ±5 mm in
the stringer array shifts k-eff by ~200–500 pcm. The MSRE operated at k-eff ≈ 1.00
with known critical configuration.

**Benchmark target:**  
openmsr/msre reports k-eff from `msre_criticality_test.ipynb`.  
If our STEP files reproduce the same k-eff (within ±500 pcm), the core geometry is validated.  
Divergence > 500 pcm → geometry error in `02_reactor_core.py`.

**Pipeline:**
```bash
# Requires: openmc, CAD_to_openMC
pip install openmc  # or use openmsr/openmc_install_scripts
git clone https://github.com/openmsr/CAD_to_openMC
python CAD_to_openMC/convert_cad.py cad/step/02_reactor_core.step -o cad/h5m/02_reactor_core.h5m
# Then run criticality notebook with our h5m replacing theirs
```

**This is the single most authoritative check for the reactor core geometry.**

---

### 2.4 CFD Thermal Validation (PHX + Radiator)

**Method:** Use Akner's thesis (Chapter 7) as benchmark data:
- PHX: overall heat transfer coefficient U, pressure drop, outlet temperatures
- Radiator: air-side heat rejection, salt-side ΔT

**What to check:**
The thesis validates CFD results against MSRE operating data. If our PHX STEP file
(after the critical fixes in Section 4 below) is imported into SimScale or OpenFOAM,
the resulting U, LMTD, and ΔP should match the thesis values.

**Key thesis results (from Akner 2021, Chapter 6-7):**
- PHX: U_calc ≈ 4,200 W/(m²·K), consistent with ORNL design value
- PHX: validated temperature profiles match MSRE operating records
- Radiator: CFD-to-experiment agreement within ~5%

**This directly validates the dimensional corrections made to the PHX model:**
- Tube pitch 12.7 mm (corrected from 15.9 mm)
- Tube-sheet thickness 76.2 mm (corrected from 38.1 mm)

---

### 2.5 Dynamic Model Parameter Extraction

**Method:** Compute geometry-derived parameters from our STEP volumes and compare
to the values used in `dynamic_model/` (Singh et al. replication).

**Parameters derivable from CAD geometry:**

| Parameter | Symbol | How to compute from STEP | Used in nodal model |
|-----------|--------|--------------------------|---------------------|
| Primary loop transit time | τ_C | Loop volume / volumetric flow rate = V_primary / 75.7 L/s | Delay term in DDE |
| Fuel mass in core | m_f1, m_f2 | Core fuel channel volume × salt density (2240 kg/m³) | Heat transfer nodes |
| Graphite mass per node | m_g | Core graphite volume × graphite density (1.86 g/cm³) | Heat transfer nodes |
| Fuel-graphite heat transfer area | A_fg | Total fuel-channel wall area in active zone | hA_fg coefficient |
| Heat exchanger UA | UA | From validated CFD (Pathway 2.4) | HX heat transfer node |

**Validation check:** Extract these from our STEP files using `cadquery` volume queries;
compare to the values in Singh et al. Table 1 (reproduced in `dynamic_model/README.md`).

---

## 3. Immediate Action Items (Prioritized)

### Today (Zero tooling required)

1. **Resolve vessel OD conflict:**  
   Read ORNL-TM-3229 Section 3 (from [msr-archive](https://github.com/openmsr/msr-archive)) to determine if the 60-in head refers to the flange OD (not the shell OD). Our 55.5 in is from ORNL-TM-728 shell drawing. Add clarifying note to `01_reactor_vessel.py` and `components/01_reactor_vessel/specifications.md`.

2. **Close the stringer count open item:**  
   openmsr/msre conclusively states 617 stringers (from ORNL-TM-3039 p.112+114). Update `components/02_reactor_core/bom.csv` RC-001/RC-002 quantities from HOLD to 617.

3. **Add openmsr to `docs/references.md`:**  
   Cite the OnShape model and Akner thesis as secondary validation sources.

### This Week

4. **Implement `cad/validation/cross_check_openmsr.py`:**  
   Automated dimensional diff against msrecore.tex values.  
   Run as part of `make validate`.

5. **Add missing upper-section wall thickening to vessel script:**  
   The top 16 in (406 mm) of the vessel shell is 1 in (25.4 mm) thick per ORNL-TM-3229
   (currently uniform 12.7 mm in our model). Update `01_reactor_vessel.py`.

### Next Sprint

6. **OpenMC k-eff benchmark (Pathway 2.3):**  
   Integrate `CAD_to_openMC` into CI or a one-off notebook.
   Target: k-eff within ±500 pcm of openmsr benchmark.

7. **Geometric overlay visualization (Pathway 2.2):**  
   Download openmsr OnShape STEP via API, compute bounding-box comparison,
   render overlay PNG for each component.

---

## 4. Critical Dimensional Fixes Already Applied (from msr-gstack Review)

The multi-agent review (`cad/cad_review/cad_review_report.md`) already identified several
errors that the openmsr cross-check independently confirms should be fixed:

| Fix | Script | Before | After | openmsr confirmation |
|-----|--------|--------|-------|---------------------|
| Head crown depth | `01_reactor_vessel.py` | OD/4 = 352.5 mm | ID/4 = 346.15 mm | msrecore.tex: ASME F&D head formula uses inside diameter |
| PHX tube pitch | `03_primary_heat_exchanger.py` | 15.9 mm | 12.7 mm | Akner thesis: triangular pitch = 1.33 × tube OD |
| PHX tube-sheet | `03_primary_heat_exchanger.py` | 38.1 mm | 76.2 mm | Akner thesis: TS = 3.0 in per design drawings |
| Fuel pump bowl height | `04_fuel_salt_pump.py` | 1829 mm (total length) | 609.6 mm | OnShape model shows bowl ≈ bowl OD |
| Coolant pump bowl height | `05_coolant_salt_pump.py` | 1524 mm (total length) | 457 mm | OnShape model shows same proportions |

---

## 5. What openmsr/msre Cannot Validate

For completeness, openmsr/msre has these gaps that our repo must resolve independently:

| Component | Gap |
|-----------|-----|
| Fuel Drain Tank (06) | Not in openmsr model (excluded from pit model) |
| Freeze Valves (07) | Not in openmsr model |
| Off-Gas System (08) | Not in openmsr model |
| Control Rods (09) | Present in openmsr as h5m, but no parametric STEP |
| Reactor Cell shielding (10) | Excluded from openmsr core model |
| Instrumentation (12) | Not in openmsr model |

For these components, `components/*/specifications.md` (ORNL-TM-728 primary source)
remains the sole dimensional reference. The Akner thesis provides secondary validation
for the **radiator** (Component 11) which openmsr also partially covers.

---

## 6. Integration into Repository Workflow

```
┌──────────────────────────────────────────────┐
│  openmsr/msre                                │
│  ├── msrecore.tex  (dimension reference)     │
│  ├── OnShape STEP  (geometry reference)      │
│  └── OpenMC h5m   (physics reference)        │
└──────────────────┬───────────────────────────┘
                   │ cad/validation/cross_check_openmsr.py
                   ▼
┌──────────────────────────────────────────────┐
│  This repo (msre_hardware_design)            │
│  ├── components/*/specifications.md          │
│  │   └── ORNL-TM-728 primary source         │
│  ├── cad/scripts/*.py                        │
│  │   └── parametric CadQuery models         │
│  ├── cad/step/*.step                         │
│  │   └── STEP AP214 exchange files          │
│  └── cad/cad_review/                        │
│      └── msr-gstack agent review            │
└──────────────────────────────────────────────┘
                   │ CAD_to_openMC pipeline
                   ▼
┌──────────────────────────────────────────────┐
│  OpenMC k-eff benchmark                      │
│  ├── Target: match openmsr k-eff ± 500 pcm  │
│  └── Pass/fail in CI                        │
└──────────────────────────────────────────────┘
```

**Proposed addition to `Makefile`:**
```makefile
cross-check:   ## Cross-check dimensions against openmsr/msre
	python3 cad/validation/cross_check_openmsr.py
```

---

## 7. References

| Reference | URL |
|-----------|-----|
| openmsr/msre GitHub | https://github.com/openmsr/msre |
| OnShape CAD model v24 | https://cad.onshape.com/documents/4f04f63bfd4138a61a54b3f8/v/88d7fcc8417e56a4ac5f9154/e/a2eb55ebc566613c79946855 |
| Akner thesis (LTU, 2021) | https://ltu.diva-portal.org/smash/get/diva2:1546993/FULLTEXT01.pdf |
| CAD_to_openMC | https://github.com/openmsr/CAD_to_openMC |
| Singh et al. dynamic model | https://doi.org/10.1016/j.anucene.2017.11.002 |
| msr-archive (ORNL reports) | https://github.com/openmsr/msr-archive |
