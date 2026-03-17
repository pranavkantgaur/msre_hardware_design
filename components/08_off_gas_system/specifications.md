# Off-Gas System — Detailed Specifications

**Reference:** ORNL-TM-728, Section 3.10; ORNL-TM-4180

---

## 1. Noble Gas Stripping Efficiency

### Helium Sparge (Pump Bowl)

| Parameter | Value |
|-----------|-------|
| He sparge flow | 0.5 L/min (standard conditions, 25 °C) |
| Fuel salt flow through pump bowl | ~75.7 L/s |
| Contact time (gas–salt in bowl) | ~2 s |
| ¹³³Xe stripping efficiency per pass | ~90–95% |
| ¹³³Xe steady-state inventory in fuel salt | ~5% of production rate |
| Krypton stripping efficiency per pass | ~85–90% |

### Mass Balance (Steady State at 8 MWt)

| Nuclide | Production rate | Stripping rate | Off-gas activity |
|---------|----------------|----------------|-----------------|
| ¹³³Xe (t₁/₂ = 5.25 d) | ~130 Ci/day | ~120 Ci/day | ~120 Ci/day to off-gas |
| ¹³⁵Xe (t₁/₂ = 9.2 h) | ~310 Ci/day | ~285 Ci/day | ~285 Ci/day to off-gas |
| ⁸⁵ᵐKr (t₁/₂ = 4.48 h) | ~18 Ci/day | ~16 Ci/day | ~16 Ci/day to off-gas |
| ⁸⁸Kr (t₁/₂ = 2.84 h) | ~80 Ci/day | ~70 Ci/day | ~70 Ci/day to off-gas |

> Note: Activities are estimates based on standard fission yields and MSRE operating parameters.

---

## 2. Condensation Trap Specifications

| Parameter | Value |
|-----------|-------|
| Type | Double-pipe heat exchanger (inner/outer tube) |
| Inner tube (gas side) | Hastelloy-N; 12.7 mm OD × 1.65 mm wall |
| Outer tube (coolant jacket) | 316L SS; 25.4 mm OD × 2.41 mm wall |
| Active cooling length | 500 mm |
| Coolant | Facility cooling water (15 °C), ~2 L/min |
| Gas outlet temperature | ~50 °C (from 640 °C) |
| Condensate accumulation | Salt aerosol + moisture; drained to radioactive waste |
| Condensate drain valve | Freeze valve (Type B) — 6.35 mm Hastelloy-N tube |

---

## 3. Primary Charcoal Delay Bed Specifications

### Charcoal Properties

| Property | Requirement |
|----------|-------------|
| Type | Coconut-shell activated charcoal, nuclear grade |
| Iodine number | >1,000 mg/g |
| BET surface area | >900 m²/g |
| Mesh size | 4×8 (4.75–2.36 mm) |
| Ash content | <3 wt% |
| Moisture content | <2 wt% (as delivered) |
| Radioactive impurities | <0.01 µCi/g |
| Charcoal bed supplier example | Calgon Carbon BPL 4×8, nuclear grade |

### Bed Vessel

| Parameter | Value |
|-----------|-------|
| Quantity | 2 beds in series |
| Each bed dimensions | 450 mm ID × 1,600 mm length (active height) |
| Each bed volume | ~254 L |
| Total charcoal volume | ~508 L (500 kg charcoal) |
| Vessel material | 304L SS outer shell; inner surfaces lined with 316L SS |
| Design pressure | 170 kPa gauge (25 psig) |
| Design temperature | 65 °C (ambient; no heating required) |
| Orientation | Vertical; gas flows upward through bed |
| Gas distributor (inlet) | 316L SS perforated plate; open area >30% |
| Hold-down screen (outlet) | 316L SS wire mesh, 0.8 mm aperture |

### Xenon Delay Performance

| Nuclide | Half-life | Sorption coefficient (ρ; room T) | Delay time (500 kg charcoal) |
|---------|-----------|----------------------------------|------------------------------|
| ¹³³Xe | 5.25 days | ~800 cm³/g | ~50 days → >9 half-lives ✓ |
| ¹³⁵Xe | 9.2 hours | ~400 cm³/g | ~25 days → >65 half-lives ✓ |
| ⁸⁵ᵐKr | 4.48 hours | ~20 cm³/g | ~1.2 days → >6 half-lives ✓ |
| ⁸⁸Kr | 2.84 hours | ~20 cm³/g | ~1.2 days → >10 half-lives ✓ |

> Requirement: >10 half-lives decay before release (for all isotopes with t₁/₂ > 1 hour).
> ⁸⁵Kr (t₁/₂ = 10.7 yr): cannot be decayed — retained in secondary cooled bed.

---

## 4. Secondary Cooled Charcoal Bed Specifications

| Parameter | Value |
|-----------|-------|
| Purpose | Long-term retention of ⁸⁵Kr |
| Quantity | 1 bed |
| Vessel dimensions | 500 mm ID × 2,400 mm length |
| Charcoal volume | ~471 L (750 kg charcoal) |
| Coolant jacket | Water jacket around vessel |
| Operating temperature | 10–15 °C |
| Sorption coefficient for Kr at 12 °C | ~100 cm³/g (5× improvement over room temperature) |
| ⁸⁵Kr delay time (750 kg at 12 °C) | ~6,000 days — effectively permanent retention for operating period |
| Vessel material | 304L SS with water jacket |
| Design pressure | 170 kPa (25 psig) |

---

## 5. HEPA Filter Specifications

| Parameter | Value |
|-----------|-------|
| Efficiency | 99.97% at 0.3 µm (HEPA standard) |
| Type | Sintered metal (replaces paper HEPA; radiation-resistant) |
| Element material | Sintered Hastelloy-N powder |
| Element OD | 150 mm |
| Element length | 250 mm |
| Housing material | Hastelloy-N or 316L SS |
| Design pressure | 170 kPa gauge |
| Pressure drop (clean) | <5 kPa at design flow |
| Pressure drop (replace at) | >20 kPa (differential pressure switch alarm) |
| Installation | Bag-in/bag-out (BIBO) design — filter can be changed without direct contact |

---

## 6. Off-Gas Piping Design

| Segment | Material | Size | Temperature | Justification |
|---------|----------|------|-------------|---------------|
| Pump bowl to condensation trap | Hastelloy-N | 12.7 mm OD | 50–640 °C | Fluoride salt compatibility required at hot end |
| Condensation trap to cell wall | Hastelloy-N | 12.7 mm OD | ~50 °C | Same material for consistency inside cell |
| Cell wall to charcoal beds | 316L SS | 25.4 mm OD | Ambient | No salt contact; ambient temperature |
| Charcoal bed interconnect | 316L SS | 25.4 mm OD | Ambient | — |
| HEPA to stack | 316L SS | 50.8 mm OD | Ambient | — |

---

## 7. Radiation Dose Rate in Off-Gas System

| Location | Dose Rate (contact) |
|----------|-------------------|
| Off-gas line at pump bowl | >1,000 R/h (direct beta/gamma from Xe/Kr) |
| After condensation trap | ~100 R/h |
| Primary charcoal bed surface | ~10–100 R/h (during operation) |
| Secondary charcoal bed surface | ~1–10 R/h |
| Stack gas monitor | <1 mR/h (after decay) |

> All off-gas equipment inside and adjacent to reactor cell must be accessible only with remote tools or after extended decay period.
