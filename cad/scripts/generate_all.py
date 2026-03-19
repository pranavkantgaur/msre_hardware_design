#!/usr/bin/env python3
"""
MSRE CAD Pipeline — Master Generator
=====================================
Runs all 12 component scripts in sequence, producing:
  - cad/step/<component>.step     (STEP AP214 exchange file)
  - cad/screenshots/<component>.png  (3-D rendered PNG)

Usage:
  python3 cad/scripts/generate_all.py [--component N]

Options:
  --component N   Run only component N (1-12).  Default: all.

Exit code 0 = all succeeded.  Non-zero = at least one failure.
"""
import os, sys, time, argparse, importlib.util, traceback
from pathlib import Path

SCRIPTS_DIR = Path(__file__).parent
REPO_ROOT   = SCRIPTS_DIR.parent.parent

COMPONENTS = [
    "01_reactor_vessel",
    "02_reactor_core",
    "03_primary_heat_exchanger",
    "04_fuel_salt_pump",
    "05_coolant_salt_pump",
    "06_fuel_drain_tank",
    "07_freeze_valves",
    "08_off_gas_system",
    "09_control_rods",
    "10_reactor_cell",
    "11_coolant_radiator",
    "12_instrumentation_control",
]


def run_component(name: str) -> tuple[bool, float]:
    """Run a component script as a subprocess.  Returns (success, elapsed_s)."""
    import subprocess
    script = SCRIPTS_DIR / f"{name}.py"
    t0 = time.time()
    try:
        result = subprocess.run(
            [sys.executable, str(script)],
            capture_output=False,
            check=True,
        )
        return True, time.time() - t0
    except subprocess.CalledProcessError:
        return False, time.time() - t0
    except Exception:
        traceback.print_exc()
        return False, time.time() - t0


def main():
    parser = argparse.ArgumentParser(description="Generate MSRE CAD models")
    parser.add_argument("--component", type=int, default=None,
                        help="Generate only component N (1-12)")
    args = parser.parse_args()

    if args.component:
        idx = args.component - 1
        if idx < 0 or idx >= len(COMPONENTS):
            print(f"ERROR: --component must be 1-{len(COMPONENTS)}")
            sys.exit(1)
        targets = [COMPONENTS[idx]]
    else:
        targets = COMPONENTS

    print(f"MSRE CAD Pipeline — generating {len(targets)} component(s)")
    print("=" * 60)

    results = {}
    for name in targets:
        print(f"\n▶  {name}")
        ok, elapsed = run_component(name)
        results[name] = (ok, elapsed)
        status = "✅" if ok else "❌"
        print(f"   {status} {elapsed:.1f} s")

    print("\n" + "=" * 60)
    passed  = sum(1 for ok, _ in results.values() if ok)
    failed  = len(results) - passed
    total_t = sum(t for _, t in results.values())
    print(f"Results: {passed}/{len(results)} passed  |  total time {total_t:.0f} s")

    if failed:
        print("\nFailed components:")
        for name, (ok, _) in results.items():
            if not ok:
                print(f"  ✗ {name}")
        sys.exit(1)

    # Print summary table
    print("\nGenerated files:")
    step_dir = REPO_ROOT / "cad" / "step"
    png_dir  = REPO_ROOT / "cad" / "screenshots"
    for name in targets:
        sp = step_dir / f"{name}.step"
        pp = png_dir  / f"{name}.png"
        sp_kb = sp.stat().st_size // 1024 if sp.exists() else 0
        pp_kb = pp.stat().st_size // 1024 if pp.exists() else 0
        print(f"  {name:<42} STEP {sp_kb:5} kB   PNG {pp_kb:4} kB")

    sys.exit(0)


if __name__ == "__main__":
    main()
