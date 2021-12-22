# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
.. _using:

Downloading data
----------------

The location of the cache folder varies by operating system. Use the
:func:`ensaio.v1.cache_folder` function to get its location. You can also set
the location manually by creating a ``ENSAIO_V1_DATA_DIR`` environment variable
with the desired path. Ensaio will search for this variable and if found will
use its value instead of the default cache folder.

"""
import pandas as pd
import pygmt

import ensaio.v1 as ensaio

###############################################################################
# Download and cache the data and return the path to it on disk
fname = ensaio.fetch_southern_africa_gravity()
print(fname)

###############################################################################
# Load the CSV formatted data with pandas
data = pd.read_csv(fname)
data

###############################################################################
# Make a PyGMT map with the data points colored by the gravity data.
fig = pygmt.Figure()
fig.basemap(
    region=[
        data.longitude.min() - 1,
        data.longitude.max() + 1,
        data.latitude.min() - 1,
        data.latitude.max() + 1,
    ],
    projection="M15c",
    frame=True,
)
pygmt.makecpt(cmap="viridis", series=[data.gravity_mgal.min(), data.gravity_mgal.max()])
fig.plot(
    x=data.longitude,
    y=data.latitude,
    color=data.gravity_mgal,
    cmap=True,
    style="c0.05c",
)
fig.colorbar(frame='af+l"gravity [mGal]"')
fig.coast(shorelines=True, water="royalblue4", area_thresh=1e4)
fig.show()
