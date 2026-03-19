# MSRE Validation — NotebookLM Integration

This directory contains the tooling to **automatically validate** every key
hardware parameter documented in this repository against the primary-source ORNL
knowledge base hosted at:

> https://notebooklm.google.com/notebook/07ea44bc-8090-4066-8943-c45b2b428c1f

Validation uses [notebooklm-py](https://github.com/teng-lin/notebooklm-py) — an
unofficial Python client for Google NotebookLM — to query the indexed ORNL
reports and compare the answers against this repository's documented values.

---

## Files

| File | Purpose |
|------|---------|
| `validate_with_notebooklm.py` | Main validation script (queries NotebookLM, compares parameters, writes report) |
| `validation_report_live.md` | Auto-generated report from last successful run *(not present until first run)* |
| `README.md` | This file |

---

## Prerequisites

### 1 — Python packages

```bash
pip install "notebooklm-py[browser]"
playwright install chromium          # downloads ~130 MB Chromium binary
```

### 2 — Google authentication (one-time setup)

The validation script queries a private/shared Google NotebookLM notebook.
Authentication requires a real Google account that has access to the notebook.

```bash
notebooklm login
# A Chromium browser window opens — log in with your Google account.
# Cookies are saved to ~/.notebooklm/storage_state.json automatically.
```

> **Tip — verify auth is working:**
> ```bash
> notebooklm auth check --test
> ```

### 3 — CI / Headless environments

Copy your local `storage_state.json` and export it as an environment variable:

```bash
# On your local machine (after notebooklm login):
cat ~/.notebooklm/storage_state.json | base64   # copy output

# In CI (e.g. GitHub Actions), add as secret NOTEBOOKLM_AUTH_JSON:
export NOTEBOOKLM_AUTH_JSON='{ "cookies": [...] }'
python validate_with_notebooklm.py
```

For GitHub Actions, see the [notebooklm-py CI guide](https://github.com/teng-lin/notebooklm-py/blob/main/docs/configuration.md#cicd-configuration).

---

## Running the Validation

```bash
cd validation/

# Full validation (all parameters, ~45 questions × 1.5 s pause = ~70 s):
python validate_with_notebooklm.py

# Validate specific parameters only:
python validate_with_notebooklm.py --params SYS-001,RC-001,RC-005

# Write report to a custom path:
python validate_with_notebooklm.py --output /tmp/my_report.md

# Use a different notebook:
python validate_with_notebooklm.py --notebook-id <other-id>
```

---

## What Gets Validated

The script checks **47 parameters** across all 12 MSRE subsystems:

| Category | # params | Key checks |
|----------|----------|-----------|
| System / Primary Loop | 13 | Design power, temperatures, flow rates, salt compositions, operating history |
| Reactor Vessel | 6 | OD, wall thickness, height, material, design pressure |
| Reactor Core | 11 | Core diameter, height, stringer count, pitch, void fraction, reactivity parameters |
| Primary Heat Exchanger | 6 | Duty, tube count, geometry, LMTD |
| Fuel Salt Pump | 4 | Flow, head, motor power, speed |
| Coolant Salt Pump | 2 | Flow, motor power |
| Fuel Drain Tanks | 2 | Annular thickness, drain time |
| Freeze Valves | 2 | Liquidus temperature, freeze section length |
| Control Rods | 4 | Count, rod worths, absorber material |
| Off-Gas System | 1 | Helium sparge flow |
| Coolant Radiator | 1 | Air flow rate |

Pass/fail status is determined by comparing the NotebookLM answer to the
repository value within a configurable tolerance (default ±5 %).

---

## Interpreting Results

| Status | Meaning |
|--------|---------|
| ✅ Pass | Repo value matches NotebookLM answer within tolerance |
| ❌ Fail | Clear numeric or factual mismatch — **repository must be corrected** |
| ⚠️ Warn | Borderline mismatch (within 3× tolerance) or ambiguous answer — **review manually** |
| 🔴 Error | Network/auth failure or unparseable answer — **re-run after fixing auth** |

---

## Parameters Flagged for Manual Review

Even without running against NotebookLM, the following parameters were
identified as **likely incorrect** through mathematical consistency analysis
(see `docs/validation_report.md` for full derivations):

| Param ID | Issue |
|----------|-------|
| RC-001 | Core active diameter documented as 55.0 in (1397 mm) exceeds vessel ID (54.5 in = 1384.6 mm). Should be ~54.0 in (1372 mm). |
| RC-005 | 1,140 stringers cannot fit in a 54-in core at 2 in × 2 in on 2.12 in pitch (~509 fit geometrically). |
| RC-006 | Void fraction 22.5 % is inconsistent with 2-in stringer on 2.12-in pitch (calculation gives ~13.5 %). |
| RC-009 | β_eff = 0.00265 labelled "U-235" is more consistent with U-233. Expected ~0.004 for U-235 with circulation. |
| HX-006 | LMTD documented as 50.6 °C; calculation from documented temperatures gives 55.3 °C. |
| SYS-011 | Fuel velocity 0.37 m/s in system overview conflicts with 0.22 m/s calculated from geometry (already corrected). |
| SYS-012 | Transit time 8.5 s conflicts with 7.4 s from geometry (already corrected). |
| SYS-013 | "13,000 EFPH" is ambiguous — likely ~13,172 MWh total ≈ 1,795 EFPH at rated power (already clarified). |
| FSP-004 | Pump speed 1,750 rpm may be incorrect; some ORNL sources indicate 1,200 rpm. Verify against ORNL-TM-517. |

---

## Keeping Validation Fresh

Google session cookies expire every few weeks.  Refresh with:

```bash
notebooklm login
```

Then re-run the validation:

```bash
python validate_with_notebooklm.py
```

Commit `validation_report_live.md` to track validation history over time.
