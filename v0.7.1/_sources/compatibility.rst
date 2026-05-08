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
We will add ``FutureWarning`` messages about deprecations ahead of making any
breaking changes to give users a chance to upgrade.

.. warning::

    The above does not apply to versions < ``1.0.0``. All ``0.*`` versions may
    deprecate, remove, or change functionality between releases. Proper
    warnings may be raised, and any breaking changes will be marked as such in
    the :ref:`changes`.


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


.. _dependency-versions:

Supported dependency versions
-----------------------------

Ensaio follows the recommendations in
`NEP29 <https://numpy.org/neps/nep-0029-deprecation_policy.html>`__ for setting
the minimum required version of our dependencies.
In short, we support **all minor releases of our dependencies from the previous
24 months** before an Ensaio release with a minimum of 2 minor releases.

We follow this guidance conservatively and won't require newer versions if the
older ones are still working without causing problems.
Whenever support for a version is dropped, we will include a note in the
:ref:`changes`.

.. seealso::

    Exact version constraints on our dependencies can be found in the
    `pyproject.toml file <https://github.com/fatiando/ensaio/blob/main/pyproject.toml>`__.


.. _python-versions:

Python version compatibility
----------------------------

Ensaio supports Python versions greater than the ones listed below.
If you require support for older Python versions, please pin Ensaio to the
following releases to ensure compatibility:

.. list-table::
    :widths: 40 60

    * - **Python version**
      - **Last compatible release**
    * - 3.6
      - 0.4.0
    * - 3.7
      - 0.6.0
    * - 3.8
      - 0.6.0
