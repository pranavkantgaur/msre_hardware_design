#!/usr/bin/env python3
"""
04 — Fuel Salt Pump (ORNL-TM-517 / ORNL-TM-728 §3.5)

Vertical centrifugal sump pump:
  - Pump bowl OD 609.6 mm  wall 9.53 mm  length 1829 mm
  - Impeller OD 203 mm, 6 blades
  - Vertical hollow shaft, cantilevered, no submerged bearings
  - Gas space (He) above salt surface in bowl
  - Hastelloy-N wetted surfaces
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cadquery as cq
from render_utils import render_and_export

# --- parameters (mm) ---
BOWL_OD   = 609.6
BOWL_WT   =   9.53
# Bowl height ≈ BOWL_OD (roughly cubic sump bowl);
# 1829 mm is the TOTAL pump assembly length (shaft + neck), not the bowl height
BOWL_H    = 609.6     # corrected from 1829 mm (total length): bowl ≈ one diameter tall
SHAFT_D   =   50.8    # shaft diameter (approximate)
IMP_OD    =  203.0
IMP_T     =   25.4    # impeller thickness
NECK_OD   =  168.3    # pump neck (riser tube) OD
NECK_WT   =    7.11
NECK_H    = 1829.0 - BOWL_H   # neck height so total = 1829 mm (spec total length)
DISCHARGE_OD = 141.3; DISCHARGE_WT = 6.55  # 5-in SCH40 per ORNL MSRE film (corrected from 4-in)

def make_pump():
    bowl_id = BOWL_OD - 2 * BOWL_WT

    # ── Bowl ───────────────────────────────────────────────────────────
    bowl = (
        cq.Workplane("XY")
          .cylinder(BOWL_H, BOWL_OD/2)
          .cut(cq.Workplane("XY").cylinder(BOWL_H, bowl_id/2))
    )

    # ── Bottom dome (hemispherical) ────────────────────────────────────
    dome_r = BOWL_OD / 2
    dome = (
        cq.Workplane("XY")
          .workplane(offset=-BOWL_H/2)
          .sphere(dome_r)
          .cut(cq.Workplane("XY")
                 .workplane(offset=-BOWL_H/2)
                 .cylinder(dome_r, dome_r))          # keep upper half
    )

    # ── Impeller (simplified flat disc) ───────────────────────────────
    impeller = (
        cq.Workplane("XY")
          .workplane(offset=-BOWL_H/2 + 120)
          .cylinder(IMP_T, IMP_OD/2)
          .cut(cq.Workplane("XY")
                 .workplane(offset=-BOWL_H/2 + 120)
                 .cylinder(IMP_T, SHAFT_D/2))        # shaft hole
    )

    # ── Shaft (cantilevered, running from impeller to top) ─────────────
    shaft_h = BOWL_H + NECK_H
    shaft = (
        cq.Workplane("XY")
          .workplane(offset=-BOWL_H/2 + 120)
          .cylinder(shaft_h, SHAFT_D/2)
    )

    # ── Pump neck / riser above bowl ──────────────────────────────────
    neck = (
        cq.Workplane("XY")
          .workplane(offset=BOWL_H/2)
          .cylinder(NECK_H, NECK_OD/2)
          .cut(cq.Workplane("XY")
                 .workplane(offset=BOWL_H/2)
                 .cylinder(NECK_H, NECK_OD/2 - NECK_WT))
    )

    # ── Discharge nozzle (radial, near bowl top) ──────────────────────
    disch = (
        cq.Workplane("YZ")
          .workplane(offset=BOWL_OD/2)
          .workplane(offset=0)
          .cylinder(200, DISCHARGE_OD/2)
          .cut(cq.Workplane("YZ")
                 .workplane(offset=BOWL_OD/2)
                 .cylinder(200, DISCHARGE_OD/2 - DISCHARGE_WT))
    )

    pump = bowl.union(impeller).union(shaft).union(neck).union(disch)
    return pump


if __name__ == "__main__":
    print("Building 04_fuel_salt_pump …")
    pump = make_pump()
    render_and_export(pump, "04_fuel_salt_pump",
                      title="04 — Fuel Salt Pump (Vertical Centrifugal, Hastelloy-N)",
                      color="#5b8dd9", elev=20, azim=-60)
    print("Done.")
