.. _install:

Installing
==========

There are different ways to install Ensaio:

.. tab-set::

    .. tab-item:: conda/mamba

        Using the `conda <https://conda.io/>`__ package manager (or ``mamba``)
        that comes with the Anaconda, Miniconda, or Miniforge distributions:

        .. code:: bash

            conda install ensaio --channel conda-forge

    .. tab-item:: pip

        Using the `pip <https://pypi.org/project/pip/>`__ package manager:

        .. code:: bash

            python -m pip install ensaio

    .. tab-item:: Development version

        You can use ``pip`` to install the latest **unreleased** version from
        GitHub (**not recommended** in most situations):

        .. code:: bash

            python -m pip install --upgrade git+https://github.com/fatiando/ensaio

.. tip::

    The commands above should be executed in a terminal. On Windows, use the
    ``cmd.exe`` or the "Anaconda Prompt" / "Miniforge Prompt" app if you're using
    Anaconda / Miniforge.

.. admonition:: Which Python?
    :class: tip

    See :ref:`python-versions` for a list of  supported Python versions.

.. note::

   We recommend using the
   `Miniforge distribution <https://conda-forge.org/download/>`__
   to ensure that you have the ``conda`` package manager available.
   Installing Miniforge does not require administrative rights to your computer
   and doesn't interfere with any other Python installations in your system.
   It's also much smaller than the Anaconda distribution and is less likely to
   break when installing new software.

.. _dependencies:

Dependencies
------------

The required dependencies should be installed automatically when you install
Ensaio using ``conda`` or ``pip``.

Required:

* `Pooch <https://www.fatiando.org/pooch/>`__

.. note::

    See :ref:`dependency-versions` for our policy of oldest supported
    versions of each dependency.

Our examples use other packages to load and plot the data.
If you wish to **run the examples in the documentation**, you will also have to
install:

* `numpy <https://www.numpy.org/>`__
* `pandas <https://pandas.pydata.org/>`__
* `xarray <https://xarray.pydata.org/>`__
* `netcdf4 <https://github.com/Unidata/netcdf4-python>`__
* `PyGMT <https://www.pygmt.org/latest/>`__
