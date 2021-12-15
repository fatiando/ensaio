.. _gallery_v1:

Version 1
=========

About
-----

The datasets that make up the ``v1`` series of Ensaio. Use the functions in the
:mod:`ensaio.v1` module to download and cache (store) them on your computer.
See the documentation of invidual functions for more information about the
data, the original sources and the respective licenses.

**Data source:** doi:`10.5281/zenodo.5167357 <https://doi.org/10.5281/zenodo.5167357>`__

**Data compilation license:** `CC-BY <https://creativecommons.org/licenses/by/4.0/>`__

**Data compilation provanace:** `github.com/fatiando/data/tree/v1.0.0 <https://github.com/fatiando/data/tree/v1.0.0>`__

The location of the cache folder varies by operating system. Use the
:func:`ensaio.v1.cache_folder` function to get its location. You can also set
the location manually by creating a ``ENSAIO_V1_DATA_DIR`` environment variable
with the desired path. Ensaio will search for this variable and if found will
use its value instead of the default cache folder.

You can also specify alternative data download URLs using the ``ENSAIO_V1_URL``
environment variable (for example, if you want to use a mirror). By default,
Ensaio uses the Zenodo archive linked above. You can also set the download URL
to the `GitHub data release <https://github.com/fatiando/data/releases>`__
using
``ENSAIO_V1_URL="https://github.com/fatiando/data/releases/download/v1.0.0"``.

.. tip::

    Use the GitHub download URL if using Ensaio on continuous integration (CI)
    to avoid overloading the Zenodo servers.

Data
----
