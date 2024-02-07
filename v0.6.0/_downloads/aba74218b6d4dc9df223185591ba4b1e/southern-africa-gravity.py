# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
Gravity ground-based surveys of Southern Africa
-----------------------------------------------

This dataset is a compilation of several public domain ground measurements
of gravity from Southern Africa. The observations are the absolute gravity
values in mGal. The horizontal datum is not specified and heights are
referenced to "sea level", which we will interpret as the geoid (which
realization is likely not relevant since the uncertainty in the height is
probably larger than geoid model differences).

**Original source:** `NOAA NCEI
<https://ngdc.noaa.gov/mgg/geodas/trackline.html>`__

**Pre-processing:** `Source code for preparation of the original dataset for
redistribution in Ensaio
<https://github.com/fatiando-data/southern-africa-gravity>`__
"""
import pandas as pd
import pygmt

import ensaio

###############################################################################
# Download and cache the data and return the path to it on disk
fname = ensaio.fetch_southern_africa_gravity(version=1)
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
    fill=data.gravity_mgal,
    cmap=True,
    style="c0.05c",
)
fig.colorbar(frame='af+l"gravity [mGal]"')
fig.coast(shorelines=True, water="royalblue4", area_thresh=1e4)
fig.show()
