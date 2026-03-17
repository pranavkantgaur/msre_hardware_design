# Component 06: Fuel Drain Tank System

## Overview

The fuel drain tank (FDT) system provides safe, subcritical storage for the entire fuel salt inventory during scheduled maintenance, emergency shutdowns, or any condition requiring fuel removal from the primary loop. It is a key passive safety system — gravity drains the fuel from the loop into subcritical geometry without operator action.

**Primary Reference:** ORNL-TM-728, Sections 3.7, 3.8; ORNL-TM-1647 (safety analysis)

---

## System Components

The fuel drain tank system consists of:
1. **Main Fuel Drain Tank (FDT)** — receives the full primary loop fuel salt inventory.
2. **Overflow Tank (OFT)** — catches any overflow from the FDT.
3. **Drain and fill lines** — Hastelloy-N piping with freeze valves.
4. **Heating system** — electric heat tracing to keep salt molten.
5. **Decay heat removal** — natural convection air cooling of exterior.

---

## Fuel Drain Tank (FDT)

### Criticality Safety Geometry
The FDT must remain subcritical under all conditions including:
- Full salt inventory
- Salt at any temperature (hot or cold)
- Complete moderation by water (worst-case accident scenario — water flooding of drain tank cell)

**Design approach:** Annular geometry with neutron-absorbing center column.

### Key Dimensions

| Parameter | Metric | Imperial |
|-----------|--------|----------|
| Tank outer diameter | ~1,219 mm | 48 in |
| Tank inner annulus ID | ~914 mm | 36 in |
| Annular salt thickness | ~152 mm | 6 in |
| Center column OD | ~610 mm | 24 in |
| Tank overall height | ~1,524 mm | 60 in |
| Salt volume capacity | ~2,271 L | 600 USgal (≥ full primary loop) |
| Hastelloy-N wall thickness | 9.53 mm | 0.375 in |

### Center Column (Poison/Moderator Control)
- The center column is filled with or plated with a neutron-absorbing material.
- **Material options used at MSRE:** Boron carbide (B₄C) packed pellets, or Boral sheet (boron carbide in aluminum matrix).
- The column prevents a critical geometry even under full water flooding of the annular salt zone.

### Materials

| Part | Material | Specification |
|------|----------|--------------|
| Outer cylindrical shell | Hastelloy-N | ASTM B622/B575, UNS N10003 |
| Inner cylindrical shell (annulus ID) | Hastelloy-N | ASTM B622/B575, UNS N10003 |
| Top head | Hastelloy-N | ASTM B575, UNS N10003 |
| Bottom head | Hastelloy-N | ASTM B575, UNS N10003 |
| Center column inner fill | B₄C pellets or Boral sheet | Minimum 10B loading per criticality analysis |
| Heat tracing | NiCr resistance wire or MI cable | >700 °C rated; zoned |

### Thermal Design
- At full load after shutdown: decay heat at t=0 is ~7% × 8 MWt = ~560 kW; at t=1 h it is ~120 kW.
- Natural convection of air over the tank exterior surface must remove this heat.
- Tank is not insulated on the exterior (to maximize heat rejection by natural convection).
- External air channels are arranged to promote chimney effect around the tank.
- Air temperature rise limit: <100 °C to prevent cell overpressure.
- Additional forced-air fans can be used if natural convection insufficient.

### Instrumentation
| Tag | Parameter | Sensor |
|-----|-----------|--------|
| TI-601 through TI-608 | Tank wall temperatures (8 locations) | Type K thermocouples, welded wells |
| LI-601 | Salt level in tank | Differential pressure |
| PI-601 | Tank headspace pressure | Pressure transmitter |
| RI-601 | Tank cell radiation | Gamma ion chamber |

---

## Overflow Tank (OFT)

### Purpose
- Captures any overflow from the main FDT if the salt level exceeds the design fill height.
- Also serves as a backup storage volume.

### Key Dimensions
| Parameter | Metric | Imperial |
|-----------|--------|----------|
| Tank volume | ~454 L | 120 USgal |
| Tank OD | ~610 mm | 24 in |
| Tank height | ~762 mm | 30 in |
| Wall thickness | 9.53 mm | 0.375 in |

### Materials
Same Hastelloy-N construction as FDT; annular geometry also (criticality safety).

---

## Drain and Fill Lines

### Drain Line (Primary Loop → FDT)
- **Size:** 2-in SCH40 Hastelloy-N pipe (60.3 mm OD)
- **Path:** Primary loop low point → Freeze valve FV-101 → FDT top nozzle
- **Slope:** Minimum 25 mm/m (0.3°) continuous downward slope to FDT — no pockets
- **Freeze valve:** FV-101 (see Component 07)
- **Time to drain:** Complete drain in <30 minutes from freeze valve full-open

### Fill Line (FDT → Primary Loop)
- **Size:** 2-in SCH40 Hastelloy-N pipe
- **Path:** FDT bottom nozzle → Freeze valve FV-103 → Primary loop low point
- **Operation:** Pump loop to operating temperature first; open FV-103; salt flows back by gravity-assist + pump suction

### Overflow Line (FDT → OFT)
- **Size:** 2-in SCH40 Hastelloy-N pipe
- **Path:** FDT top overflow nozzle (at design high level) → Freeze valve FV-104 → OFT

---

## Passive Drain (Emergency Safety Operation)

### Drain Sequence (Loss of Power)
1. Electric power to freeze valve FV-101 heaters is lost.
2. FV-101 salt plug begins to melt (heated by decay heat from nearby piping).
3. After ~5 minutes, salt plug is fully liquid; drain begins.
4. Fuel salt drains by gravity from primary loop through drain line to FDT.
5. FDT fills; k-eff of FDT remains <0.95 throughout.
6. Reactor is subcritical in FDT.
7. Decay heat is removed by natural convection air cooling.

### Safety Margins
- k-eff (FDT, fully loaded with fuel salt, flooded with water): <0.95 (required).
- k-eff (FDT, loaded with fuel salt, dry): <0.85 (typical MSRE value).
- Maximum tank wall temperature (decay heat, no active cooling): <760 °C (material limit).

---

## Interfaces

| Interface | Connected To | Type |
|-----------|-------------|------|
| FDT drain line inlet | Primary loop drain line via FV-101 | 2-in butt weld |
| FDT fill line outlet | Primary loop fill line via FV-103 | 2-in butt weld |
| FDT overflow outlet | Overflow tank via FV-104 | 2-in butt weld |
| FDT cover gas | He inert gas system | 12.7 mm compression fitting |
| FDT vent | Off-gas system | 12.7 mm tube |
| FDT exterior | Drain tank cell air space | Natural convection; no insulation |
