#!/usr/bin/env python3
"""
10 — Reactor Cell (Biological Shielding, ORNL-TM-728)

Thick-walled concrete biological shielding enclosure:
  - Outer plan approx 7.3 m × 7.3 m
  - Wall thickness 1520 mm (baritic concrete)
  - Internal clear height ~5.5 m
  - Removable roof plug sections (RCL-002A)  ~1520 mm concrete
  - 15 t overhead bridge crane (RCL-008)
  - N₂ inert atmosphere, heated floor

Model: hollow rectangular cell box with wall thickness shown.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cadquery as cq
from render_utils import render_and_export

# Outer dimensions (mm)
OUTER_W  = 7300.0
OUTER_D  = 7300.0
OUTER_H  = 8000.0   # total (wall + floor + roof)
WALL_T   = 1520.0   # concrete wall thickness
FLOOR_T  =  600.0
ROOF_T   = 1520.0
# Crane runway height
CRANE_H  = 5500.0   # bay clear height (floor to bridge)
CRANE_W  = 5000.0   # runway width
CRANE_BEAM_H = 300

def make_cell():
    # ── Outer block ───────────────────────────────────────────────────
    outer = cq.Workplane("XY").box(OUTER_W, OUTER_D, OUTER_H)

    # ── Inner cavity ─────────────────────────────────────────────────
    inner_w = OUTER_W - 2 * WALL_T
    inner_d = OUTER_D - 2 * WALL_T
    inner_h = OUTER_H - FLOOR_T - ROOF_T
    inner = (
        cq.Workplane("XY")
          .workplane(offset=-OUTER_H/2 + FLOOR_T + inner_h/2)
          .box(inner_w, inner_d, inner_h)
    )
    cell = outer.cut(inner)

    # ── Removable roof plug (shown as separate slab sitting on top) ───
    plug = (
        cq.Workplane("XY")
          .workplane(offset=OUTER_H/2 + ROOF_T/2)
          .box(inner_w * 0.6, inner_d * 0.6, ROOF_T)
    )

    # ── Overhead crane bridge (simplified I-beam) ─────────────────────
    crane_z = -OUTER_H/2 + FLOOR_T + CRANE_H + CRANE_BEAM_H/2
    crane = (
        cq.Workplane("XY")
          .workplane(offset=crane_z)
          .box(CRANE_W, 400, CRANE_BEAM_H)
    )

    return cell.union(plug).union(crane)


if __name__ == "__main__":
    print("Building 10_reactor_cell …")
    cell = make_cell()
    render_and_export(cell, "10_reactor_cell",
                      title="10 — Reactor Cell (Baritic Concrete Biological Shielding)",
                      color="#b0a090", elev=30, azim=-40)
    print("Done.")
