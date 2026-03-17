.PHONY: validate lint check help

help:
	@echo "MSRE Hardware Design — available commands:"
	@echo "  make validate   Validate all BOM CSV files (column count + schema)"
	@echo "  make lint       Lint all markdown files (requires markdownlint-cli)"
	@echo "  make check      Run both validate and lint"

validate:
	@echo "=== Validating BOM CSV files ==="
	@python3 validation/validate_boms.py && echo "✅  All BOMs valid" || (echo "❌  BOM validation failed" && exit 1)

lint:
	@echo "=== Linting markdown files ==="
	@command -v markdownlint >/dev/null 2>&1 || { echo "markdownlint-cli not found. Run: npm install -g markdownlint-cli"; exit 1; }
	@markdownlint --config .markdownlint.json "**/*.md" --ignore node_modules && echo "✅  All markdown valid" || (echo "❌  Markdown lint failed" && exit 1)

check: validate lint
	@echo "✅  All checks passed"
