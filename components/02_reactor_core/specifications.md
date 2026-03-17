# Reactor Core — Detailed Specifications

**Reference:** ORNL-TM-728, Section 3.3; ORNL-3674; ORNL-TM-1240

---

## 1. Core Geometry Specifications

### Active Zone Envelope
- **Shape:** Right circular cylinder
- **Outer diameter:** 1372.0 mm (54.0 in)
  > *Corrected from 1397 mm (55.0 in): the vessel inner diameter is 1384.6 mm (54.5 in);
  > a 6.4 mm (0.25 in) annular clearance gap between the graphite assembly and the vessel
  > wall (confirmed in core README) sets the graphite OD at ≈ 1371.8 mm ≈ 1372 mm.
  > Verify exact value against ORNL-TM-728 Figure 3.1 drawing.*
- **Active height:** 1626.4 mm (64.0 in)
- **Radial graphite reflector thickness:** ~76 mm (3.0 in) on sides (solid graphite blocks, no fuel channels)
  > *The reflector fills the space between Zone II outer boundary (r ≈ 610 mm) and the
  > graphite assembly OD (r = 686 mm). Verify exact annulus geometry against ORNL-TM-728.*
- **Axial graphite reflector thickness:** ~152 mm (6.0 in) top/bottom (end blocks, no fuel channels)

### Graphite Stringer Array
- **Array type:** Square pitch
- **Nominal stringer cross-section:** 50.8 mm × 50.8 mm (2.0 in × 2.0 in)
- **Array pitch:** 53.85 mm (2.12 in) center-to-center
- **Face-to-face gap:** 3.05 mm (0.12 in) between stringers
- **Total channel area as fraction of total core cross-section:** ~22.5%

### Radial Zones

| Zone | Inner radius | Outer radius | Channel groove depth (each face) | Target void fraction |
|------|-------------|-------------|----------------------------------|----------------------|
| Zone I (inner) | 0 mm | 457 mm | 3.18 mm (0.125 in) | ~25% |
| Zone II (outer) | 457 mm | ~610 mm | 2.38 mm (0.094 in) | ~18% |
| Radial reflector | ~610 mm | 686 mm | None (solid) | ~2% |

> *Zone II and reflector outer radii are derived from the corrected graphite assembly OD
> of 1372 mm (r = 686 mm) with an estimated 3-in (76 mm) radial reflector. Exact zone
> boundaries must be confirmed against ORNL-TM-728 Section 3.3 drawings.*

---

## 2. Individual Stringer Specifications

### Zone I Stringer
| Dimension | Value |
|-----------|-------|
| Cross-section | 50.8 mm × 50.8 mm |
| Length | 1676 mm (66.0 in) |
| Channel groove width | 6.35 mm (0.25 in) per face |
| Channel groove depth | 3.18 mm (0.125 in) per face |
| Channel position on face | Centered |
| Number of grooves per face | 1 (centered groove on each of 4 faces) |
| Tolerance on cross-section | ±0.25 mm |
| Tolerance on length | ±1.6 mm |
| Straightness | ≤1.0 mm total in 1676 mm length |
| Surface finish (salt-wetted) | ≤3.2 µm Ra |

### Zone II Stringer
Same as Zone I except:
- Channel groove depth: 2.38 mm (0.094 in) per face
- Channel groove width: 4.75 mm (0.187 in) per face

### Reflector Block
- Various shapes (rectangular parallelepipeds, wedges) to fill the annular reflector zone.
- No channels machined; bulk graphite only.
- Same material grade and seal treatment as stringers.

---

## 3. Graphite Material Specifications

### Chemical Purity Requirements
| Impurity | Maximum Limit |
|----------|--------------|
| Total ash | 25 ppm |
| Boron (B) equivalent | 5 ppm |
| Vanadium (V) | 5 ppm |
| Chlorine (Cl) | 5 ppm |
| Total alkali metals (Li+Na+K) | 10 ppm |

### Physical Properties (acceptance range)
| Property | Min | Max |
|----------|-----|-----|
| Bulk density | 1.69 g/cm³ | 1.75 g/cm³ |
| Compressive strength (with grain) | 27.6 MPa | — |
| Flexural strength | 13.8 MPa | — |
| Thermal conductivity (25°C, with grain) | 130 W/(m·K) | — |
| CTE (25–600°C, with grain) | 1.2 × 10⁻⁶/°C | 3.5 × 10⁻⁶/°C |
| Open porosity (before sealing) | 16% | 22% |

### Post-Seal Acceptance
| Property | Acceptance Criterion |
|----------|---------------------|
| Open porosity | <0.5% |
| Helium permeability | <0.001 mD |
| Weight gain (resin uptake) | >3.5% by weight after all cycles |
| Visual | No cracks, chips, or delamination |

---

## 4. Control Rod Thimble Specifications

| Parameter | Value |
|-----------|-------|
| Material | Hastelloy-N, ASTM B622, UNS N10003 |
| Outside diameter | 44.45 mm (1.750 in) |
| Inside diameter | 38.05 mm (1.499 in) |
| Wall thickness | 3.18 mm (0.125 in) |
| Length | 1727 mm (68.0 in) |
| Lower end | Welded Hastelloy-N cap, full-penetration weld |
| Upper end | Butt-welded to vessel upper head nozzle (N3/N4/N5) |
| Surface finish (outer, salt-wetted) | ≤3.2 µm Ra |
| Straightness | ≤0.5 mm in full length |
| Position tolerance | ±3.2 mm from design centerline |

---

## 5. Support Grid Specifications

### Lower Support Grid
| Parameter | Value |
|-----------|-------|
| Material | Hastelloy-N, ASTM B575 |
| Diameter | 1380 mm |
| Thickness | 25.4 mm (1.0 in) |
| Hole pattern | 50.8 × 50.8 mm square holes on 53.85 mm pitch |
| Number of holes | ~509 *(corrected from ~640; matches corrected total stringer count ≈ 509. Verify against ORNL-TM-728.)* |
| Thimble holes | 3 × 46.05 mm diameter (for thimble OD + clearance) |
| Flatness | ≤0.5 mm over full diameter |

### Upper Hold-Down Grid
| Parameter | Value |
|-----------|-------|
| Material | Hastelloy-N, ASTM B575 |
| Diameter | 1380 mm |
| Thickness | 19.05 mm (0.75 in) |
| Hole pattern | Same as lower grid |

---

## 6. Core Criticality and Reactivity Parameters

| Parameter | Value | Note |
|-----------|-------|------|
| Initial critical loading (²³⁵U) | ~33 kg | Dissolved in fuel salt as UF₄ |
| Reactor critical at room temp (cold) | Not achievable — requires salt melting | — |
| k-eff (hot full power, design rods) | ~1.004 | With rods partially inserted |
| k-eff (hot zero power) | ~1.000 + control rod worth | — |
| Excess reactivity (hot) | ~1.0% Δk/k | Available for burnup/temperature |
| Temperature coefficient (overall) | −8.7 × 10⁻⁵ Δk/k/°C | Strongly negative |
| Void coefficient | ~−0.5% Δk/k per 1% void | Negative |
| Prompt neutron lifetime | ~3.0 × 10⁻⁴ s | Thermal spectrum |
| Effective delayed neutron fraction β_eff (²³⁵U) | ~0.004 | *Corrected from 0.00265 (which matches ²³³U); static β for ²³⁵U = 0.0065; circulating-fuel reduction ≈40 % → β_eff ≈ 0.004. Verify against ORNL-TM-1647.* |

---

## 7. Dimensional Inspection Plan

| Check | Method | Frequency |
|-------|--------|----------|
| Stringer cross-section | Calibrated micrometer, 3 points per stringer | 100% |
| Stringer length | Calibrated ruler | 10% sample (100% if out-of-spec) |
| Channel groove width and depth | Calibrated groove gauge | 10% sample |
| Straightness | Precision straightedge + feeler gauge | 10% sample |
| Open porosity (sealed) | Mercury porosimetry | 5 samples per batch of 100 |
| Helium permeability (sealed) | Gas permeameter | 5 samples per batch of 100 |
| Boron impurity (raw graphite) | INAA (instrumental neutron activation analysis) | 1 per heat of graphite |
