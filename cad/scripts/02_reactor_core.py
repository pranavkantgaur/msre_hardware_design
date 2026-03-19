#!/usr/bin/env python3
"""
02 — Reactor Core (Graphite Moderator Assembly, ORNL-TM-728 §3.3)

AGOT nuclear-grade graphite stringer array inside the reactor vessel:
  - Active zone OD 1372 mm  height 1626.4 mm
  - 50.8 × 50.8 mm stringers on 53.85 mm pitch
  - Central 2-in control-rod thimbles (3 off)
  - Radial reflector ring ~76 mm thick
  - Axial reflector blocks 152 mm top + bottom

Model shows representative graphite assembly as:
  outer reflector cylinder + simplified stringer array cross-section.
"""
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cadquery as cq
from render_utils import render_and_export

# --- parameters (mm) ---
CORE_OD    = 1372.0
CORE_H     = 1626.4
REFL_T     = 76.0          # radial reflector thickness
AX_REFL    = 152.0         # axial reflector height
PITCH      = 53.85         # stringer centre-to-centre
STRINGER_W = 50.8          # stringer cross-section (square)
FUEL_CH    = 12.7          # fuel channel diameter (approx, 2 semi-circular grooves)

def make_core():
    # ── Outer graphite cylinder (reflector outer boundary) ─────────────
    total_h = CORE_H + 2 * AX_REFL
    outer = cq.Workplane("XY").cylinder(total_h, CORE_OD / 2)

    # ── Active zone inner cylinder (just for reference; use as body) ───
    # Model stringers as a representative 5×5 sub-array in Zone I centre
    # (full 509-stringer array is too heavy for a reference model; a
    #  representative cross-section conveys the geometry clearly)
    n_per_side = 5                     # representative array for render speed
    base_h     = CORE_H
    stringer_block = cq.Workplane("XY").workplane(offset=-base_h/2)
    for ix in range(-n_per_side, n_per_side + 1):
        for iy in range(-n_per_side, n_per_side + 1):
            cx = ix * PITCH
            cy = iy * PITCH
            r  = math.hypot(cx, cy)
            if r + STRINGER_W/2 > CORE_OD/2 - REFL_T:
                continue
            # stringer solid
            s = (cq.Workplane("XY")
                   .center(cx, cy)
                   .workplane(offset=-base_h/2)
                   .box(STRINGER_W, STRINGER_W, base_h, centered=(True, True, False)))
            # fuel channel (simplified cylindrical bore)
            bore = (cq.Workplane("XY")
                      .center(cx, cy)
                      .workplane(offset=-base_h/2)
                      .cylinder(base_h, FUEL_CH/2))
            stringer_block = stringer_block.union(s.cut(bore))

    # Combine: outer reflector shell + stringer array
    core = outer.cut(stringer_block).union(stringer_block)
    return core


if __name__ == "__main__":
    print("Building 02_reactor_core …")
    core = make_core()
    render_and_export(core, "02_reactor_core",
                      title="02 — Reactor Core (AGOT Graphite Stringer Assembly)",
                      color="#7a9e7e", elev=30, azim=-45)
    print("Done.")
