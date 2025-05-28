# Build, package, test, and clean
PROJECT=ensaio
TESTDIR=tmp-test-dir-with-unique-name
PYTEST_ARGS=--cov-config=../.coveragerc --cov-report=term-missing --cov=$(PROJECT) --doctest-modules -v --pyargs
CHECK_STYLE=$(PROJECT) doc
GITHUB_ACTIONS=.github/workflows

.PHONY: help build install test format check check-format check-style check-actions clean

help:
	@echo "Commands:"
	@echo ""
	@echo "  install   install in editable mode"
	@echo "  test      run the test suite (including doctests) and report coverage"
	@echo "  format    automatically format the code"
	@echo "  check     run code style and quality checks"
	@echo "  build     build source and wheel distributions"
	@echo "  clean     clean up build and generated files"
	@echo ""

build:
	python -m build .

install:
	python -m pip install --no-deps --editable .

test:
	# Run a tmp folder to make sure the tests are run on the installed version
	mkdir -p $(TESTDIR)
	cd $(TESTDIR); MPLBACKEND='agg' pytest $(PYTEST_ARGS) $(PROJECT)
	cp $(TESTDIR)/.coverage* .
	rm -rvf $(TESTDIR)

format:
	ruff check --select I --fix $(CHECK_STYLE) # fix isort errors
	ruff format $(CHECK_STYLE)
	burocrata --extension=py $(CHECK_STYLE)

check: check-format check-style check-actions

check-format:
	ruff format --check $(CHECK_STYLE)
	burocrata --check --extension=py $(CHECK_STYLE)

check-style:
	ruff check $(CHECK_STYLE)

check-actions:
	zizmor $(GITHUB_ACTIONS)

clean:
	find . -name "*.pyc" -exec rm -v "{}" \;
	find . -name "*.orig" -exec rm -v "{}" \;
	find . -name ".coverage.*" -exec rm -v "{}" \;
	find . -name "_version_generated.py" -exec rm -v "{}" \;
	find . -name "*.egg-info" -type d -exec rm -vr "{}" \; -prune
	find . -name "__pycache__" -type d -exec rm -vr "{}" \; -prune
	rm -rvf build dist MANIFEST .coverage .*cache
