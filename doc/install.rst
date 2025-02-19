.. _install:

Installing
==========

There are different ways to install Ensaio:

.. tab-set::

    .. tab-item:: pip

        Using the `pip package manager <https://pypi.org/project/pip/>`__:

        .. code:: bash

            pip install ensaio

    .. tab-item:: conda/mamba

        Using the `conda package manager <https://conda.io/>`__ (or ``mamba``)
        that comes with the Anaconda, Miniconda, or Miniforge distributions:

        .. code:: bash

            conda install ensaio --channel conda-forge

    .. tab-item:: Development version

        You can use ``pip`` to install the latest **unreleased** version from
        GitHub (**not recommended** in most situations):

        .. code:: bash

            python -m pip install --upgrade git+https://github.com/fatiando/ensaio

.. note::

    The commands above should be executed in a terminal. On Windows, use the
    ``cmd.exe`` or the "Anaconda Prompt" app if you're using Anaconda.

.. admonition:: Which Python?
    :class: tip

    See :ref:`python-versions` for a list of  supported Python versions.

.. _dependencies:

Dependencies
------------

The required dependencies should be installed automatically when you install
Ensaio using ``conda`` or ``pip``.

Required:

* `Pooch <https://www.fatiando.org/pooch/>`__

Our examples use other packages to load and plot the data.
If you wish to **run the examples in the documentation**, you will also have to
install:

* `numpy <https://www.numpy.org/>`__
* `pandas <https://pandas.pydata.org/>`__
* `xarray <https://xarray.pydata.org/>`__
* `netcdf4 <https://github.com/Unidata/netcdf4-python>`__
* `PyGMT <https://www.pygmt.org/latest/>`__
