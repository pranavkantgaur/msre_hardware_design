# Component 02: Reactor Core (Graphite Moderator Assembly)

## Overview

The reactor core is a cylindrical assembly of nuclear-grade graphite stringers (bars) arranged in a square-pitch array within the reactor vessel. Fuel salt flows upward through channels machined into and between the graphite elements, providing both moderation and fuel-carrying functions.

**Primary Reference:** ORNL-TM-728, Section 3.3; ORNL-3674

---

## Operating Conditions

| Parameter | Value |
|-----------|-------|
| Core inlet temperature (fuel salt) | 632 °C (1170 °F) |
| Core outlet temperature (fuel salt) | 654 °C (1210 °F) |
| Neutron flux (peak thermal) | ~4 × 10¹³ n/cm²·s |
| Neutron flux (peak fast, E>0.18 MeV) | ~3 × 10¹² n/cm²·s |
| Design fluence (lifetime) | <10²² n/cm² fast (graphite serviceable) |
| Fuel-to-moderator volume ratio | ~22.5% salt / 77.5% graphite |
| Core power density (average) | ~3 kW/L in active zone |

---

## Core Geometry

| Parameter | Metric | Imperial |
|-----------|--------|----------|
| Active core diameter | 1.372 m *(corrected from 1.397 m — see note below)* | 54.0 in |
| Active core height | 1.626 m | 64.0 in |
| Graphite stringer cross-section | 50.8 mm × 50.8 mm | 2.0 in × 2.0 in |
| Stringer pitch (square array) | 53.85 mm | 2.12 in |
| Total graphite stringers | ~509 *(corrected from 1,140 — see note below)* | — |
| Control rod thimble channels | 3 | — |
| Fuel-salt void fraction | ~22.5% | — |
| Core region graphite packing fraction | ~77.5% | — |

> **Core diameter correction:** The vessel inner diameter is 1384.6 mm (54.5 in).
> The core README states a 6.4 mm (0.25 in) annular clearance between graphite and
> vessel wall, which sets the graphite assembly OD at ≈ 1372 mm (54.0 in), not 1397 mm
> (55.0 in) as previously stated. An OD of 1397 mm would exceed the vessel ID.
> Verify exact dimension against ORNL-TM-728 Figure 3.1.
>
> **Stringer count correction:** At 50.8 mm × 50.8 mm cross-section on 53.85 mm pitch,
> approximately 509 stringers fit in a 54-in (1372 mm) diameter core
> (π × 686² / 53.85² ≈ 509). The previously stated value of 1,140 would require a
> core diameter of ~80 in — larger than the vessel. Verify exact count against
> ORNL-TM-728 Table 3.1.

---

## Graphite Stringer Design

Each graphite stringer is a prismatic bar with machined grooves that create flow channels for the fuel salt.

### Stringer Dimensions
| Parameter | Metric | Imperial |
|-----------|--------|----------|
| Cross-section | 50.8 mm × 50.8 mm | 2.0 in × 2.0 in |
| Length (active zone) | 1,676 mm | 66.0 in |
| Channel configuration | Grooves on all 4 faces | — |

### Channel Geometry (Machined into stringer faces)
- Each face has a central groove forming a half-channel.
- When two adjacent stringers are placed face-to-face, adjacent grooves form a complete rectangular channel.
- **Channel dimensions (assembled):** 6.35 mm × 6.35 mm (0.25 in × 0.25 in) typical; varies in different radial zones for flux shaping.
- **Channel spacing (face-to-face gap):** ~3.2 mm (0.125 in) gap between stringer faces provides additional flow area.

### Zoning
The core is divided into radial zones with different channel sizes to shape the radial power distribution:

| Zone | Description | Channel area (approx.) | Salt fraction |
|------|-------------|----------------------|---------------|
| Zone 1 (inner, ~0–457 mm radius) | Larger channels | ~25% void | Higher moderation |
| Zone 2 (outer, 457–698 mm radius) | Smaller channels | ~18% void | Reduced moderation |
| Reflector region | Solid blocks, no channels | ~2% void (gaps only) | Neutron reflection |

### Graphite Material
- **Grade:** AGOT nuclear graphite (Union Carbide / GrafTech)
- **Density:** 1.69–1.72 g/cm³
- **Purity:** <25 ppm ash content; <5 ppm boron equivalent
- **Seal treatment:** Furfuryl alcohol impregnation (see `docs/materials_guide.md`)
- **Permeability (sealed):** <0.001 mD (milliDarcy) to helium after sealing

---

## Control Rod Thimbles

Three control rod thimble channels are located in the central core region:

| Parameter | Value |
|-----------|-------|
| Thimble inner diameter | 38.1 mm (1.5 in) |
| Thimble outer diameter | 44.5 mm (1.75 in) |
| Thimble material | Hastelloy-N tube |
| Thimble length | 1,727 mm (68 in) — extends from lower head through core |
| Thimble spacing (centerline-to-centerline) | ~254 mm (10 in) |
| Thimble location | Near core center, triangular pitch |

- Control rods insert into thimbles from above.
- Thimbles are sealed at the lower end (welded cap) and open at the top to the control rod drive nozzle.
- Thimbles are surrounded by graphite; salt does not enter thimble interior.

---

## Graphite Seal Treatment Process

1. **Cleaning:** Machine graphite to final dimensions; blow dry with clean compressed air.
2. **Vacuum impregnation:** Place stringers in autoclave; evacuate to <1 Pa; flood with furfuryl alcohol monomer; pressurize to 700 kPa (100 psi) for 30 minutes to force liquid into pores.
3. **Polymerization (cure):** Heat to 150 °C in inert atmosphere (N₂) for 4 hours; temperature-hold allows furfuryl alcohol to polymerize in pores.
4. **Carbonization:** Heat to 900 °C in N₂ for 2 hours; polymer carbonizes to fill pores with solid carbon.
5. **Repeat:** Repeat steps 2–4 two additional times to achieve target permeability.
6. **Acceptance test:** Measure open porosity (ASTM C373 or mercury porosimetry) and helium permeability. Accept: open porosity <0.5%, helium permeability <0.001 mD.

---

## Core Assembly Procedure

1. Install lower support grid in reactor vessel.
2. Insert graphite stringers one at a time through the vessel top opening; seat each stringer in the lower grid.
3. Check stringer-to-stringer fit; shim if needed to maintain 3.2 mm (0.125 in) face-to-face gap.
4. Install control rod thimbles in designated positions during stringer insertion.
5. Install upper hold-down grid; secure to upper head.
6. Install upper head; torque studs.

---

## Core Nuclear Parameters

| Parameter | Value |
|-----------|-------|
| Effective multiplication factor (k-eff) at HFP | ~1.004 (with control rods partially inserted) |
| Prompt neutron lifetime | ~3.0 × 10⁻⁴ s |
| Delayed neutron fraction (β_eff) | ~0.004 (²³⁵U fuel, corrected; see note) |
| Temperature coefficient of reactivity (overall) | ~−8.7 × 10⁻⁵ Δk/k per °C |
| Void coefficient | Moderately negative (loss of fuel salt inserts negative reactivity) |
| Critical mass (²³⁵U at MSRE conditions) | ~33 kg |

> **β_eff note:** The value 0.00265 previously listed is consistent with ²³³U fuel
> (static β = 0.0027, circulation-reduced). For ²³⁵U fuel (static β = 0.0065),
> the circulating-fuel effective β is approximately 0.004. Verify against ORNL-TM-1647.

---

## Interfaces

| Interface | Connected To | Description |
|-----------|-------------|-------------|
| Graphite lower ends | Core support grid | Seated in machined pockets; sliding fit (thermal expansion) |
| Graphite upper ends | Upper hold-down grid | Retaining feature; allows some axial movement |
| Control rod thimbles | Reactor vessel top head nozzles | Welded to vessel nozzle top; pass through upper grid |
| Core outer boundary | Reactor vessel inner wall | 6.4 mm (0.25 in) annular gap (clearance between graphite OD = 1372 mm and vessel ID = 1384.6 mm) |
| Fuel salt inlet | Lower plenum (bottom of vessel) | Fuel salt floods lower plenum → enters core channel bottoms |
| Fuel salt outlet | Upper plenum (top of vessel) | Fuel salt exits channel tops → collects in upper plenum |
