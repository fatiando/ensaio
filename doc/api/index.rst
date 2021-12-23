.. _api:

List of functions and classes (API)
===================================

Functions and variables used to download the datasets and cache them locally.
Use the respective module to access the datasets in each major version of the
data release.

.. tip::

    The best way to use Ensaio is to ``import ensaio.v1 as ensaio`` or likewise
    with other versions that are available. This way your code will continue to
    work even when Ensaio updates to include newer incompatible dataset
    versions. See :ref:`compatibility`.

.. automodule:: ensaio
.. currentmodule:: ensaio

``ensaio.v1``
-------------

.. automodule:: ensaio.v1

Functions:

.. autosummary::
   :toctree: generated/

    ensaio.v1.locate
    ensaio.v1.fetch_alps_gps
    ensaio.v1.fetch_britain_magnetic
    ensaio.v1.fetch_british_columbia_lidar
    ensaio.v1.fetch_caribbean_bathymetry
    ensaio.v1.fetch_earth_geoid
    ensaio.v1.fetch_earth_gravity
    ensaio.v1.fetch_earth_topography
    ensaio.v1.fetch_southern_africa_gravity

Module variables:

.. autosummary::
   :toctree: generated/

    ensaio.v1.DOI
    ensaio.v1.URL
    ensaio.v1.ENVIRONMENT_VARIABLE_URL
    ensaio.v1.ENVIRONMENT_VARIABLE_CACHE
