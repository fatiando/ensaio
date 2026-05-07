Released on: 2026/05/08

DOI:

Documentation:

* General improvements to the Installing and Version Compatibility pages (#119)
* Use an admonition to add more visibility to the `pyproject.toml` file link in the Version Compatibility page (#120)
* Make the README banner the h1 element for proper HTML heading progression, create a citing.rst page and add a link it in the README (#118)

Maintenance:

* Move to a `src` layout, with all the code in the `src` directory and tests in the `test` directory (which isn't distributed with the package anymore to make downloads smaller) (#97)
* Allow official Actions to use version numbers since they should be trustworthy enough (#114)
* Fix Ruff error about checking against single item container (#115)
* Replace Codecov with a GitHub Actions job to check if coverage is 100%, eliminating another third-party dependency (#98)
* Use Ruff and zizmor for linting and formatting instead of flake8, isort, and black (#96)

This release contains contributions from:

- Santiago Soler
- Leonardo Uieda
