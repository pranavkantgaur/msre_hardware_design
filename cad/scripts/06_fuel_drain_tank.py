#!/usr/bin/env python3
"""
06 — Fuel Drain Tank (ORNL-TM-728 §3.7; ORNL-TM-1647)

Annular criticality-safe drain tank:
  - Outer cylinder OD 610 mm  wall 9.53 mm  height 762 mm
  - Inner (absorber) column OD 304 mm  — B₄C packed inside
  - Annular salt layer 128 mm thick
  - Top and bottom heads
  - Drain inlet / outlet nozzles
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cadquery as cq
from render_utils import render_and_export

OUTER_OD  = 610.0
OUTER_WT  =   9.53
TANK_H    = 762.0
INNER_OD  = 304.0  # B₄C absorber column
INNER_WT  =   9.53
HEAD_T    =  12.7
NOZZLE_OD =  60.3; NOZZLE_WT = 3.91; NOZZLE_L = 120

def make_fdt():
    outer_id = OUTER_OD - 2 * OUTER_WT
    # ── Outer annular shell ────────────────────────────────────────────
    outer = (
        cq.Workplane("XY")
          .cylinder(TANK_H, OUTER_OD/2)
          .cut(cq.Workplane("XY").cylinder(TANK_H, outer_id/2))
    )
    # ── Bottom head ────────────────────────────────────────────────────
    bot_head = (
        cq.Workplane("XY")
          .workplane(offset=-TANK_H/2 - HEAD_T/2)
          .cylinder(HEAD_T, outer_id/2)
    )
    # ── Top head ───────────────────────────────────────────────────────
    top_head = (
        cq.Workplane("XY")
          .workplane(offset=TANK_H/2 + HEAD_T/2)
          .cylinder(HEAD_T, outer_id/2)
    )
    # ── Inner absorber column (B₄C centre column) ────────────────────
    inner_col = (
        cq.Workplane("XY")
          .cylinder(TANK_H + 2*HEAD_T, INNER_OD/2)
          .cut(cq.Workplane("XY")
                 .cylinder(TANK_H + 2*HEAD_T, INNER_OD/2 - INNER_WT))
    )
    # B₄C fill shown as solid dark cylinder inside column
    b4c_fill = (
        cq.Workplane("XY")
          .cylinder(TANK_H, INNER_OD/2 - INNER_WT)
    )
    # ── Drain nozzle (bottom) ──────────────────────────────────────────
    drain_noz = (
        cq.Workplane("XY")
          .workplane(offset=-TANK_H/2 - HEAD_T - NOZZLE_L/2)
          .cylinder(NOZZLE_L, NOZZLE_OD/2)
          .cut(cq.Workplane("XY")
                 .workplane(offset=-TANK_H/2 - HEAD_T - NOZZLE_L/2)
                 .cylinder(NOZZLE_L, NOZZLE_OD/2 - NOZZLE_WT))
    )
    # ── Vent nozzle (top) ──────────────────────────────────────────────
    vent_noz = (
        cq.Workplane("XY")
          .workplane(offset=TANK_H/2 + HEAD_T + NOZZLE_L/2)
          .cylinder(NOZZLE_L, NOZZLE_OD/2)
          .cut(cq.Workplane("XY")
                 .workplane(offset=TANK_H/2 + HEAD_T + NOZZLE_L/2)
                 .cylinder(NOZZLE_L, NOZZLE_OD/2 - NOZZLE_WT))
    )
    fdt = (outer.union(bot_head).union(top_head)
                .union(inner_col).union(b4c_fill)
                .union(drain_noz).union(vent_noz))
    return fdt


if __name__ == "__main__":
    print("Building 06_fuel_drain_tank …")
    fdt = make_fdt()
    render_and_export(fdt, "06_fuel_drain_tank",
                      title="06 — Fuel Drain Tank (Annular, Criticality-Safe)",
                      color="#c07850", elev=30, azim=-55)
    print("Done.")
