# Reactor Cell — Detailed Specifications

**Reference:** ORNL-TM-728, Section 4.1; ORNL-3014

---

## 1. Shielding Analysis

### Design Basis Radiation Source

The shielding is designed to reduce dose rates from the operating reactor to acceptable levels at the cell exterior. The dominant source terms are:

| Source | Activity at Full Power |
|--------|----------------------|
| Fuel salt (dissolved fission products) | ~10⁶ Ci total beta/gamma |
| Prompt fission gammas from core | ~8 MWt fission power |
| Capture gammas (Hastelloy-N, graphite) | ~0.5 MWt |
| Activated coolant salt (minimal) | <1 Ci |

### Shielding Calculation Basis

| Assumption | Value |
|------------|-------|
| Point source approximation | Conservative; actual is distributed source |
| Gamma energy spectrum | 2–3 MeV average (fission product mix) |
| Target dose rate outside cell | <0.25 mSv/h (25 mrem/h) |
| Required attenuation | >10⁶ (from ~250,000 mSv/h at source to <0.25 mSv/h) |
| Required concrete thickness (2-MeV gamma, μ = 0.048 /cm in baritic concrete) | ~1.52 m (10 HVLs) |

### Shielding Dimensions by Wall Location

| Wall | Thickness | Material | Reason for Variation |
|------|-----------|----------|---------------------|
| Side walls (adjacent to reactor vessel) | 2.44 m | Normal concrete | Closest to source; maximum shielding |
| Side walls (far from reactor) | 1.52 m | Normal concrete | Reduced requirement |
| Roof/ceiling | 2.44 m | Normal concrete | Direct activation shine upward |
| Floor (above drain tank cell) | 1.22 m | Normal concrete | Reduced; drain tank has own shielding |
| Access door | 0.50 m | Lead-filled steel | Door-width constraint |
| Viewing windows | 0.60 m | Lead glass | Optical transparency required |

### Concrete Specification

| Property | Normal Weight | Baritic (High-Density) |
|----------|--------------|----------------------|
| Type | ASTM C150 Type II (sulfate-resistant) | — |
| Aggregate | Limestone or gravel | Barite (BaSO₄) |
| Density | 2,307 kg/m³ (144 lb/ft³) | 3,200–3,520 kg/m³ (200–220 lb/ft³) |
| f'c (28-day) | ≥34 MPa (5,000 psi) | ≥41 MPa (6,000 psi) |
| Water/cement ratio | ≤0.45 | ≤0.40 |
| Notes | Standard reinforced concrete | Use where space is constrained |

---

## 2. Nitrogen Purge System Specifications

### Supply System

| Parameter | Value |
|-----------|-------|
| N₂ source | Liquid nitrogen (LN₂) supply → vaporizer → distribution |
| LN₂ storage tank | 20,000 L dewar; 7-day supply at normal operation |
| Vaporizer capacity | 50 Nm³/h |
| Distribution pressure | 150 kPa gauge (20 psig) |
| Cell injection points | 4 (corner of cell near floor level for sweep from floor up) |
| Exhaust | Single point at ceiling; routed through HEPA filter |
| Normal purge flow | ~2 Nm³/h (makeup for leakage + oxygen generation by radiolysis) |
| Emergency purge flow (on cell breach) | Up to 50 Nm³/h to rapidly flush any air ingress |
| N₂ purity requirement | Grade 4.0 minimum (99.99% N₂; O₂ <10 ppm; moisture <5 ppm) |

### Oxygen and Moisture Control

| Parameter | Normal | Alarm | Action |
|-----------|--------|-------|--------|
| O₂ concentration in cell | <20 ppm | >100 ppm | Increase N₂ purge rate |
| Moisture (dew point) | <−60 °C | >−40 °C | Investigate moisture source; dry N₂ purge |
| Cell pressure | −25 to −75 Pa | <−100 Pa or >0 Pa | Adjust N₂ supply or exhaust |

---

## 3. Concrete Construction Requirements

### Reinforcement
- All walls: minimum #8 rebar (25.4 mm) at 300 mm spacing each way, each face.
- Roof: minimum #8 rebar at 250 mm, top and bottom mats.
- Penetration sleeves: reinforce around sleeves with hoop bars to prevent cracking.

### Construction Joints
- Minimize construction joints in high-flux regions.
- Waterstop at all construction joints: 150 mm × 9 mm PVC waterstop centered in joint.
- All joints: pressure-grout with non-shrink grout before occupancy.

### Penetration Sealing Details

| Penetration type | Method |
|-----------------|--------|
| Pipe (≤4-in) | Annular gap filled: lead wool packing + Portland cement mortar plug |
| Pipe (>4-in) | Steel bellows sleeve welded to pipe; grout packed around bellows |
| Cable bundles | Multi-pin sealed connectors (Conax or equivalent); lead-filled annular gap |
| Duct (ventilation) | Butterfly damper rated for radiation/temperature; lead shutter for maintenance |
| Access door frame | Steel frame cast in place; door reveals sealed with compressible fire-resistant sealant |

---

## 4. Cell Drain and Contamination Control

| Feature | Specification |
|---------|--------------|
| Cell floor drain | 100 mm diameter Hastelloy-N floor drain at low point of heated floor |
| Drain leads to | Radioactive liquid waste sump (separate concrete sump, 1 m³) |
| Floor slope to drain | 10 mm per meter toward drain |
| Decontamination water collection | All floor drains tie back to radioactive waste sump |
| Spill containment | Cell walls and floor form secondary containment for full primary loop volume + 20% |
| Spill containment volume | ≥2,400 L (full primary loop 1,993 L × 1.2 factor) |

---

## 5. Crane Specifications

| Parameter | Value |
|-----------|-------|
| Crane type | Electric overhead traveling (EOT) bridge crane |
| Safe working load | 10,000 kg (10 tonnes) at hook |
| Span (bridge) | 7.0 m |
| Bay height (bottom of bridge to floor) | 5.5 m |
| Hook height (from floor at max lift) | 5.0 m |
| Bridge travel | 6.0 m (end-to-end of cell) |
| Trolley travel | Full 7.0 m span |
| Hoist speed | 1.2 m/min (fine) and 3.0 m/min (normal) |
| Bridge travel speed | 5 m/min |
| Control | Pendant cable; 24 V DC pendant; 10 m cable length |
| Motors | Explosion-proof; TEFC; 460 V 3-phase |
| Structural classification | ASME HST-1 Service Class 4 or equivalent |
| End stops | Hardened steel bumpers at both ends of bridge and trolley travel |

---

## 6. Lighting and Utilities in Cell

| Utility | Specification |
|---------|--------------|
| Normal lighting | 4× flood lights (explosion-proof IP67; remote aim); 200 W LED each |
| Emergency lighting | Battery-backed (2 h) fluorescent; 50 lux minimum at floor |
| Power outlets (maintenance) | 2× 120V AC GFCI; 1× 240V AC — only used when cell atmosphere is safe for human entry |
| Instrument air | 700 kPa dry air (−40°C dew point) distribution manifold; 6× outlet points |
| He supply (primary loop) | 700 kPa; 2× outlet points at primary loop |
| Floor drains | 1× main drain + 2× corner drains (all to rad waste sump) |
