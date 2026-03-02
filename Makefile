.PHONY: prepare-venv test coverage docs

VENV   ?=
PYTHON  = $(if $(VENV),$(CURDIR)/$(VENV)/bin/python3,python3)
SPHINXBUILD  = $(if $(VENV),$(CURDIR)/$(VENV)/bin/sphinx-build,sphinx-build)

prepare-venv:
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install ".[dev,doc]"

test:
	$(PYTHON) -m coverage run -m unittest discover -s home/tests -t . -v
	$(PYTHON) -m coverage run --append -m behave home/features/

coverage: test
	$(PYTHON) -m coverage report -m
	$(PYTHON) -m coverage html
	open htmlcov/index.html

docs:
	$(MAKE) -C docs html SPHINXBUILD=$(SPHINXBUILD) PYTHON=$(PYTHON)
