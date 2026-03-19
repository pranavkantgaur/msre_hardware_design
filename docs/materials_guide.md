# Materials Guide

This document describes the primary materials used in MSRE construction, their specifications, sourcing guidance, and fabrication considerations.

---

## 1. Hastelloy-N (INOR-8, UNS N10003)

### Background
Hastelloy-N was specifically developed at ORNL for the MSRE as the primary structural material in contact with fluoride molten salts at high temperatures. It is the most critical material in the MSRE design.

### Composition (weight percent)

| Element | Nominal | Range |
|---------|---------|-------|
| Nickel (Ni) | Balance | — |
| Molybdenum (Mo) | 16% | 15–18% |
| Chromium (Cr) | 7% | 6–8% |
| Iron (Fe) | 4% | ≤5% |
| Silicon (Si) | — | ≤1% |
| Manganese (Mn) | — | ≤0.80% |
| Carbon (C) | — | ≤0.08% |
| Tungsten (W) | — | ≤0.5% |
| Cobalt (Co) | — | ≤0.2% |
| Copper (Cu) | — | ≤0.35% |
| Boron (B) | — | ≤0.01% (critical: excess B embrittles under irradiation) |
| Phosphorus (P) | — | ≤0.015% |
| Sulfur (S) | — | ≤0.020% |

### Key Properties at Operating Temperature (~650 °C)

| Property | Value |
|----------|-------|
| Ultimate tensile strength | ~552 MPa (80 ksi) |
| Yield strength (0.2% offset) | ~276 MPa (40 ksi) |
| Elongation | ~45% |
| Density | 8.86 g/cm³ |
| Thermal conductivity | ~11.9 W/(m·K) at 650 °C |
| Thermal expansion (avg, 25–650°C) | ~13.1 × 10⁻⁶ /°C |
| Modulus of elasticity | ~172 GPa at 650 °C |

### Corrosion Resistance
- Virtually no corrosion by LiF-BeF₂ fuel and coolant salts under MSRE conditions (total corrosion ~0.025 mm over full service life).
- Corrosion mechanism is selective dissolution of Cr; controlled by salt redox potential.
- Must maintain salt redox potential (U⁴⁺/U³⁺ ratio) in the mildly reducing range.

### Fabrication Notes
- Weldable by TIG (GTAW) process with matching Hastelloy-N filler wire.
- All welds in salt-wetted service must be dye-penetrant and radiographically inspected.
- Post-weld heat treatment: anneal at 1175 °C (2150 °F) in inert atmosphere, water quench.
- Avoid carburizing atmospheres; carbides impair corrosion resistance.
- Standard mill forms: sheet, plate, bar, tube, pipe, and forgings available from specialty suppliers.

### Modern Sourcing
- Haynes International (Kokomo, IN, USA) produces Hastelloy-N as their commercial product.
- Alternative: ATI, Special Metals Corp.
- ASTM specification: ASTM B619 (welded pipe), ASTM B622 (seamless pipe/tube), ASTM B575 (plate/sheet/strip).

---

## 2. AGOT Nuclear-Grade Graphite

### Background
The MSRE reactor core moderator and reflector were fabricated from AGOT (Acheson Graphite Oil-Treated) nuclear-grade graphite, produced by Union Carbide (now GrafTech International).

### Key Properties (room temperature)

| Property | Value |
|----------|-------|
| Bulk density | 1.69–1.72 g/cm³ |
| Porosity (open) | ~19% |
| Compressive strength | ~34.5 MPa (5,000 psi) |
| Tensile strength | ~13.8 MPa (2,000 psi) |
| Flexural strength | ~17.2 MPa (2,500 psi) |
| Thermal conductivity (with grain) | ~155 W/(m·K) |
| Thermal conductivity (against grain) | ~95 W/(m·K) |
| Coefficient of thermal expansion (with grain) | ~1.8 × 10⁻⁶ /°C |
| Electrical resistivity | ~1000 µΩ·cm |

### Salt Permeability Concern
- Raw AGOT graphite has ~19% open porosity and would absorb fuel salt, increasing fissile inventory and causing graphite swelling.
- **MSRE Solution:** Graphite was impregnated with furfuryl alcohol (polymerized in-situ) to seal open pores, reducing open porosity to <0.1%.
- Seal treatment reduces salt absorption to <0.5% by volume under MSRE conditions.

### Radiation Effects
- Graphite dimensional changes under fast-neutron irradiation (shrinkage then growth).
- MSRE graphite was expected to remain serviceable for the experiment duration (<10²² n/cm²).
- For higher-fluence applications, nuclear graphite grades with improved radiation stability (e.g., H-451, IG-110) are preferred.

### Modern Sourcing
- GrafTech International (formerly Union Carbide Carbon Products): AGOT and ATJ grades.
- Toyo Tanso (IG-110 grade, Japan/USA): highly purified, fine-grain nuclear graphite.
- SGL Carbon: R7650 nuclear graphite.
- POCO Graphite (Entegris): specialty grades for sealed/low-permeability requirements.

---

## 3. Fuel Salt: LiF-BeF₂-ZrF₄-UF₄

### Composition (mole percent)

| Component | Mole % | Purpose |
|-----------|--------|---------|
| LiF | 65.0% | Primary carrier salt; provides Li for breeding potential |
| BeF₂ | 29.1% | Carrier; reduces melting point; moderates slightly |
| ZrF₄ | 5.0% | Corrosion inhibitor; stabilizes oxidation state |
| UF₄ | 0.9% | Fissile material (initially ²³⁵U, later ²³³U) |

> **Note:** Lithium must be isotopically enriched to ≥99.99% ⁷Li (natural Li contains 7.5% ⁶Li which poisons the reactor and produces tritium).

### Physical Properties

| Property | Value |
|----------|-------|
| Liquidus temperature | ~450 °C (842 °F) |
| Operating range | 550–700 °C |
| Density at 650 °C | ~2.24 g/cm³ |
| Viscosity at 650 °C | ~9 cP |
| Heat capacity | ~1.508 J/(g·K) |
| Thermal conductivity | ~1.0 W/(m·K) |

### Preparation
Salt is prepared by:
1. Blending dry LiF, BeF₂, ZrF₄ powders in correct molar ratios.
2. Melting and sparging with HF/H₂ mixture to remove oxide and hydroxide impurities.
3. Adding UF₄ (or UF₄ + ThF₄) to achieve desired fissile loading.
4. Performing final chemistry analyses (redox potential, impurity levels) before loading.

### Hazard Note
BeF₂ is a beryllium compound — full beryllium safety protocols required (see `safety_considerations.md`).

---

## 4. Coolant Salt: LiF-BeF₂ (Flibe)

### Composition

| Component | Mole % |
|-----------|--------|
| LiF | 66.0% |
| BeF₂ | 34.0% |

### Physical Properties

| Property | Value |
|----------|-------|
| Liquidus temperature | ~459 °C (858 °F) |
| Density at 650 °C | ~1.94 g/cm³ |
| Viscosity at 650 °C | ~6 cP |
| Heat capacity | ~2.38 J/(g·K) |
| Thermal conductivity | ~1.0 W/(m·K) |

### Notes
- No fissile material; lower radiation level than fuel salt.
- Same ⁷Li enrichment requirement as fuel salt.
- BeF₂ hazard applies equally.

---

## 5. Insulation Materials

| Application | Material | Notes |
|-------------|----------|-------|
| Pipe and vessel exterior | Min-K or Microtherm microporous silica | High-temperature; ~650 °C rated |
| Removable blanket insulation | Fiberfrax ceramic fiber blankets | Used on components requiring maintenance access |
| Under heat tracing | Calcium silicate board | Dimensionally stable; supports heater wire |

---

## 6. Heat Tracing (Electric)

- All primary and secondary loop piping must be heat-traced to maintain salt above liquidus (>460 °C) during standby.
- MSRE used resistance-wire type heaters (Nichrome) embedded in grooves cut into the pipe insulation.
- Heater density: ~3.3 W/cm of pipe length for 101.6 mm (4 in) piping to maintain 550 °C ambient.
- Modern alternative: mineral-insulated (MI) cable electric trace heaters rated for >700 °C surface temperature.

---

## 7. Gasket and Seal Materials

- **No organic gaskets** may be used in fluoride salt service or in radiation fields.
- Metal gaskets: Annealed nickel or Hastelloy-N ring-type joints (RTJ) for flanged connections.
- Where possible, all connections should be butt-welded to eliminate flange joints.
- Valve packing (freeze valve atmosphere side): Grafoil (expanded graphite) or metallic packing only.

---

## 8. Filter/Purification Materials

| Application | Material |
|-------------|----------|
| Off-gas delay beds | Coconut-shell activated charcoal (nuclear grade) |
| Off-gas HEPA filtration | Sintered Hastelloy or stainless steel elements |
| Salt cleanup (fluorination) | NiF₂ pellets or F₂ gas system |
