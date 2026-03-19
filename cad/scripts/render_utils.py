#!/usr/bin/env python3
"""
MSRE CAD Pipeline — shared render utilities.

Every component script imports this module for:
  - render_and_export(shape, name, out_dir, ...)  → writes STEP + PNG
  - REPO_ROOT / CAD_DIR constants
"""
import os
import sys
from pathlib import Path

import cadquery as cq
from cadquery import exporters

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ── paths ──────────────────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).parent.parent.parent   # msre_hardware_design/
CAD_DIR   = REPO_ROOT / "cad"
STEP_DIR  = CAD_DIR / "step"
PNG_DIR   = CAD_DIR / "screenshots"

for d in (STEP_DIR, PNG_DIR):
    d.mkdir(parents=True, exist_ok=True)


# ── helpers ───────────────────────────────────────────────────────────────────
def _tessellate(shape, tol=0.3):
    """Tessellate a CadQuery Assembly or Shape to numpy arrays."""
    if hasattr(shape, "val"):
        solid = shape.val()
    else:
        solid = shape
    verts_raw, tris = solid.tessellate(tol)
    verts = np.array([[v.x, v.y, v.z] for v in verts_raw], dtype=float)
    tris  = np.array([list(t) for t in tris], dtype=int)
    return verts, tris


def render_png(shape, title, out_png, elev=28, azim=-55, color="#4a90d9"):
    """Render a 3-D matplotlib screenshot from a CadQuery shape/workplane."""
    verts, tris = _tessellate(shape)
    if len(verts) == 0 or len(tris) == 0:
        print(f"  [warn] no geometry to render for {title}")
        return

    tri_verts = verts[tris]            # (N, 3, 3)
    mn, mx = verts.min(0), verts.max(0)
    span = mx - mn
    # guard against degenerate axis
    span = np.where(span < 1e-6, 1.0, span)

    fig = plt.figure(figsize=(7, 6), facecolor="#f0f4f8")
    ax  = fig.add_subplot(111, projection="3d")
    poly = Poly3DCollection(tri_verts, alpha=0.85, linewidths=0,
                            facecolor=color, edgecolor="none")
    ax.add_collection3d(poly)
    pad = 0.05
    ax.set_xlim(mn[0] - span[0]*pad, mx[0] + span[0]*pad)
    ax.set_ylim(mn[1] - span[1]*pad, mx[1] + span[1]*pad)
    ax.set_zlim(mn[2] - span[2]*pad, mx[2] + span[2]*pad)
    ax.view_init(elev=elev, azim=azim)
    ax.set_box_aspect(span)
    ax.set_axis_off()
    ax.set_title(title, fontsize=12, fontweight="bold", pad=10)
    # dimension annotation
    dims = f"~{span[0]:.0f} × {span[1]:.0f} × {span[2]:.0f} mm"
    ax.text2D(0.5, 0.01, dims, transform=ax.transAxes,
              ha="center", va="bottom", fontsize=8, color="#555")
    plt.tight_layout()
    plt.savefig(out_png, dpi=150, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    plt.close()
    print(f"  PNG → {out_png} ({os.path.getsize(out_png)//1024} kB)")


def export_step(shape, out_step):
    """Write a STEP AP214 file."""
    exporters.export(shape, str(out_step))
    print(f"  STEP → {out_step} ({os.path.getsize(out_step)//1024} kB)")


def render_and_export(shape, name, title=None, color="#4a90d9",
                      elev=28, azim=-55):
    """Export STEP and PNG for a component.  Returns (step_path, png_path)."""
    title = title or name
    step_path = STEP_DIR  / f"{name}.step"
    png_path  = PNG_DIR   / f"{name}.png"
    export_step(shape, step_path)
    render_png(shape, title, png_path, elev=elev, azim=azim, color=color)
    return step_path, png_path
