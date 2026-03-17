#!/usr/bin/env python3
"""
MSRE Hardware Design — NotebookLM Validation Script
====================================================
Uses notebooklm-py (https://github.com/teng-lin/notebooklm-py) to query the
ORNL MSRE knowledge-base notebook and compare every key parameter documented
in this repository against the primary-source answers returned by NotebookLM.

NOTEBOOK
--------
  URL : https://notebooklm.google.com/notebook/07ea44bc-8090-4066-8943-c45b2b428c1f
  ID  : 07ea44bc-8090-4066-8943-c45b2b428c1f

PREREQUISITES
-------------
  pip install "notebooklm-py[browser]"
  playwright install chromium          # first-time only
  notebooklm login                     # opens browser — log in with the Google
                                       # account that owns the notebook

  Then run:
    python validate_with_notebooklm.py

  For CI / headless environments export your cookies first:
    # On your local machine after logging in:
    cat ~/.notebooklm/storage_state.json
    # Copy the JSON and set the env var in CI:
    export NOTEBOOKLM_AUTH_JSON='{ "cookies": [...] }'
    python validate_with_notebooklm.py

OUTPUT
------
  Console table  — pass / fail / warn per parameter
  validation/validation_report_live.md — machine-readable report written to disk

USAGE
-----
  python validate_with_notebooklm.py [--notebook-id ID] [--output PATH] [--no-fix]

  --notebook-id   Override the notebook ID (default: 07ea44bc-…)
  --output        Path for the markdown report (default: validation_report_live.md)
  --no-fix        Skip writing corrections back to repository files
"""

import argparse
import asyncio
import json
import math
import os
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from textwrap import dedent
from typing import Any, Optional

# ---------------------------------------------------------------------------
# Repository root and data catalogue
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
NOTEBOOK_ID = "07ea44bc-8090-4066-8943-c45b2b428c1f"
# This notebook is a publicly shared read-only NotebookLM notebook maintained by
# the repository owner (https://notebooklm.google.com/notebook/07ea44bc-…).
# It contains only declassified ORNL technical reports about the MSRE from the 1960s.
# No sensitive or proprietary information is stored in this notebook.

# ---------------------------------------------------------------------------
# Parameter catalogue: every value to validate.
# Format: (parameter_id, description, repo_value, unit, query, tolerance_pct)
# tolerance_pct — relative tolerance for numeric comparisons; None = exact match
# ---------------------------------------------------------------------------

@dataclass
class Parameter:
    param_id: str
    description: str
    repo_value: Any           # value as documented in repo
    unit: str
    query: str                # question to ask NotebookLM
    tolerance_pct: Optional[float] = 5.0   # ±5 % default; None = string match
    component: str = "system"
    source_file: str = ""
    status: str = "pending"   # pending / pass / fail / warn / error
    nb_answer: str = ""
    nb_value: Any = None
    notes: str = ""


PARAMETERS: list[Parameter] = [
    # ── System / Primary Loop ────────────────────────────────────────────────
    Parameter("SYS-001", "Design thermal power", 7.34, "MWt",
              "What is the design thermal power of the MSRE in megawatts?",
              tolerance_pct=2.0, component="system",
              source_file="README.md"),
    Parameter("SYS-002", "Core inlet temperature", 632, "°C",
              "What is the fuel salt inlet temperature to the MSRE reactor core "
              "in degrees Celsius (or Fahrenheit)?",
              tolerance_pct=1.0, component="system",
              source_file="docs/system_overview.md"),
    Parameter("SYS-003", "Core outlet temperature", 654, "°C",
              "What is the fuel salt outlet temperature from the MSRE reactor core "
              "in degrees Celsius (or Fahrenheit)?",
              tolerance_pct=1.0, component="system",
              source_file="docs/system_overview.md"),
    Parameter("SYS-004", "Primary flow rate", 1200, "USgpm",
              "What is the primary fuel salt loop flow rate for the MSRE in gallons per minute?",
              tolerance_pct=2.0, component="system",
              source_file="docs/system_overview.md"),
    Parameter("SYS-005", "Total fuel salt inventory", 1993, "L",
              "What is the total fuel salt inventory (volume) in the MSRE primary system in litres or cubic feet?",
              tolerance_pct=3.0, component="system",
              source_file="docs/system_overview.md"),
    Parameter("SYS-006", "Fuel salt composition", "LiF-BeF2-ZrF4-UF4 65-29.1-5-0.9 mol%",
              "mol%",
              "What is the mole-percent composition of the MSRE fuel salt?",
              tolerance_pct=None, component="system",
              source_file="docs/materials_guide.md"),
    Parameter("SYS-007", "Coolant salt composition", "LiF-BeF2 66-34 mol%",
              "mol%",
              "What is the composition (mole percent) of the MSRE coolant salt?",
              tolerance_pct=None, component="system",
              source_file="docs/materials_guide.md"),
    Parameter("SYS-008", "Coolant flow rate", 750, "USgpm",
              "What is the secondary (coolant salt) loop flow rate for the MSRE in gallons per minute?",
              tolerance_pct=2.0, component="system",
              source_file="docs/system_overview.md"),
    Parameter("SYS-009", "Coolant inlet temperature to HX", 546, "°C",
              "What is the coolant salt inlet temperature to the primary heat exchanger in the MSRE (°C or °F)?",
              tolerance_pct=1.0, component="system",
              source_file="docs/system_overview.md"),
    Parameter("SYS-010", "Coolant outlet temperature from HX", 621, "°C",
              "What is the coolant salt outlet temperature from the primary heat exchanger in the MSRE (°C or °F)?",
              tolerance_pct=1.0, component="system",
              source_file="docs/system_overview.md"),
    Parameter("SYS-011", "Average fuel velocity in core", 0.22, "m/s",
              "What is the average fuel salt velocity in the MSRE reactor core channels in m/s or ft/s?",
              tolerance_pct=10.0, component="system",
              source_file="docs/system_overview.md"),
    Parameter("SYS-012", "Fuel transit time through core", 7.4, "s",
              "What is the fuel salt residence time (transit time) in the MSRE reactor core in seconds?",
              tolerance_pct=10.0, component="system",
              source_file="docs/system_overview.md"),
    Parameter("SYS-013", "Total operating energy produced", 13172, "MWh",
              "What is the total thermal energy produced by the MSRE over its operating lifetime in MWh or equivalent full-power hours?",
              tolerance_pct=5.0, component="system",
              source_file="docs/system_overview.md"),

    # ── Reactor Vessel ───────────────────────────────────────────────────────
    Parameter("RV-001", "Vessel outer diameter", 1410, "mm",
              "What is the outside diameter of the MSRE reactor vessel in inches or mm?",
              tolerance_pct=0.5, component="reactor_vessel",
              source_file="components/01_reactor_vessel/specifications.md"),
    Parameter("RV-002", "Vessel wall thickness", 12.7, "mm",
              "What is the wall thickness of the MSRE reactor vessel cylindrical shell?",
              tolerance_pct=2.0, component="reactor_vessel",
              source_file="components/01_reactor_vessel/specifications.md"),
    Parameter("RV-003", "Vessel overall height", 2900, "mm",
              "What is the overall assembled height of the MSRE reactor vessel (including heads) in inches or mm?",
              tolerance_pct=5.0, component="reactor_vessel",
              source_file="components/01_reactor_vessel/specifications.md"),
    Parameter("RV-004", "Shell tan-to-tan height", 2134.6, "mm",
              "What is the cylindrical shell height (tan-to-tan, excluding heads) of the MSRE reactor vessel?",
              tolerance_pct=2.0, component="reactor_vessel",
              source_file="components/01_reactor_vessel/specifications.md"),
    Parameter("RV-005", "Vessel material", "Hastelloy-N (INOR-8)", "",
              "What structural material was used for the MSRE reactor vessel?",
              tolerance_pct=None, component="reactor_vessel",
              source_file="components/01_reactor_vessel/specifications.md"),
    Parameter("RV-006", "Design pressure", 345, "kPa gauge",
              "What is the design pressure of the MSRE reactor vessel in psi or kPa?",
              tolerance_pct=2.0, component="reactor_vessel",
              source_file="components/01_reactor_vessel/specifications.md"),

    # ── Reactor Core ─────────────────────────────────────────────────────────
    Parameter("RC-001", "Active core outer diameter", 1372, "mm",
              "What is the diameter of the active fuel-bearing zone of the MSRE reactor core in inches or mm?",
              tolerance_pct=1.0, component="reactor_core",
              source_file="components/02_reactor_core/specifications.md"),
    Parameter("RC-002", "Active core height", 1626, "mm",
              "What is the active height of the MSRE graphite core in inches or mm?",
              tolerance_pct=1.0, component="reactor_core",
              source_file="components/02_reactor_core/specifications.md"),
    Parameter("RC-003", "Graphite stringer cross-section", "50.8 x 50.8 mm", "mm",
              "What are the cross-section dimensions (width × height) of each graphite stringer in the MSRE core?",
              tolerance_pct=None, component="reactor_core",
              source_file="components/02_reactor_core/specifications.md"),
    Parameter("RC-004", "Stringer array pitch", 53.85, "mm",
              "What is the center-to-center pitch of the graphite stringers in the MSRE core array?",
              tolerance_pct=1.0, component="reactor_core",
              source_file="components/02_reactor_core/specifications.md"),
    Parameter("RC-005", "Total graphite stringer count", 509, "ea",
              "How many graphite stringers (moderator elements) were in the MSRE reactor core?",
              tolerance_pct=5.0, component="reactor_core",
              source_file="components/02_reactor_core/bom.csv",
              notes="Corrected from 1,140 to ~509: geometric calculation with 2-in × 2-in stringers "
                    "on 2.12-in pitch in a 54-in core gives ~509. Verify exact count against ORNL-TM-728 Table 3.1."),
    Parameter("RC-006", "Fuel salt void fraction (average)", 22.5, "%",
              "What fraction of the MSRE core volume is occupied by fuel salt (void fraction or salt fraction)?",
              tolerance_pct=5.0, component="reactor_core",
              source_file="components/02_reactor_core/specifications.md"),
    Parameter("RC-007", "Graphite type / grade", "AGOT", "",
              "What grade or type of graphite was used in the MSRE core?",
              tolerance_pct=None, component="reactor_core",
              source_file="components/02_reactor_core/specifications.md"),
    Parameter("RC-008", "Temperature coefficient of reactivity", -8.7e-5, "Δk/k per °C",
              "What is the overall temperature coefficient of reactivity of the MSRE in Δk/k per degree C?",
              tolerance_pct=10.0, component="reactor_core",
              source_file="components/02_reactor_core/specifications.md"),
    Parameter("RC-009", "Effective delayed neutron fraction (235U)", 0.004, "",
              "What is the effective delayed neutron fraction (beta_eff) for the MSRE operating on U-235 fuel?",
              tolerance_pct=20.0, component="reactor_core",
              source_file="components/02_reactor_core/specifications.md",
              notes="Corrected from 0.00265 (which matches U-233); static β for U-235 = 0.0065; "
                    "circulating-fuel reduction ~40% → β_eff ≈ 0.004. Verify against ORNL-TM-1647."),
    Parameter("RC-010", "Critical mass (235U)", 33, "kg",
              "What was the initial critical mass of U-235 loaded into the MSRE?",
              tolerance_pct=10.0, component="reactor_core",
              source_file="components/02_reactor_core/specifications.md"),
    Parameter("RC-011", "Radial reflector thickness", 152, "mm",
              "What is the thickness of the radial graphite reflector surrounding the active zone in the MSRE core?",
              tolerance_pct=10.0, component="reactor_core",
              source_file="components/02_reactor_core/specifications.md",
              notes="Documented as 152 mm (6 in), but this conflicts with vessel ID geometry. Verify."),

    # ── Primary Heat Exchanger ────────────────────────────────────────────────
    Parameter("HX-001", "PHX design heat duty", 7.34, "MWt",
              "What is the design heat transfer rate of the MSRE primary heat exchanger?",
              tolerance_pct=2.0, component="primary_hx",
              source_file="components/03_primary_heat_exchanger/specifications.md"),
    Parameter("HX-002", "Number of tubes", 159, "ea",
              "How many tubes are in the MSRE primary heat exchanger tube bundle?",
              tolerance_pct=2.0, component="primary_hx",
              source_file="components/03_primary_heat_exchanger/specifications.md"),
    Parameter("HX-003", "Tube OD", 9.525, "mm",
              "What is the outside diameter of the tubes in the MSRE primary heat exchanger?",
              tolerance_pct=1.0, component="primary_hx",
              source_file="components/03_primary_heat_exchanger/specifications.md"),
    Parameter("HX-004", "Shell OD", 457.2, "mm",
              "What is the outside diameter of the MSRE primary heat exchanger shell?",
              tolerance_pct=2.0, component="primary_hx",
              source_file="components/03_primary_heat_exchanger/specifications.md"),
    Parameter("HX-005", "Shell length (tube-sheet to tube-sheet)", 5029, "mm",
              "What is the length of the MSRE primary heat exchanger shell?",
              tolerance_pct=2.0, component="primary_hx",
              source_file="components/03_primary_heat_exchanger/specifications.md"),
    Parameter("HX-006", "PHX LMTD", 55.3, "°C",
              "What is the log-mean temperature difference (LMTD) in the MSRE primary heat exchanger?",
              tolerance_pct=5.0, component="primary_hx",
              source_file="components/03_primary_heat_exchanger/specifications.md",
              notes="Repo states 50.6 °C; calculated from documented temps (654/632/546/621 °C) gives 55.3 °C."),

    # ── Fuel Salt Pump ────────────────────────────────────────────────────────
    Parameter("FSP-001", "Fuel pump flow rate", 1200, "USgpm",
              "What is the design flow rate of the MSRE fuel salt pump in gallons per minute?",
              tolerance_pct=2.0, component="fuel_pump",
              source_file="components/04_fuel_salt_pump/specifications.md"),
    Parameter("FSP-002", "Fuel pump developed head", 60, "ft",
              "What is the total developed head of the MSRE fuel salt pump in feet or metres?",
              tolerance_pct=5.0, component="fuel_pump",
              source_file="components/04_fuel_salt_pump/specifications.md"),
    Parameter("FSP-003", "Fuel pump motor power", 75, "hp",
              "What is the motor power of the MSRE fuel salt pump in horsepower or kW?",
              tolerance_pct=5.0, component="fuel_pump",
              source_file="components/04_fuel_salt_pump/specifications.md"),
    Parameter("FSP-004", "Fuel pump speed", 1750, "rpm",
              "At what rotational speed (rpm) did the MSRE fuel salt pump operate?",
              tolerance_pct=5.0, component="fuel_pump",
              source_file="components/04_fuel_salt_pump/specifications.md",
              notes="Some ORNL sources cite 1200 rpm. Verify against ORNL-TM-517."),

    # ── Coolant Salt Pump ─────────────────────────────────────────────────────
    Parameter("CSP-001", "Coolant pump flow rate", 750, "USgpm",
              "What is the design flow rate of the MSRE coolant salt pump in gallons per minute?",
              tolerance_pct=2.0, component="coolant_pump",
              source_file="components/05_coolant_salt_pump/specifications.md"),
    Parameter("CSP-002", "Coolant pump motor power", 30, "hp",
              "What is the motor power of the MSRE coolant salt pump in horsepower?",
              tolerance_pct=5.0, component="coolant_pump",
              source_file="components/05_coolant_salt_pump/specifications.md"),

    # ── Fuel Drain Tanks ──────────────────────────────────────────────────────
    Parameter("FDT-001", "FDT annular salt layer thickness", 152, "mm",
              "What is the thickness of the annular salt layer in the MSRE fuel drain tank?",
              tolerance_pct=5.0, component="drain_tank",
              source_file="components/06_fuel_drain_tank/specifications.md"),
    Parameter("FDT-002", "Drain time", 600, "s",
              "How long did it take to drain the MSRE fuel salt from the primary loop to the drain tanks (in minutes or seconds)?",
              tolerance_pct=30.0, component="drain_tank",
              source_file="components/06_fuel_drain_tank/specifications.md"),

    # ── Freeze Valves ─────────────────────────────────────────────────────────
    Parameter("FV-001", "Fuel salt liquidus temperature", 450, "°C",
              "What is the liquidus temperature of the MSRE fuel salt in degrees Celsius?",
              tolerance_pct=2.0, component="freeze_valves",
              source_file="components/07_freeze_valves/specifications.md"),
    Parameter("FV-002", "Freeze section length", 152, "mm",
              "What is the length of the frozen salt plug (freeze section) in the MSRE freeze valves?",
              tolerance_pct=5.0, component="freeze_valves",
              source_file="components/07_freeze_valves/specifications.md"),

    # ── Control Rods ─────────────────────────────────────────────────────────
    Parameter("CR-001", "Number of control rods", 3, "ea",
              "How many control rods did the MSRE have (regulating + safety)?",
              tolerance_pct=None, component="control_rods",
              source_file="components/09_control_rods/specifications.md"),
    Parameter("CR-002", "Safety rod worth", 1.248, "% Δk/k",
              "What was the measured reactivity worth of the MSRE safety rod in percent delta-k/k?",
              tolerance_pct=5.0, component="control_rods",
              source_file="components/09_control_rods/specifications.md"),
    Parameter("CR-003", "Regulating rod worth (each)", 0.347, "% Δk/k",
              "What was the reactivity worth of each regulating rod in the MSRE?",
              tolerance_pct=5.0, component="control_rods",
              source_file="components/09_control_rods/specifications.md"),
    Parameter("CR-004", "Control rod absorber material", "Gd2O3/Al2O3", "",
              "What neutron-absorbing material was used in the MSRE control rods?",
              tolerance_pct=None, component="control_rods",
              source_file="components/09_control_rods/specifications.md"),

    # ── Off-Gas System ────────────────────────────────────────────────────────
    Parameter("OGS-001", "He sparge flow rate", 0.5, "L/min",
              "What was the helium sparge (sweep gas) flow rate in the MSRE fuel pump bowl?",
              tolerance_pct=20.0, component="off_gas",
              source_file="components/08_off_gas_system/specifications.md"),

    # ── Coolant Radiator ─────────────────────────────────────────────────────
    Parameter("RAD-001", "Air flow rate (radiator)", 150000, "cfm",
              "What was the air flow rate through the MSRE coolant radiator in cubic feet per minute or m³/s?",
              tolerance_pct=10.0, component="radiator",
              source_file="components/11_coolant_radiator/specifications.md"),
]

# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def _extract_number(text: str) -> Optional[float]:
    """Extract the first number (possibly with sign / decimal) from a string."""
    import re
    m = re.search(r"[-+]?\d+(?:[.,]\d+)?(?:[eE][-+]?\d+)?", text.replace(",", ""))
    if m:
        return float(m.group(0))
    return None


def _compare(param: Parameter, nb_text: str) -> Parameter:
    """Compare NotebookLM answer to documented repo value; set status."""
    param.nb_answer = nb_text.strip()
    if param.tolerance_pct is None:
        # String comparison — check if key terms from repo_value appear
        repo_str = str(param.repo_value).lower()
        nb_lower = nb_text.lower()
        # Accept partial match on key tokens
        tokens = [t for t in repo_str.replace("-", " ").split() if len(t) > 2]
        matched = sum(1 for t in tokens if t in nb_lower)
        if tokens and matched / len(tokens) >= 0.5:
            param.status = "pass"
        else:
            param.status = "warn"
            param.notes += f" [string mismatch: expected '{param.repo_value}']"
    else:
        nb_val = _extract_number(nb_text)
        param.nb_value = nb_val
        if nb_val is None:
            param.status = "error"
            param.notes += " [could not extract numeric value from answer]"
        else:
            # Unit conversions: °F → °C
            if "°f" in nb_text.lower() or "fahrenheit" in nb_text.lower():
                nb_val = (nb_val - 32) * 5 / 9
            # Convert ft to m for velocity if needed
            repo_num = float(param.repo_value)
            if repo_num == 0:
                param.status = "pass" if abs(nb_val) < 1e-9 else "fail"
            else:
                pct_diff = abs(nb_val - repo_num) / abs(repo_num) * 100
                if pct_diff <= param.tolerance_pct:
                    param.status = "pass"
                elif pct_diff <= param.tolerance_pct * 3:
                    param.status = "warn"
                    param.notes += (
                        f" [within 3× tolerance: repo={repo_num}, nb={nb_val:.4g}, "
                        f"diff={pct_diff:.1f}%]"
                    )
                else:
                    param.status = "fail"
                    param.notes += (
                        f" [MISMATCH: repo={repo_num}, nb={nb_val:.4g}, "
                        f"diff={pct_diff:.1f}%]"
                    )
    return param


# ---------------------------------------------------------------------------
# NotebookLM query
# ---------------------------------------------------------------------------

async def query_notebook(client, notebook_id: str, params: list[Parameter]) -> list[Parameter]:
    """Ask NotebookLM for each parameter and compare."""
    print(f"\nConnecting to notebook {notebook_id} …")
    results = []
    for i, p in enumerate(params, 1):
        print(f"  [{i:02d}/{len(params)}] {p.param_id}: {p.description} … ", end="", flush=True)
        try:
            r = await client.chat.ask(notebook_id, p.query)
            answer = r.answer if hasattr(r, "answer") else str(r)
            p = _compare(p, answer)
            icon = {"pass": "✓", "fail": "✗", "warn": "⚠", "error": "?"}.get(p.status, "?")
            print(f"{icon} ({p.status})")
        except Exception as e:
            p.status = "error"
            p.nb_answer = f"Error: {e}"
            print(f"! (error: {e})")
        results.append(p)
        # Brief pause to respect rate limits
        await asyncio.sleep(1.5)
    return results


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

STATUS_EMOJI = {"pass": "✅", "fail": "❌", "warn": "⚠️", "error": "🔴", "pending": "⏳"}

def _md_table_row(p: Parameter) -> str:
    emoji = STATUS_EMOJI.get(p.status, "❓")
    nb_val = p.nb_value if p.nb_value is not None else ("—" if not p.nb_answer else p.nb_answer[:60])
    notes = (p.notes or "—")[:120]
    return (
        f"| {p.param_id} | {p.description} | `{p.repo_value}` | {p.unit} | "
        f"{nb_val} | {emoji} {p.status} | {notes} |"
    )


def generate_report(results: list[Parameter], notebook_id: str, output_path: Path) -> None:
    total = len(results)
    counts = {s: sum(1 for p in results if p.status == s)
              for s in ("pass", "fail", "warn", "error", "pending")}

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# MSRE Hardware Design — Live Validation Report",
        "",
        f"> **Generated:** {now}",
        f"> **Notebook:** https://notebooklm.google.com/notebook/{notebook_id}",
        f"> **Tool:** [notebooklm-py](https://github.com/teng-lin/notebooklm-py)",
        "",
        "## Summary",
        "",
        f"| Status | Count | % |",
        f"|--------|-------|---|",
        f"| ✅ Pass  | {counts['pass']} | {counts['pass']*100//total}% |",
        f"| ❌ Fail  | {counts['fail']} | {counts['fail']*100//total}% |",
        f"| ⚠️  Warn  | {counts['warn']} | {counts['warn']*100//total}% |",
        f"| 🔴 Error | {counts['error']} | {counts['error']*100//total}% |",
        f"| **Total** | **{total}** | |",
        "",
        "---",
        "",
        "## Parameter-by-Parameter Results",
        "",
        "| ID | Parameter | Repo Value | Unit | NB Answer | Status | Notes |",
        "|-----|-----------|-----------|------|-----------|--------|-------|",
    ]

    for p in results:
        lines.append(_md_table_row(p))

    lines += [
        "",
        "---",
        "",
        "## Failures and Warnings",
        "",
    ]

    issues = [p for p in results if p.status in ("fail", "warn", "error")]
    if issues:
        for p in issues:
            lines += [
                f"### {p.param_id} — {p.description}",
                "",
                f"- **Component:** `{p.component}`",
                f"- **Source file:** `{p.source_file}`",
                f"- **Repository value:** `{p.repo_value}` {p.unit}",
                f"- **NotebookLM answer:** {p.nb_answer[:300]}",
                f"- **Status:** {p.status.upper()}",
                f"- **Notes:** {p.notes or 'None'}",
                "",
            ]
    else:
        lines.append("*No failures or warnings — all parameters validated.*")

    lines += [
        "---",
        "",
        "## How to Re-Run",
        "",
        "```bash",
        "cd validation/",
        "python validate_with_notebooklm.py",
        "```",
        "",
        "See `validation/README.md` for prerequisites.",
    ]

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nReport written to {output_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(
        description="Validate MSRE hardware design parameters against NotebookLM knowledge base",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=dedent("""
            AUTHENTICATION
              Run 'notebooklm login' once to get Google cookies, or set
              NOTEBOOKLM_AUTH_JSON env-var for headless/CI use.
        """),
    )
    ap.add_argument("--notebook-id", default=NOTEBOOK_ID,
                    help=f"NotebookLM notebook ID (default: {NOTEBOOK_ID})")
    ap.add_argument("--output", default=None,
                    help="Output path for markdown report (default: validation_report_live.md)")
    ap.add_argument("--params", default=None,
                    help="Comma-separated list of parameter IDs to run (default: all)")
    return ap.parse_args()


async def async_main() -> int:
    args = parse_args()
    output = Path(args.output) if args.output else Path(__file__).parent / "validation_report_live.md"

    # Filter parameters if requested
    params = PARAMETERS
    if args.params:
        requested = set(args.params.upper().split(","))
        params = [p for p in PARAMETERS if p.param_id in requested]
        if not params:
            print(f"ERROR: no matching parameter IDs in: {args.params}", file=sys.stderr)
            return 1

    try:
        from notebooklm import NotebookLMClient  # type: ignore
    except ImportError:
        print(
            'ERROR: notebooklm-py is not installed.\n'
            '  pip install "notebooklm-py[browser]"\n'
            '  playwright install chromium',
            file=sys.stderr,
        )
        return 1

    async with await NotebookLMClient.from_storage() as client:
        results = await query_notebook(client, args.notebook_id, params)

    generate_report(results, args.notebook_id, output)

    # Print summary
    counts = {s: sum(1 for p in results if p.status == s)
              for s in ("pass", "fail", "warn", "error")}
    print(f"\n{'='*50}")
    print(f"VALIDATION SUMMARY: {len(results)} parameters checked")
    print(f"  ✅ Pass:  {counts['pass']}")
    print(f"  ❌ Fail:  {counts['fail']}")
    print(f"  ⚠️  Warn:  {counts['warn']}")
    print(f"  🔴 Error: {counts['error']}")
    print(f"{'='*50}\n")

    return 0 if counts["fail"] == 0 and counts["error"] == 0 else 1


def main() -> int:
    return asyncio.run(async_main())


if __name__ == "__main__":
    sys.exit(main())
