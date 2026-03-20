# Digital Twin Approaches for MSRE Fabrication Processes

**Date:** 2026-03-20
**Source transcript:** OpenUSD Insiders live stream — *"Building Agentic AI Powered Digital
Twins"* (Nvidia, Site Machine, Kinetic Vision, Microsoft, 2026)
**Scope:** Index of fabrication-process-relevant concepts extracted from the transcript,
mapped to MSRE component fabrication and assembly workflows.

---

## 1. Purpose

The transcript describes industrial practice for creating **operational digital twins** of
manufacturing shop floors using OpenUSD, Nvidia Omniverse, and agentic AI. While the
demonstration used a commercial bottling line, every technique described maps directly onto
the fabrication and assembly challenges present in MSRE component manufacture:

- Hastelloy-N pressure-part welding and machining (Components 01, 03, 04, 05, 06)
- Graphite moderator machining and assembly (Component 02)
- Remote-handled subassembly integration (all primary-loop components)
- Post-fabrication inspection and dimensional verification
- Operator situational awareness on a radioactive shop floor

---

## 2. Key Concepts Indexed from the Transcript

### 2.1 Acquire-Activate-Optimize (AAO) Process

| Phase | Transcript description | MSRE fabrication application |
|-------|------------------------|------------------------------|
| **Acquire** | Laser-scan the facility to ≤ 5 mm point-cloud accuracy, with zero disruption to ongoing operations; 10× faster than traditional survey methods | Scan the fabrication cell and each major sub-assembly jig; capture as-built geometry of the reactor vessel, core barrel, and HX shell before they are mated — enabling as-built vs. as-designed comparison |
| **Activate** | Ingest point-cloud into a 3D software pipeline; generate USD scene with metadata tagging; link to live sensor / IoT data streams | Convert fabrication-cell scan to USD scene; tag each fixture, weld station, and inspection point with `part_id` metadata matching the BOM (e.g. `RV-001`, `PHX-001`); attach thermocouple and dimensional-gauge feeds as USD attributes |
| **Optimize** | Run agentic AI over the enriched USD scene to surface recommendations — schedule adherence, throughput, anomaly alerts | Run AI inference over weld-sequence sensor logs to flag deviations from the qualified weld procedures (ORNL-TM-728, §4); detect fixture drift or machining tolerance exceedances in real time |

Source: Transcript — Jeremy (Kinetic Vision) describing the AAO framework and the
marketing video narration; deployment claim of 8–10× first-year ROI with ≤ 3-month payback.

---

### 2.2 OpenUSD as the 3D Integration Layer

The transcript identifies USD files enriched with ID metadata ("syntactical sugar" — Sashi,
Microsoft/Nvidia) as the correlation key between 3D geometry and live IoT data streams.
For MSRE fabrication this means:

- Every `cad/step/*.step` file exported from `cad/scripts/` should map 1-to-1 to a USD
  scene in a fabrication-monitoring pipeline.
- The `part_id` field in each `bom.csv` (e.g. `RV-001`) is the natural candidate for the
  USD prim path `/World/Components/RV_001`.
- USD attributes can carry material specification references (e.g. `msre:spec = "ORNL-TM-728 §3.2"`)
  alongside live sensor values, providing operators with both the design authority and the
  real-time measurement in the same interface.

Architecture excerpt from transcript (Sashi, Microsoft/Nvidia):
> *"The USD files that we create in Azure blob storage with the 3D data, we enrich them
> with ID information and other metadata … and that's what's brought into Omniverse Kit
> and provided to the front end … to map between the data sources coming in from Fabric
> to the data source in Omniverse."*

---

### 2.3 Operational Digital Twin Architecture Pattern

The transcript presents a reference architecture (demoed at Microsoft Ignite and later
deployed at Coca-Cola Consolidated):

```text
Edge (shop floor)          Cloud staging              Visualization front-end
─────────────────          ─────────────              ──────────────────────
PLC / sensor data    →  Azure IoT Operations    →  Microsoft Fabric RT Intel  →  Omniverse Kit
                         ARC-enabled Kubernetes     Azure Functions               streaming
Laser scan / USD    →  Azure Blob Storage      →  (enriched USD correlation)  →  Power BI overlay
assets
```

**MSRE fabrication mapping:**

| Architecture node | MSRE fabrication equivalent |
|-------------------|------------------------------|
| PLC / sensor data | Dimensional gauges, weld monitors, thermocouple feeds at each machining and assembly station |
| Azure IoT Operations / ARC Kubernetes | Facility data-acquisition system; could use any equivalent edge-compute platform |
| Azure Blob Storage (USD assets) | `cad/step/` STEP files converted to USD with BOM metadata embedded |
| Microsoft Fabric RT Intelligence | Fabrication quality management system (QMS); tracks dimensional records against specifications |
| Omniverse Kit streaming | 3D visualization of the fabrication cell, showing real-time status of each component sub-assembly |
| Power BI overlay | Fabrication dashboard: weld pass counts, dimensional deviations, material traceability records |

The transcript specifically notes this is an **open-source accelerator** pattern (Drew,
Microsoft):
> *"Post-Ignite we posted an open source accelerator repo … and then site machine got
> involved … and they took it and ran with it."*

---

### 2.4 Agentic AI for Process Recommendations

Site Machine's industrial AI platform (Charu Kaluri, Site Machine) targets:
- **Line throughput increase** — maximise production rate
- **Schedule adherence** — minimise fabrication delays
- **Machine efficiency / availability** — maximise equipment utilisation
- Recommendations generated *at the point of consumption* against the 3D layer, adapting to varying conditions in real time

MSRE fabrication equivalents:
- Alert when a weld-joint dimensional record deviates from the as-designed geometry before
  the next operation is started (preventing downstream rework)
- Flag when a Hastelloy-N heat (melt batch) is used across multiple safety-critical parts
  without traceability record, triggering a material-review hold
- Recommend revised machining sequence when core graphite stringer inventory drops below
  the 617-stringer minimum confirmed in ORNL-TM-3039 (see `components/02_reactor_core/bom.csv`)

---

### 2.5 Immersive 3D Visualization for Operator Situational Awareness

The transcript emphasises that large production lines are physically impossible to observe
end-to-end from any single vantage point:
> *"If you actually go to these plants, you literally can't see a couple of machines away
> from you."* (Charu Kaluri, Site Machine)

This exactly describes the MSRE reactor cell (Component 10): once major sub-assemblies are
installed inside the biological shielding, operators work through hatches and remote-handling
equipment with no direct line of sight to most of the primary circuit. A 3D immersive twin
of the reactor cell, enriched with thermocouple / level-gauge / flow-meter data, would give
the entire facility team — operations, maintenance, radiological protection — a common
operating picture.

The transcript records a 5 mm scan resolution figure (marketing video narration):
*"scanning your facility in stunning detail … [zero disruption] … 5 millimetre …"*

For MSRE-scale components (vessel OD ≈ 1410 mm, reference ORNL-TM-728) a 5 mm point-cloud
resolution is sufficient to verify external dimensional compliance against the procurement
specifications in `components/*/specifications.md`.

---

### 2.6 60-Day Deployment and Phased Approach

The transcript gives an explicit deployment timeline (marketing video): *"In just 60 days,
we uncover 8 to 10 times first-year ROI with payback in less than three months."*

A phased approach for MSRE fabrication digital twin:

| Phase | Duration | Deliverable |
|-------|----------|-------------|
| 1 — Acquire | Weeks 1–2 | Laser-scan fabrication cell; import existing `cad/step/` files as USD base scene |
| 2 — Activate | Weeks 3–6 | Enrich USD prims with `part_id` / spec references from `bom.csv`; connect dimensional-gauge and weld-monitor feeds |
| 3 — Optimize | Weeks 7–12 | Deploy agentic AI layer for real-time anomaly detection; integrate fabrication QMS records into dashboard |
| 4 — Scale | Post-week 12 | Replicate baseline twin across all 12 component fabrication shops |

---

## 3. Applicable Components and Specifications

The following components from the MSRE BOM have the most direct relevance to the
fabrication-twin workflow described in the transcript:

| Component | `part_id` prefix | Key fabrication challenge | Digital-twin monitoring value |
|-----------|------------------|---------------------------|-------------------------------|
| 01 Reactor Vessel | `RV-` | Hastelloy-N deep-groove GTAW welds; 55.5 in OD shell roundness | Weld distortion monitoring; wall-thickness scans post-weld |
| 02 Reactor Core | `RC-` | 617 graphite stringers machined to tight tolerances | Stringer dimensional records; assembly sequence tracking |
| 03 Primary Heat Exchanger | `PHX-` | U-tube bundle fabrication; tube-sheet drilling (341 holes, 12.7 mm pitch) | Tube-sheet drill-pattern verification against `PHX-003` spec |
| 04 Fuel Salt Pump | `FSP-` | Impeller casting + machining; hydraulic test | As-built bowl geometry vs. design; seal face run-out |
| 05 Coolant Salt Pump | `CSP-` | Same as FSP; separate Hastelloy-N heat certification | Material traceability for coolant-side parts |
| 06 Fuel Drain Tank | `FDT-` | Large-diameter thin-wall vessel; internal baffle welding | Post-weld dimensional survey; baffle alignment |
| 10 Reactor Cell | `RCL-` | 1.2 m-thick concrete bioshield; roof plug (≈ 22 t) crane lift | Crane SWL margin monitoring; plug seating gap verification |

---

## 4. Technology Stack Intersection with This Repository

The transcript's technology stack intersects with tools already referenced in this repo:

| Transcript technology | Repository touchpoint |
|-----------------------|-----------------------|
| OpenUSD / Omniverse Kit | `cad/scripts/*.py` produce STEP files; STEP → USD conversion is the next pipeline step. The `part_id` BOM column is the linking key for USD prim metadata. |
| CadQuery (used by Kinetic Vision pipeline, per industry standard) | `cad/scripts/*.py` are CadQuery parametric models — compatible with STEP export to USD pipelines |
| Agentic AI for manufacturing | Alignment with `bom_review/` multi-agent BOM reviews produced by msr-gstack; same agentic pattern applied to fabrication monitoring |
| Azure Blob Storage (USD assets) | Consistent with cloud-hosted `cad/step/` artefacts in CI/CD |

---

## 5. What the Transcript Does Not Cover

The following MSRE-specific fabrication concerns are **not** addressed by the transcript
and must continue to rely on ORNL primary sources:

| Topic | Required source |
|-------|----------------|
| Hastelloy-N qualified weld procedures for salt-wetted surfaces | ORNL-TM-728, §4; ORNL-3700 |
| Fluoride-salt cleaning and pre-service conditioning procedures | ORNL-TM-1978 |
| Graphite surface-treatment requirements (anti-permeation furfuryl alcohol impregnation) | ORNL-TM-728, §3.3; ORNL-3674 |
| Radiological contamination control during remote maintenance | ORNL-TM-1647 safety analysis |
| Criticality safety controls during enriched-uranium component assembly | ORNL-TM-1647 |

⚠️ Any AI-generated fabrication recommendation must be reviewed against the above ORNL
sources before implementation. Do not weaken safety margins or criticality controls.

---

## 6. References

| Source | Description |
|--------|-------------|
| OpenUSD Insiders live stream, 2026 | *"Building Agentic AI Powered Digital Twins"* — Nvidia, Site Machine, Kinetic Vision, Microsoft. Source transcript for this document. |
| ORNL-TM-728 | MSRE Design and Operations Report, Part I — master dimensional reference for all components |
| ORNL-TM-3039 | MSRE Operations Report Jan–Jun 1968 — confirms 617 graphite stringers |
| ORNL-3700 | Hastelloy Alloy N: Development and Use in Molten Salt Reactors — weld and fabrication data |
| ORNL-TM-1978 | Summary of MSRE Fuel-Salt Flush and Drain Operations — pre-service procedures |
| ORNL-TM-1647 | MSRE Safety Analysis — criticality and radiological controls |
| ORNL-3674 | MSRE Core Graphite: Irradiation-Induced Changes — graphite treatment requirements |
| openmsr/msre | <https://github.com/openmsr/msre> — independent CAD and OpenMC validation source |
