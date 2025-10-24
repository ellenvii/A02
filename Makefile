#!/usr/bin/env make

# Python command (change if needed)
PYTHON ?= python3

# Print colored messages
MESSAGE = printf "\033[32;01m---> $(1)\033[0m\n"

# All top-level python modules (exclude tests)
MODULES := $(filter-out test_%.py,$(wildcard *.py))

# Default rule
all: codestyle test doc

# ---------------------------------------------------------
# Setup virtual environment and dependencies
version:
	@printf "Currently using executable: $(PYTHON)\n"
	which $(PYTHON)
	$(PYTHON) --version

venv:
	[ -d .venv ] || $(PYTHON) -m venv .venv
	@printf "Now activate the Python virtual environment.\n"
	@printf "On Unix/Mac, run:\n"
	@printf ". .venv/bin/activate\n"

install:
	$(PYTHON) -m pip install -r requirements.txt

installed:
	$(PYTHON) -m pip list

# ---------------------------------------------------------
# Cleanup rules
clean:
	@$(call MESSAGE,$@)
	rm -f .coverage *.pyc
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf htmlcov

clean-doc: clean
	@$(call MESSAGE,$@)
	rm -rf doc

clean-all: clean clean-doc
	@$(call MESSAGE,$@)
	rm -rf .venv

# ---------------------------------------------------------
# Linting / Code quality
pylint:
	@$(call MESSAGE,$@)
	-$(PYTHON) -m pylint dice.py dice_hand.py game.py highscore.py histogram.py intelligence.py main.py player.py shell.py

flake8:
	@$(call MESSAGE,$@)
	-$(PYTHON) -m flake8 .

lint: flake8 pylint

# ---------------------------------------------------------
# Code formatting
black:
	@$(call MESSAGE,$@)
	$(PYTHON) -m black .

codestyle: black

# ---------------------------------------------------------
# Testing and coverage using pytest
pytest:
	@$(call MESSAGE,$@)
	$(PYTHON) -m pytest -v

coverage:
	@$(call MESSAGE,$@)
	$(PYTHON) -m pytest --cov=. --cov-report=term-missing --cov-report=html

test: lint pytest

# ---------------------------------------------------------
# Documentation
pdoc:
	@$(call MESSAGE,$@)
	$(PYTHON) -m pdoc -o doc/pdoc $(MODULES)

pyreverse:
	@$(call MESSAGE,$@)
	install -d doc/pyreverse
	pyreverse *.py -a1 -s1
	dot -Tpng classes.dot -o doc/pyreverse/classes.png
	dot -Tpng packages.dot -o doc/pyreverse/packages.png
	rm -f classes.dot packages.dot

doc: pdoc pyreverse

# ---------------------------------------------------------
# Software metrics
radon-cc:
	@$(call MESSAGE,$@)
	radon cc --show-complexity --average .

radon-mi:
	@$(call MESSAGE,$@)
	radon mi --show .

radon-raw:
	@$(call MESSAGE,$@)
	radon raw .

radon-hal:
	@$(call MESSAGE,$@)
	radon hal .

cohesion:
	@$(call MESSAGE,$@)
	cohesion --directory .

metrics: radon-cc radon-mi radon-raw radon-hal cohesion

# ---------------------------------------------------------
# Security scan
bandit:
	@$(call MESSAGE,$@)
	bandit --recursive .

# ---------------------------------------------------------
# Run the game (shortcut)
run:
	@$(call MESSAGE,$@)
	$(PYTHON) main.py
