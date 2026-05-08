.. _using:

Downloading data
================

Ensaio provides functions for downloading datasets from the `Fatiando a Terra
Datasets <https://github.com/fatiando-data>`__ collection to your computer.
These functions don't attempt to do any loading of the data into memory and
only return the path of the downloaded file on your computer.

To take care of the actual loading of the data, we'll import
`Pandas <https://pandas.pydata.org/>`__ as well since the data we'll use is in
CSV format.

.. jupyter-execute::

    import pandas as pd

    import ensaio

To download a particular dataset, say version 1 of our Southern Africa
gravity data, call the corresponding ``fetch_*`` functions:

.. jupyter-execute::

    fname = ensaio.fetch_southern_africa_gravity(version=1)
    print(fname)

.. tip::

    The version of the data should **always** be explicitly included so that
    you code continues to work in the same way even if a newer version of the
    data is released.

If the data are not yet available on your computer, Ensaio will automatically
download it and return the path to the downloaded file.
In the file had already been downloaded, Ensaio won't repeat the download and
will only return the path to the existing file.

This means that placing the code above in a Python script or Jupyter notebook
will mean that whoever runs it is guaranteed to get the data on their
computer.
Running the code multiple times or using the same data in multiple places
will only trigger a single download, saving bandwidth and storage space.

.. note::

    Ensaio uses `Pooch <https://www.fatiando.org/pooch/>`__ under the hood to
    make all of this work.

Once we have the path to the data file, we can load it like we would any
other data file. In this case, our data is in a CSV file so the natural
choice is to use `Pandas <https://pandas.pydata.org/>`__:

.. jupyter-execute::

    data = pd.read_csv(fname)
    data

.. seealso::

    You can browse a list of all available datasets in :ref:`api` or
    :ref:`gallery`.

Where are the data?
-------------------

The location of the cache folder varies by operating system. Use the
:func:`ensaio.locate` function to get its location on your computer.

.. jupyter-execute::

    print(ensaio.locate())

You can also set the location manually by creating a ``ENSAIO_DATA_DIR``
environment variable with the desired path. Ensaio will search for this
variable and if found will use its value instead of the default cache folder.
