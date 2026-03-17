#!/usr/bin/env python3
"""
07 — Freeze Valves (ORNL-TM-728 §3.9)

Passive freeze-valve spool piece in 2-in SCH40 drain line:
  - Tube OD 60.3 mm (2.375 in)  wall 3.91 mm
  - Frozen section length 152 mm
  - Electric heater coil wound around frozen zone
  - Air-cooling nozzle for fast freeze
  - Flanged at both ends for remote maintenance

Model shows a representative spool piece with flange pair.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cadquery as cq
from render_utils import render_and_export

TUBE_OD     =  60.3
TUBE_WT     =   3.91
FREEZE_L    = 152.0
TOTAL_L     = 500.0   # spool piece total length
FLANGE_OD   = 127.0   # flange OD (2-in 150# ASME B16.5)
FLANGE_T    =  22.4
HEATER_OD   =  76.2   # heater coil envelope
HEATER_T    =   7.9

def make_freeze_valve():
    tube_id = TUBE_OD - 2 * TUBE_WT

    # ── Main tube ─────────────────────────────────────────────────────
    tube = (
        cq.Workplane("XY")
          .cylinder(TOTAL_L, TUBE_OD/2)
          .cut(cq.Workplane("XY").cylinder(TOTAL_L, tube_id/2))
    )

    # ── Heater coil envelope (centred on frozen zone) ─────────────────
    heater = (
        cq.Workplane("XY")
          .cylinder(FREEZE_L + 40, HEATER_OD/2)
          .cut(cq.Workplane("XY").cylinder(FREEZE_L + 40, TUBE_OD/2))
    )

    # ── End flanges ───────────────────────────────────────────────────
    for z_off in (-TOTAL_L/2, TOTAL_L/2):
        sign = -1 if z_off < 0 else 1
        flange = (
            cq.Workplane("XY")
              .workplane(offset=z_off)
              .cylinder(FLANGE_T, FLANGE_OD/2)
              .cut(cq.Workplane("XY")
                     .workplane(offset=z_off)
                     .cylinder(FLANGE_T, tube_id/2))
        )
        tube = tube.union(flange)

    # ── Air-cooling nozzle (radial, on frozen zone) ───────────────────
    air_noz = (
        cq.Workplane("YZ")
          .workplane(offset=HEATER_OD/2)
          .cylinder(40, 12.7/2)
    )

    fv = tube.union(heater).union(air_noz)
    return fv


if __name__ == "__main__":
    print("Building 07_freeze_valves …")
    fv = make_freeze_valve()
    render_and_export(fv, "07_freeze_valves",
                      title="07 — Freeze Valve Spool Piece (2-in SCH40, Hastelloy-N)",
                      color="#7ab0d4", elev=25, azim=-50)
    print("Done.")
