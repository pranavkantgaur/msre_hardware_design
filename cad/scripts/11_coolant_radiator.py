#!/usr/bin/env python3
"""
11 — Coolant Radiator (ORNL-TM-728 §3.11)

Air-cooled forced-convection finned-tube radiator:
  - Finned tubes: OD 25.4 mm  fin OD 50.8 mm  fin pitch ~25 mm
  - Bundle depth ~0.45 m (one tube row)
  - Headers: 200 × 200 mm square box  wall 9.53 mm
  - Inlet/outlet nozzles 3-in SCH40 (88.9 mm OD)
  - ~14 tubes per bundle width (representative model)

Model shows header box + representative tube/fin bundle.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cadquery as cq
from render_utils import render_and_export

TUBE_OD    =  25.4
FIN_OD     =  50.8
FIN_T      =   0.889
FIN_PITCH  =  25.4     # centre-to-centre
TUBE_PITCH =  60.0     # tube-to-tube, transverse
N_TUBES    =   8       # representative count (model)
TUBE_L     = 3000.0    # tube active length
HDR_W      =  200.0    # header cross-section
HDR_WT     =    9.53
HDR_L      = N_TUBES * TUBE_PITCH + TUBE_PITCH
NOZZLE_OD  =  88.9; NOZZLE_WT = 5.49; NOZZLE_L = 150

def make_radiator():
    # ── Headers (two: inlet and outlet) ──────────────────────────────
    hdr_id = HDR_W - 2 * HDR_WT
    headers = cq.Workplane("XY")
    for x_off in (-TUBE_L/2, TUBE_L/2):
        h = (
            cq.Workplane("YZ")
              .workplane(offset=x_off)
              .box(HDR_L, HDR_W, HDR_W)
              .cut(
                  cq.Workplane("YZ")
                    .workplane(offset=x_off)
                    .box(HDR_L, hdr_id, hdr_id)
              )
        )
        headers = headers.union(h)

    # ── Tube + fin bundle ─────────────────────────────────────────────
    n_fins_per_tube = int(TUBE_L / FIN_PITCH)
    bundle = cq.Workplane("XY")
    for i in range(N_TUBES):
        cy = (i - N_TUBES/2 + 0.5) * TUBE_PITCH
        # bare tube
        t = (
            cq.Workplane("XZ")
              .center(0, cy)
              .cylinder(TUBE_L, TUBE_OD/2)
              .cut(
                  cq.Workplane("XZ")
                    .center(0, cy)
                    .cylinder(TUBE_L, TUBE_OD/2 - 1.65))
        )
        # fins (every fin_pitch along tube axis, show 1 in 4 for speed)
        for fi in range(0, n_fins_per_tube, 4):
            fx = -TUBE_L/2 + fi * FIN_PITCH
            fin = (
                cq.Workplane("XZ")
                  .center(fx, cy)
                  .cylinder(FIN_T, FIN_OD/2)
                  .cut(
                      cq.Workplane("XZ")
                        .center(fx, cy)
                        .cylinder(FIN_T, TUBE_OD/2))
            )
            t = t.union(fin)
        bundle = bundle.union(t)

    # ── Inlet / outlet nozzles ────────────────────────────────────────
    nozzles = cq.Workplane("XY")
    for x_off, y_off in [(-TUBE_L/2 - NOZZLE_L/2, 0), (TUBE_L/2 + NOZZLE_L/2, 0)]:
        n = (
            cq.Workplane("XY")
              .workplane(offset=y_off)
              .transformed(offset=cq.Vector(x_off, 0, 0))
              .cylinder(NOZZLE_L, NOZZLE_OD/2)
              .cut(
                  cq.Workplane("XY")
                    .workplane(offset=y_off)
                    .transformed(offset=cq.Vector(x_off, 0, 0))
                    .cylinder(NOZZLE_L, NOZZLE_OD/2 - NOZZLE_WT))
        )
        nozzles = nozzles.union(n)

    radiator = headers.union(bundle).union(nozzles)
    return radiator


if __name__ == "__main__":
    print("Building 11_coolant_radiator …")
    rad = make_radiator()
    render_and_export(rad, "11_coolant_radiator",
                      title="11 — Coolant Radiator (Finned-Tube Air-Cooled, Hastelloy-N)",
                      color="#7ab0d4", elev=35, azim=-45)
    print("Done.")
