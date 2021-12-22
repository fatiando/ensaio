.. _compatibility:

Version compatibility
=====================

Ensaio version compatibility
----------------------------

Ensaio uses `semantic versioning <https://semver.org/>`__ (i.e.,
``MAJOR.MINOR.BUGFIX`` format):

* Major releases mean that backwards incompatible changes were made.
  Upgrading will require users to change their code.
* Minor releases add new features/data without changing existing functionality.
  Users can upgrade minor versions without changing their code.
* Bug fix releases fix errors in a previous release without adding new
  functionality. Users can upgrade minor versions without changing their code.

**We aim for Ensaio to be backwards compatible whenever possible and will make
major releases sparingly and with ample warning.**

Source data releases
--------------------

New releases of Ensaio will tend to accompany releases of the source data
collection in the `fatiando/data <https://github.com/fatiando/data>`__
repository.
However, the **version numbers will not necessarily match**.

A major release of the data collection will result in a **new module being
added to Ensaio** (for example, the data release ``2.0.0`` will prompt an
Ensaio release with the ``ensaio.v2`` module added).
The ``1.*.*`` data will still be accessible through the ``ensaio.v1`` module.
The modules for previous releases will not be removed unless absolutely
necessary.

This means that upgrading Ensaio should almost always be safe and documentation
using ``1.*.*`` data should still work after ``2.*.*`` data is released.

.. _python-versions:

Python version compatibility
----------------------------

If you require support for older Python versions, please pin Ensaio to the
following releases to ensure compatibility:

.. list-table::
    :widths: 40 60

    * - **Python version**
      - **Last compatible release**
    * - 3.7
      - 1.2.0 (planned for late 2022)

