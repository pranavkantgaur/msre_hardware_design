#!/usr/bin/env python3
"""
09 — Control Rods (ORNL-TM-728; CRS BOM)

Three Hastelloy-N clad control rods + one drive housing:
  - Clad OD 25.4 mm  wall 1.65 mm  active length 1422 mm
  - B₄C / Al₂O₃ pellets  23.6 mm dia × 12.7 mm height (112/rod)
  - Drive housing OD 73 mm  (3 rods, but model shows 1 rod + housing)
  - Total rod length 1448 mm including end caps
  - Drive shaft dia 19.05 mm in housing
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cadquery as cq
from render_utils import render_and_export

CLAD_OD   =  25.4
CLAD_WT   =   1.65
ROD_L     = 1448.0    # total length
ACTIVE_L  = 1422.0
PELLET_D  =  23.6
PELLET_H  =  12.7
DRIVE_OD  =  73.0
DRIVE_WT  =   7.0
DRIVE_H   = 500.0
SHAFT_D   =  19.05

def make_single_rod():
    clad_id = CLAD_OD - 2 * CLAD_WT
    # ── Clad tube ─────────────────────────────────────────────────────
    clad = (
        cq.Workplane("XY")
          .cylinder(ROD_L, CLAD_OD/2)
          .cut(cq.Workplane("XY").cylinder(ROD_L, clad_id/2))
    )
    # ── Pellet stack (5 representative pellets, not 112 for speed) ────
    n_show = 8
    z_start = -ACTIVE_L/2
    pellet_stack = cq.Workplane("XY")
    for i in range(n_show):
        z = z_start + i * (ACTIVE_L / n_show) + PELLET_H/2
        p = (
            cq.Workplane("XY")
              .workplane(offset=z - PELLET_H/2)
              .cylinder(PELLET_H, PELLET_D/2)
        )
        pellet_stack = pellet_stack.union(p)
    return clad.union(pellet_stack)

def make_drive_housing():
    drive_id = DRIVE_OD - 2 * DRIVE_WT
    housing = (
        cq.Workplane("XY")
          .workplane(offset=ROD_L/2)
          .cylinder(DRIVE_H, DRIVE_OD/2)
          .cut(cq.Workplane("XY")
                 .workplane(offset=ROD_L/2)
                 .cylinder(DRIVE_H, drive_id/2))
    )
    shaft = (
        cq.Workplane("XY")
          .workplane(offset=ROD_L/2)
          .cylinder(DRIVE_H + 200, SHAFT_D/2)
    )
    return housing.union(shaft)


def make_control_rod_assembly():
    import math
    rod = make_single_rod()
    housing = make_drive_housing()
    # Place 3 rods at 120° on r = 400 mm (matching vessel nozzle pattern)
    assembly = housing
    for angle_deg in [0, 120, 240]:
        a = math.radians(angle_deg)
        x = 200 * math.cos(a); y = 200 * math.sin(a)
        r = (
            cq.Workplane("XY")
              .transformed(offset=cq.Vector(x, y, 0))
              .add(make_single_rod().vals())
        )
        assembly = assembly.union(r)
    return assembly


if __name__ == "__main__":
    print("Building 09_control_rods …")
    cr = make_control_rod_assembly()
    render_and_export(cr, "09_control_rods",
                      title="09 — Control Rods (Hastelloy-N Clad, B₄C/Al₂O₃ Pellets)",
                      color="#c0a060", elev=20, azim=-55)
    print("Done.")
