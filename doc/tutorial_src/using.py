# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
.. _using:

Downloading data
================

Ensaio provides functions for downloading datasets from the `fatiando/data
<https://github.com/fatiando/data>`__ collection to your computer. The
functions are available through different modules for each major release of
the data collection. For example, datasets from the version 1.X series are
available through :mod:`ensaio.v1`.

The recommended way to use Ensaio is to import a particular version module like
so:
"""
# Load Pandas as well so we can read in some data
import pandas as pd

import ensaio.v1 as ensaio

###############################################################################
# To download a particular dataset, say our Southern Africa gravity data,
# call the corresponding ``fetch_`` functions:
fname = ensaio.fetch_southern_africa_gravity()
print(fname)

###############################################################################
# .. tip::
#
#     You can browse a list of all available datasets in :ref:`api` or
#     :ref:`gallery_v1`.
#
# If the data are not yet available on your computer, Ensaio will automatically
# download it and return the path to the downloaded file.
# In the file had already been downloaded, Ensaio won't repeat the download and
# will only return the path to the existing file.
#
# This means that placing the code above in a Python script or Jupyter notebook
# will mean that whoever runs it is guaranteed to get the data on their
# computer.
# Running the code multiple times or using the same data in multiple places
# will only trigger a single download, saving bandwidth and storage space.
#
# .. note::
#
#     Ensaio uses `Pooch <https://www.fatiando.org/pooch/>`__ under the hood to
#     make all of this work.
#
# Once we have the path to the data file, we can load it like we would any
# other data file. In this case, our data is in a CSV file so the natural
# choice is to use `Pandas <https://pandas.pydata.org/>`__:
data = pd.read_csv(fname)
data

###############################################################################
# .. admonition:: Using Ensaio in your project documentation?
#
#     Make sure you take a look at :ref:`developers` for useful tips and
#     tricks.
#
# Where are the data?
# -------------------
#
# The location of the cache folder varies by operating system. Use the
# :func:`ensaio.v1.cache_folder` function to get its location on your computer.
print(ensaio.cache_folder())

###############################################################################
# You can also set the location manually by creating a ``ENSAIO_V1_DATA_DIR``
# environment variable with the desired path. Ensaio will search for this
# variable and if found will use its value instead of the default cache folder.
#
# Similar variables and functions are available for each data collection
# version.
