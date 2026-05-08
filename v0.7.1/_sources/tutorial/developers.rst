.. _developers:

Using Ensaio in your project
----------------------------

One of the main use cases of Ensaio is to provide reproducible and
easy-to-access data for the documentation of other Python projects.
These are a few tips and tricks for using Ensaio in your own project.

Explicitly set data versions
++++++++++++++++++++++++++++

New version of each dataset may be included in new Ensaio releases. We'll do
our very best to always keep the older data versions available as well to
avoid breaking existing tutorials and documentation.

We recommend always explicitly setting the data version when fetching a
dataset:

.. jupyter-execute::

    import ensaio

    fname = ensaio.fetch_southern_africa_gravity(version=1)

This way, your documentation/tutorial should still use the same data (and
hopefully still produce the same result) even if new versions of Ensaio are
installed.
Otherwise, people going through older examples with newer versions of Ensaio
could get different results (or worse, broken code).

.. tip::

    We still recommend updating to the latest data versions in new tutorials
    and documentation whenever you can.

Download from GitHub on CI
++++++++++++++++++++++++++

By default, the data sources for Ensaio are the archives with the given DOIs
for each dataset (usually
`Zenodo <https://zenodo.org/communities/fatiando>`__).
Alternatively, you can ask Ensaio to download from the GitHub release of each
dataset by setting the environment variable ``ENSAIO_DATA_FROM_GITHUB=true``.

We recommend using the environment variable when running on continuous
integration (CI).
This will minimize the load that is placed on public data servers like
Zenodo.
When using GitHub Actions, this may even make the downloads much faster since
the data source is likely physically closer to the CI infrastructure.
