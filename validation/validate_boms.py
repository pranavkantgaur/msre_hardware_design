#!/usr/bin/env python3
"""
Validate all BOM CSV files in components/*/bom.csv.

Checks:
1. Exactly 10 columns per row
2. part_id matches expected pattern
3. unit is from allowed set
4. No completely empty rows

Exit code 0 = all pass, 1 = failures found.
"""
import csv
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
COMPONENTS_DIR = REPO_ROOT / "components"

REQUIRED_COLUMNS = [
    "part_id", "description", "material", "specification",
    "quantity", "unit", "dimension_1_mm", "dimension_2_mm",
    "dimension_3_mm", "notes"
]
ALLOWED_UNITS = {"ea", "m", "kg", "L", "set", "wall", "slab"}
PART_ID_PATTERN = re.compile(r"^[A-Z]+-[0-9]+[A-Z]?$")

failures = []

bom_files = sorted(COMPONENTS_DIR.glob("*/bom.csv"))
if not bom_files:
    print("ERROR: No bom.csv files found under components/")
    sys.exit(1)

for bom_path in bom_files:
    component = bom_path.parent.name
    with open(bom_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        # Check header columns
        if reader.fieldnames is None:
            failures.append(f"{component}: empty file")
            continue
        actual = list(reader.fieldnames)
        if actual != REQUIRED_COLUMNS:
            failures.append(
                f"{component}: header mismatch.\n"
                f"  Expected: {REQUIRED_COLUMNS}\n"
                f"  Got:      {actual}"
            )
            continue
        for i, row in enumerate(reader, start=2):  # row 1 = header
            pid = row.get("part_id", "").strip()
            unit = row.get("unit", "").strip()

            # Skip rows that are continuation notes (no part_id)
            if not pid:
                continue

            if not PART_ID_PATTERN.match(pid):
                failures.append(
                    f"{component} row {i}: part_id '{pid}' does not match [A-Z]+-[0-9]+"
                )

            if unit and unit not in ALLOWED_UNITS:
                failures.append(
                    f"{component} row {i} ({pid}): unit '{unit}' not in {ALLOWED_UNITS}"
                )

if failures:
    print(f"BOM validation FAILED — {len(failures)} issue(s):\n")
    for f in failures:
        print(f"  ✗ {f}")
    sys.exit(1)
else:
    print(f"BOM validation PASSED — {len(bom_files)} files checked, 0 issues.")
    sys.exit(0)
