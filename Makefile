# Build, package, test, and clean
PROJECT=ensaio
CHECK_STYLE=setup.py $(PROJECT) doc/conf.py doc/gallery_src/

help:
	@echo "Commands:"
	@echo ""
	@echo "  install   install in editable mode"
	@echo "  format    automatically format the code"
	@echo "  check     run code style and quality checks"
	@echo "  clean     clean up build and generated files"
	@echo ""

install:
	pip install --no-deps -e .

format: license isort black

check: black-check isort-check license-check flake8

black:
	black $(CHECK_STYLE)

black-check:
	black --check $(CHECK_STYLE)

license:
	python license_notice.py

license-check:
	python license_notice.py --check

isort:
	isort $(CHECK_STYLE)

isort-check:
	isort --check $(CHECK_STYLE)

flake8:
	flake8 $(CHECK_STYLE)

clean:
	find . -name "*.pyc" -exec rm -v {} \;
	find . -name ".coverage.*" -exec rm -v {} \;
	find . -name "*.orig" -exec rm -v {} \;
	rm -rvf build dist MANIFEST *.egg-info __pycache__ .coverage .cache .pytest_cache
	rm -rvf $(TESTDIR) dask-worker-space
