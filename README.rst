.. image:: https://github.com/fatiando/ensaio/raw/main/doc/_static/readme-banner.png
   :alt: Ensaio: Practice datasets to probe your code

`Documentation <https://www.fatiando.org/ensaio>`__ |
`Documentation (dev version) <https://www.fatiando.org/ensaio/dev>`__ |
Part of the `Fatiando a Terra <https://www.fatiando.org>`__ project

.. image:: http://img.shields.io/pypi/v/ensaio.svg?style=flat-square
    :alt: Latest version on PyPI
    :target: https://pypi.python.org/pypi/ensaio
.. image:: https://img.shields.io/conda/vn/conda-forge/ensaio.svg?style=flat-square
    :alt: Latest version on conda-forge
    :target: https://github.com/conda-forge/ensaio-feedstock
.. image:: https://img.shields.io/codecov/c/github/fatiando/ensaio/main.svg?style=flat-square
    :alt: Test coverage status
    :target: https://codecov.io/gh/fatiando/ensaio
.. image:: https://img.shields.io/pypi/pyversions/ensaio.svg?style=flat-square
    :alt: Compatible Python versions.
    :target: https://pypi.python.org/pypi/ensaio
.. image:: https://img.shields.io/badge/doi-10.5281%2Fzenodo.5784202-blue?style=flat-square
    :alt: DOI used to cite Ensaio
    :target: https://doi.org/10.5281/zenodo.5784202

About
-----

**Ensaio** (Portuguese for "rehearsal") is a Python package for downloading
open-access sample datasets for Geoscience.
It taps into the `Fatiando a Terra FAIR data collection
<https://github.com/fatiando-data>`__ that is designed for use in tutorials,
documentation, and teaching.

It uses `Pooch <https://www.fatiando.org/pooch>`__ to manage downloading and
caching the data on your computer.
This means that datasets are only downloaded if they can't be found on your
computer already.

Project goals
-------------

* Provide minimal code for downloading our sample data (basically just creates
  the relevant Pooch code).
* Only download and let the user load the data. This helps make tutorials and
  examples more easily extended to a user's own data.
* Be fully backwards compatible. We achieve this by separating **data**
  versions from **Ensaio** versions. Data fetching functions allow you to
  choose any data version that is older than the version of Ensaio that's
  installed. Major releases of Ensaio will be few and far between (if any).

Contacting Us
-------------

Find out more about how to reach us at
`fatiando.org/contact <https://www.fatiando.org/contact/>`__

Contributing
------------

Code of conduct
+++++++++++++++

Please note that this project is released with a
`Code of Conduct <https://github.com/fatiando/community/blob/main/CODE_OF_CONDUCT.md>`__.
By participating in this project you agree to abide by its terms.

Contributing Guidelines
+++++++++++++++++++++++

Please read our
`Contributing Guide <https://github.com/fatiando/ensaio/blob/main/CONTRIBUTING.md>`__
to see how you can help and give feedback.

License
-------

This is free software: you can redistribute it and/or modify it under the terms
of the **BSD 3-clause License**. A copy of this license is provided in
`LICENSE.txt <https://github.com/fatiando/ensaio/blob/master/LICENSE.txt>`__.
