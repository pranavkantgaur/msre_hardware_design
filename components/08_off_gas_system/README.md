# Component 08: Off-Gas System

## Overview

The off-gas system continuously removes and safely manages fission-product gases and other volatile species that are stripped from the circulating fuel salt by the helium sparge gas in the fuel salt pump bowl. It prevents radioactive gas accumulation in the primary loop gas space and manages the release of radioactive species to meet environmental and safety requirements.

**Primary Reference:** ORNL-TM-728, Section 3.10; ORNL-TM-4180

---

## Off-Gas Sources

| Source | Species | Activity Level |
|--------|---------|---------------|
| Noble gas fission products | ⁸⁵Kr, ⁸⁵ᵐKr, ⁸⁷Kr, ⁸⁸Kr, ¹³¹ᵐXe, ¹³³Xe, ¹³³ᵐXe, ¹³⁵Xe | Very high (curie level per minute) |
| Tritium (from ⁶Li) | T₂, THe | Moderate; permeates Hastelloy-N |
| Iodine (volatile) | ¹³¹I, ¹³²I, ¹³³I | High; partially retained in charcoal |
| Salt aerosol | UF₄, BeF₂ mist | Low; removed by filter |
| Helium (carrier) | He | Inert; clean |

---

## System Description

### Step 1: Helium Sparge in Pump Bowl
- Helium (dry, pure) is bubbled through the fuel salt in the pump bowl at ~0.5 L/min.
- Noble gases (Kr, Xe) dissolve in/partition to the gas phase; approximately 95% efficiency per pass.
- Stripped off-gas (He + fission product gases) exits through the off-gas nozzle on the pump bowl.
- Off-gas nozzle: 12.7 mm (0.5 in) OD Hastelloy-N tube.

### Step 2: Water-Cooled Condensation Trap
- Cools off-gas from ~640 °C to ~50 °C.
- Condensate (mainly water vapor and salt aerosol) collects in sump at bottom.
- **Material:** Hastelloy-N tube within water-cooled jacket.
- **Purpose:** Remove salt aerosol and condensable vapors before charcoal beds (water or salt would impair charcoal).

### Step 3: Primary Delay Bed (Room-Temperature Charcoal)
- Activated charcoal bed at room temperature.
- Xenon and krypton adsorb on charcoal; released slowly (delay time depends on krypton/xenon isotope and bed temperature).
- **Material:** Nuclear-grade coconut-shell activated charcoal.
- **Volume:** ~250 L (minimum); provide ≥10 half-life decay of ¹³³Xe (t₁/₂ = 5.25 d) before release.
- **Delay time for Xe (room temp charcoal):** ~50–70 days per 250 L for ¹³³Xe → satisfactory decay.
- **Bed dimensions:** 2 beds (series); each ~0.45 m diameter × 1.6 m long.
- **Material:** Carbon steel vessel with Hastelloy-N internal liner or full Hastelloy-N.

### Step 4: Secondary Delay Bed (Water-Cooled Charcoal — for ⁸⁵Kr Long-Term Retention)
- ⁸⁵Kr (t₁/₂ = 10.7 yr) cannot be adequately decayed — must be retained in charcoal for >10 years or processed.
- Water-cooled charcoal bed keeps charcoal at 10–15 °C to improve adsorption coefficient for Kr.
- **Volume:** ~750 L (provides >100 days retention of Kr at cooled conditions).
- **Vessel:** Horizontal cylindrical, water-jacketed, Hastelloy-N.

### Step 5: HEPA Filter
- Removes any residual particulate (charcoal fines, salt aerosol).
- **Material:** Sintered Hastelloy-N metal filter element (99.97% efficiency at 0.3 µm).
- **Housing:** Hastelloy-N.

### Step 6: Monitored Release (Stack)
- Off-gas that has passed through all beds and filters is monitored for radiation before release.
- Released via stack to atmosphere during normal operation (only noble gases at acceptable concentrations).

---

## Key Design Parameters

| Parameter | Value |
|-----------|-------|
| Sparge gas (He) flow rate | ~0.5 L/min (standard conditions) |
| Off-gas total flow at pump bowl | ~0.5 L/min + entrained fission gases |
| Off-gas line temperature (pump bowl) | ~640 °C |
| Off-gas line temperature (after trap) | ~50 °C |
| Primary charcoal bed volume | 250 L (minimum) |
| Secondary charcoal bed volume | 750 L |
| Operating pressure | Slightly above atmospheric (<5 kPa gauge) |
| ¹³³Xe decay factor before release | >10 half-lives (>99.9% decayed) |

---

## Off-Gas Line Piping

| Segment | Size | Material | Temperature |
|---------|------|----------|-------------|
| Pump bowl to condensation trap | 12.7 mm OD × 1.65 mm wall | Hastelloy-N | 640 → 50 °C |
| Cell penetration to off-gas cell | 12.7 mm OD × 1.65 mm wall | Hastelloy-N | ~50 °C |
| Trap to charcoal bed 1 | 25.4 mm OD × 2.41 mm wall | 316L SS | Ambient |
| Charcoal bed 1 to bed 2 | 25.4 mm OD × 2.41 mm wall | 316L SS | Ambient |
| Charcoal bed 2 to HEPA | 25.4 mm OD × 2.41 mm wall | 316L SS | Ambient |
| HEPA to monitor/stack | 50.8 mm OD | 316L SS | Ambient |

---

## Instrumentation

| Tag | Parameter | Sensor |
|-----|-----------|--------|
| FI-301 | He sparge gas flow | Rotameter or mass flow controller |
| PI-301 | Off-gas line pressure | Differential pressure transmitter |
| TI-301–TI-304 | Charcoal bed temperatures (4 zones) | Type K thermocouples |
| RI-301 | Off-gas line radiation (at pump bowl outlet) | Ion chamber |
| RI-302 | Stack effluent radiation | Continuous air monitor |
| AI-301 | ¹³³Xe activity in stack gas | NaI detector + analysis |

---

## Interfaces

| Interface | Connected To | Type |
|-----------|-------------|------|
| Off-gas inlet | Fuel salt pump bowl nozzle | 12.7 mm Hastelloy-N butt weld |
| He sparge supply | Helium supply manifold | 6.35 mm compression fitting |
| Stack outlet | Building ventilation exhaust | 50.8 mm SS flanged |
| Condensate drain | Radioactive liquid waste system | 12.7 mm SS tube |
| Charcoal bed drain | Radioactive solid waste | Removable spool piece |
