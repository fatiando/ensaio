.. _install:

Installing
==========

There are different ways to install Ensaio:

.. tabbed:: pip

    Using the `pip <https://pypi.org/project/pip/>`__ package manager:

    .. code:: bash

        python -m pip install ensaio

.. tabbed:: conda

    Using the `conda <https://conda.io/>`__ package manager that comes with the
    Anaconda/Miniconda distribution:

    .. code:: bash

        conda install ensaio --channel conda-forge

.. tabbed:: Development version

    Using ``pip`` to install the latest **unreleased** version from GitHub:

    .. code:: bash

        python -m pip install --upgrade git+https://github.com/fatiando/ensaio


Which Python?
-------------

You'll need **Python >= 3.7** (see :ref:`python-versions` if you
require support for older versions).

We recommend using the
`Anaconda <https://www.anaconda.com/download>`__
or `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`__
Python distributions to ensure you have all dependencies installed and the
``conda`` package manager available.
Installing Anaconda does not require administrative rights to your computer and
doesn't interfere with any other Python installations in your system.

.. note::

    The commands below should be executed in a terminal. On Windows, use the
    "Anaconda Prompt" app or ``cmd.exe`` if you're not using Anaconda.

.. _dependencies:

Dependencies
------------

The required dependencies should be installed automatically when you install
Ensaio using ``conda`` or ``pip``.

* `Pooch <https://www.fatiando.org/pooch/>`__

Note, however, that our examples use other packages to load and plot the data.
If you wish to run the examples in the documentation, you will have to install:

* `numpy <https://www.numpy.org/>`__
* `pandas <https://pandas.pydata.org/>`__
* `xarray <https://xarray.pydata.org/>`__
* `PyGMT <https://www.pygmt.org/latest/>`__
