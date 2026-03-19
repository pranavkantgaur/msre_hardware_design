#!/usr/bin/env python3
"""
01 — Reactor Vessel (ORNL-TM-728 §3.2; ORNL MSRE film, 1966)

Hastelloy-N cylindrical pressure vessel with:
  - Cylindrical shell  OD 1410 mm  wall 12.7 mm  height 2134.6 mm
  - Upper removable 2:1 semi-ellipsoidal head  t = 28.6 mm (1-1/8-in cold-pressed plate
    per ORNL MSRE film, ORNL 1966; corrected from 19.05 mm)
  - Lower fixed 2:1 semi-ellipsoidal head  t = 28.6 mm (same)
  - Total assembled height ~2900 mm
  - Fuel-salt inlet nozzle  5-in SCH40 (141.3 mm OD) on lower head (per ORNL MSRE film)
  - Fuel-salt outlet nozzle 5-in SCH40 (141.3 mm OD) on upper head (per ORNL MSRE film)
  - Three control-rod nozzles 2-in SCH40 (60.3 mm OD) on upper head

Known simplifications vs. openmsr/msre OnShape model (see docs/openmsr_validation.md):
  - Uniform wall 12.7 mm — upper 406 mm of shell is 25.4 mm per ORNL-TM-3229 (for 84 inlet
    orifice holes); use WT_UPPER = 25.4 if fabrication-grade model needed
  - Inlet modelled as axial nozzle; actual MSRE has a 6-in tangential volute entry (ORNL-TM-3229)
  - Core-wall cooling annulus, core can, anti-swirl vanes, and strainer basket are excluded
  - Vessel OD discrepancy: ORNL-TM-728 → 1410 mm (55.5 in); ORNL-TM-3229 references
    a "standard 60-in. OD ASME flanged and dished head" — likely the flange OD, not shell OD.
    Our 1410 mm cylinder OD is retained pending primary-drawing verification.
"""
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cadquery as cq
from render_utils import render_and_export

# --- parameters (mm) ---
OD      = 1410.0
WT      = 12.7          # cylindrical shell wall
ID      = OD - 2 * WT
H_SHELL = 2134.6        # tan-to-tan
T_HEAD  = 28.6          # head wall thickness: 1-1/8-in per ORNL MSRE film (corrected from 19.05 mm)
# 2:1 ellipse crown depth = ID/4 (per ASME UG-32: h = D/4 where D is inside diameter)
H_OUTER = ID / 4        # outer crown depth ≈ 346.15 mm (corrected from OD/4)
H_INNER = H_OUTER - T_HEAD / 2   # inner crown depth

# Nozzle dimensions — 5-in SCH40 fuel nozzles per ORNL MSRE film (corrected from 4-in)
N_SALT_OD = 141.3; N_SALT_WT = 6.55; N_SALT_L = 200
N_ROD_OD  =  60.3; N_ROD_WT  = 3.91; N_ROD_L  = 200

N_PTS = 20   # arc resolution


def _ellipse_arc_pts(r_outer, h_outer, r_inner, h_inner, n):
    """
    Return closed 2D profile (XZ plane) for a semi-ellipsoidal shell head:
      outer quarter-ellipse (equator → crown)
      → axis from outer crown to inner crown
      → inner quarter-ellipse (crown → equator)
      (close() connects inner equator back to outer equator)
    """
    outer = [(r_outer * math.cos(math.pi / 2 * i / n),
              h_outer * math.sin(math.pi / 2 * i / n))
             for i in range(n)]          # stop one step before the axis
    inner = [((r_inner) * math.cos(math.pi / 2 * i / n),
              (h_inner) * math.sin(math.pi / 2 * i / n))
             for i in range(n)]
    inner_rev = list(reversed(inner))
    return (outer
            + [(0, h_outer)]             # outer crown on axis
            + [(0, h_inner)]             # inner crown on axis
            + inner_rev)                 # crown → equator


def make_head_upper():
    """Upper removable ellipsoidal head (faces +Z)."""
    profile = _ellipse_arc_pts(
        r_outer=OD / 2,
        h_outer=H_OUTER,
        r_inner=ID / 2,
        h_inner=H_INNER,
        n=N_PTS,
    )
    # Revolve around Z-axis; head sits above z = +H_SHELL/2
    head = (
        cq.Workplane("XZ")
          .transformed(offset=cq.Vector(0, 0, H_SHELL / 2))
          .polyline(profile)
          .close()
          .revolve(360, [0, 0, 0], [0, 0, 1])
    )
    return head


def make_head_lower():
    """Lower fixed ellipsoidal head (faces -Z)."""
    # Mirror: invert Z offsets
    profile = _ellipse_arc_pts(
        r_outer=OD / 2,
        h_outer=H_OUTER,
        r_inner=ID / 2,
        h_inner=H_INNER,
        n=N_PTS,
    )
    # Negate Z for lower head
    profile_lower = [(x, -z) for x, z in profile]
    head = (
        cq.Workplane("XZ")
          .transformed(offset=cq.Vector(0, 0, -H_SHELL / 2))
          .polyline(profile_lower)
          .close()
          .revolve(360, [0, 0, 0], [0, 0, 1])
    )
    return head


def make_vessel():
    # ── Cylindrical shell ──────────────────────────────────────────────
    shell = (
        cq.Workplane("XY")
          .cylinder(H_SHELL, OD / 2)
          .cut(cq.Workplane("XY").cylinder(H_SHELL, ID / 2))
    )

    # ── Heads ─────────────────────────────────────────────────────────
    shell = shell.union(make_head_upper()).union(make_head_lower())

    # ── Salt inlet nozzle (bottom, axial) ─────────────────────────────
    z_bot = -(H_SHELL / 2 + H_OUTER)
    inlet = (
        cq.Workplane("XY")
          .workplane(offset=z_bot - N_SALT_L / 2)
          .cylinder(N_SALT_L, N_SALT_OD / 2)
          .cut(cq.Workplane("XY")
                 .workplane(offset=z_bot - N_SALT_L / 2)
                 .cylinder(N_SALT_L, N_SALT_OD / 2 - N_SALT_WT))
    )

    # ── Salt outlet nozzle (top, axial) ───────────────────────────────
    z_top = H_SHELL / 2 + H_OUTER
    outlet = (
        cq.Workplane("XY")
          .workplane(offset=z_top + N_SALT_L / 2)
          .cylinder(N_SALT_L, N_SALT_OD / 2)
          .cut(cq.Workplane("XY")
                 .workplane(offset=z_top + N_SALT_L / 2)
                 .cylinder(N_SALT_L, N_SALT_OD / 2 - N_SALT_WT))
    )

    # ── Three control-rod nozzles on upper head (120° apart, r=400 mm) ─
    for angle_deg in [0, 120, 240]:
        a = math.radians(angle_deg)
        x = 400 * math.cos(a); y = 400 * math.sin(a)
        rod = (
            cq.Workplane("XY")
              .center(x, y)
              .workplane(offset=z_top + N_ROD_L / 2)
              .cylinder(N_ROD_L, N_ROD_OD / 2)
              .cut(cq.Workplane("XY")
                     .center(x, y)
                     .workplane(offset=z_top + N_ROD_L / 2)
                     .cylinder(N_ROD_L, N_ROD_OD / 2 - N_ROD_WT))
        )
        shell = shell.union(rod)

    vessel = shell.union(inlet).union(outlet)
    return vessel


if __name__ == "__main__":
    print("Building 01_reactor_vessel …")
    vessel = make_vessel()
    render_and_export(vessel, "01_reactor_vessel",
                      title="01 — Reactor Vessel (Hastelloy-N, 1410 mm OD)",
                      color="#5b8dd9", elev=25, azim=-50)
    print("Done.")

