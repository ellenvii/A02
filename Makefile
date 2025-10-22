SHELL := /bin/bash

MODULES = dice dice_hand game highscore histogram intelligence main player shell
DOCS_DIR = docs
UML_DIR = $(DOCS_DIR)/uml
PYTHON = ./.venv/bin/python
PYREVERSE = ./.venv/bin/pyreverse
export PYTHONPATH := .

.PHONY: docs uml site clean preview check-venv

check-venv:
	@test -x $(PYTHON) || (echo "❌ No venv python at $(PYTHON)"; \
	 echo "👉 Run: python3 -m venv .venv && source .venv/bin/activate && pip install pylint"; \
	 exit 1)

docs: check-venv
	@mkdir -p $(DOCS_DIR)
	@for m in $(MODULES); do \
		echo "📚 $$m"; \
		$(PYTHON) -m pydoc -w $$m >/dev/null 2>&1 || echo "⚠️  skipped $$m"; \
		[ -f "$$m.html" ] && mv "$$m.html" $(DOCS_DIR)/ || true; \
	done
	@echo "<html><body><h1>A02 Docs</h1><ul>" > $(DOCS_DIR)/index.html
	@for m in $(MODULES); do echo "<li><a href='$$m.html'>$$m</a></li>" >> $(DOCS_DIR)/index.html; done
	@echo "</ul></body></html>" >> $(DOCS_DIR)/index.html
	@echo "✅ Docs in $(DOCS_DIR)/"

uml: check-venv
	@mkdir -p $(UML_DIR)
	@$(PYREVERSE) -o svg -p A02 -A -S -f ALL $(MODULES) >/dev/null 2>&1 || true
	@mv -f classes_A02.svg packages_A02.svg $(UML_DIR)/ 2>/dev/null || echo "ℹ️  No UML created."
	@echo "✅ UML in $(UML_DIR)/"

site: docs uml
	@echo "🎉 Built full documentation site!"

preview:
	@open $(DOCS_DIR)/index.html

clean:
	@rm -rf $(DOCS_DIR) *.html
	@echo "🧹 Cleaned."
