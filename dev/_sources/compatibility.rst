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

New releases of Ensaio will tend to accompany releases of new datasets or new
versions of existing data in the
`Fatiando a Terra Datasets <https://github.com/fatiando-data>`__ collection.

Older versions of each dataset will still remain available (as much as
possible) and can be accessed by setting the ``version`` argument of the
``fetch_*`` functions accordingly.
This means that **upgrading Ensaio should almost always be safe**.
Documentation using version ``1`` of a dataset will still use the same data
(and hopefully produce the same results) after version ``2`` is included in
Ensaio.

.. seealso::

    See :ref:`developers` for more tips and tricks.


.. _python-versions:

Python version compatibility
----------------------------

If you require support for older Python versions, please pin Ensaio to the
following releases to ensure compatibility:

.. list-table::
    :widths: 40 60

    * - **Python version**
      - **Last compatible release**
    * - 3.6
      - 0.4.0

