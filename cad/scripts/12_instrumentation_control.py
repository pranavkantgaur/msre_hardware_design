#!/usr/bin/env python3
"""
12 — Instrumentation & Control (ORNL-3832 / BOM IC-001 … IC-027)

Representative I&C hardware models:
  1. Neutron detector dry-well thimble: 50.8 mm OD × 1000 mm
  2. EM flowmeter body: Hastelloy-N tube section 114.3 mm OD × 300 mm
  3. Thermocouple assembly: 3.2 mm sheath 500 mm long
  4. Pressure transmitter body: 76.2 mm dia × 200 mm

Model renders the EM flowmeter body as primary component.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cadquery as cq
from render_utils import render_and_export

# EM flowmeter (salt service primary loop)
FM_OD  = 114.3; FM_WT  =  6.02; FM_L   = 300.0
FLANGE_OD = 165.1; FLANGE_T = 19.05

# Dry-well thimble
DW_OD  =  50.8; DW_WT  =  3.18; DW_L   = 1000.0

# TC sheath (Type N / Hastelloy-N)
TC_OD  =   3.2; TC_L   =  500.0

# Pressure transmitter
PT_OD  =  76.2; PT_H   =  200.0

def make_flowmeter():
    fm_id = FM_OD - 2 * FM_WT
    body = (
        cq.Workplane("XY")
          .cylinder(FM_L, FM_OD/2)
          .cut(cq.Workplane("XY").cylinder(FM_L, fm_id/2))
    )
    # flanges at each end
    for sign in (-1, 1):
        fl = (
            cq.Workplane("XY")
              .workplane(offset=sign * (FM_L/2 + FLANGE_T/2))
              .cylinder(FLANGE_T, FLANGE_OD/2)
              .cut(cq.Workplane("XY")
                     .workplane(offset=sign * (FM_L/2 + FLANGE_T/2))
                     .cylinder(FLANGE_T, fm_id/2))
        )
        body = body.union(fl)
    # electrode boss (simplified bump on side)
    boss = (
        cq.Workplane("YZ")
          .workplane(offset=FM_OD/2)
          .cylinder(30, 20)
    )
    body = body.union(boss)
    return body

def make_drywell():
    dw_id = DW_OD - 2 * DW_WT
    thimble = (
        cq.Workplane("XY")
          .cylinder(DW_L, DW_OD/2)
          .cut(cq.Workplane("XY").cylinder(DW_L, dw_id/2))
    )
    return thimble

def make_tc():
    return cq.Workplane("XY").cylinder(TC_L, TC_OD/2)

def make_pressure_tx():
    body = cq.Workplane("XY").cylinder(PT_H, PT_OD/2)
    cap  = (
        cq.Workplane("XY")
          .workplane(offset=-PT_H/2)
          .sphere(PT_OD/2 * 0.6)
    )
    return body.union(cap)

def make_ic_assembly():
    # Arrange side by side for a combined render
    fm   = make_flowmeter()
    dw   = (cq.Workplane("XY")
              .transformed(offset=cq.Vector(300, 0, 0))
              .add(make_drywell().vals()))
    tc   = (cq.Workplane("XY")
              .transformed(offset=cq.Vector(-250, 0, 0))
              .add(make_tc().vals()))
    pt   = (cq.Workplane("XY")
              .transformed(offset=cq.Vector(0, 250, 0))
              .add(make_pressure_tx().vals()))
    return fm.union(dw).union(tc).union(pt)


if __name__ == "__main__":
    print("Building 12_instrumentation_control …")
    ic = make_ic_assembly()
    render_and_export(ic, "12_instrumentation_control",
                      title="12 — I&C Assembly (EM Flowmeter + Dry-Well + TC + PT)",
                      color="#a0a0c0", elev=25, azim=-50)
    print("Done.")
