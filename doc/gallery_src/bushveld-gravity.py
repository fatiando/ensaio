# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
Observed and preprocessed gravity data over Bushveld, Southern Africa
---------------------------------------------------------------------

This dataset contains ground gravity observations over the area that comprises
the Bushveld Igenous Complex in Southern Africa, including preprocessed gravity
fields such as the **gravity disturbance** and the **bouguer gravity
disturbance** (topography-free gravity disturbance). In addition, the dataset
contains the heights of the observation points referenced on the WGS84
reference ellipsoid and over the mean sea-level (what can be considered to be
the geoid). This dataset was built upon a portion of the Southern Africa
gravity compilation available through NOAA NCEI.

**Original source:**
* gravity: `NOAA NCEI <https://www.ngdc.noaa.gov/mgg/gravity/>`__
* topography: `ETOPO1 <https://doi.org/10.7289/V5C8276M>`__

"""
import numpy as np
import pandas as pd
import pygmt

import ensaio

###############################################################################
# Download and cache the data and return the path to it on disk
fname = ensaio.fetch_bushveld_gravity(version=1)
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
        data.longitude.min() - 0.5,
        data.longitude.max() + 0.5,
        data.latitude.min() - 0.5,
        data.latitude.max() + 0.5,
    ],
    projection="M15c",
    frame=True,
)
scale = np.max(np.abs(data.gravity_disturbance_mgal))
pygmt.makecpt(
    cmap="polar",
    series=[-scale, scale],
)
fig.plot(
    x=data.longitude,
    y=data.latitude,
    color=data.gravity_disturbance_mgal,
    cmap=True,
    style="c0.1c",
)
fig.colorbar(frame='af+l"gravity disturbance [mGal]"')
fig.show()
