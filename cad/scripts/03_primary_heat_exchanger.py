#!/usr/bin/env python3
"""
03 — Primary Heat Exchanger (ORNL-TM-728 §3.4)

Shell-and-U-tube heat exchanger:
  - Shell OD 457.2 mm  wall 6.35 mm  length 5029 mm
  - 159 U-tubes, OD 9.525 mm  wall 0.875 mm
  - U-bend radius 25.4 mm min
  - Two tube sheets, inlet/outlet nozzles

Model: shell with representative tube bundle (12 visible tubes for clarity).
"""
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cadquery as cq
from render_utils import render_and_export

# --- parameters (mm) ---
SHELL_OD  = 457.2
SHELL_WT  = 6.35
SHELL_L   = 5029.0
TUBE_OD   = 9.525
TUBE_WT   = 0.875     # wall
TUBE_PITCH= 12.7      # triangular pitch (1.33 × OD = standard; corrected from 15.9)
UBEND_R   = 25.4
TS_THICK  = 76.2      # tube-sheet thickness (3.0 in per spec; corrected from 38.1)
# inlet / outlet nozzles
NOZZLE_OD = 114.3; NOZZLE_WT = 6.02; NOZZLE_L = 150

def make_phx():
    shell_id = SHELL_OD - 2 * SHELL_WT

    # ── Shell ──────────────────────────────────────────────────────────
    shell = (
        cq.Workplane("XY")
          .cylinder(SHELL_L, SHELL_OD / 2)
          .cut(cq.Workplane("XY").cylinder(SHELL_L, shell_id / 2))
    )

    # ── Tube sheets (two solid discs) ──────────────────────────────────
    for sign in (-1, 1):
        z0 = sign * (SHELL_L / 2 - TS_THICK / 2)
        ts = (cq.Workplane("XY")
                .workplane(offset=z0 - TS_THICK/2)
                .cylinder(TS_THICK, shell_id / 2))
        shell = shell.union(ts)

    # ── Representative tube bundle (12 tubes, 3-wide × 4-tall) ────────
    n_col, n_row = 3, 4
    for ic in range(n_col):
        for ir in range(n_row):
            cx = (ic - n_col/2 + 0.5) * TUBE_PITCH
            cy = (ir - n_row/2 + 0.5) * TUBE_PITCH
            # straight leg going up
            leg = (
                cq.Workplane("XY")
                  .center(cx, cy)
                  .cylinder(SHELL_L - 2 * TS_THICK, TUBE_OD / 2)
                  .cut(cq.Workplane("XY")
                         .center(cx, cy)
                         .cylinder(SHELL_L - 2 * TS_THICK, (TUBE_OD/2 - TUBE_WT)))
            )
            shell = shell.union(leg)

    # ── Inlet / outlet nozzles on shell (radial, mid-length) ──────────
    for sign, y_off in [(1, 0), (-1, 0)]:
        noz = (
            cq.Workplane("YZ")
              .workplane(offset=sign * SHELL_OD/2)
              .cylinder(NOZZLE_L, NOZZLE_OD/2)
              .cut(cq.Workplane("YZ")
                     .workplane(offset=sign * SHELL_OD/2)
                     .cylinder(NOZZLE_L, NOZZLE_OD/2 - NOZZLE_WT))
        )
        shell = shell.union(noz)

    return shell


if __name__ == "__main__":
    print("Building 03_primary_heat_exchanger …")
    phx = make_phx()
    render_and_export(phx, "03_primary_heat_exchanger",
                      title="03 — Primary Heat Exchanger (Hastelloy-N Shell & U-Tube)",
                      color="#c07850", elev=25, azim=-40)
    print("Done.")
