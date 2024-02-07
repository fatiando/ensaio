# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
Bathymetry single-beam surveys of the Caribbean
-----------------------------------------------

This dataset is a compilation of several public domain single-beam bathymetry
surveys of the ocean in the Caribbean. The data display a wide range of
tectonic activity, uneven distribution, and even clear systematic errors in
some of the survey lines.

**Original source:** `NOAA NCEI
<https://ngdc.noaa.gov/mgg/geodas/trackline.html>`__

**Pre-processing:** `Source code for preparation of the original dataset for
redistribution in Ensaio
<https://github.com/fatiando-data/caribbean-bathymetry>`__

"""
import pandas as pd
import pygmt

import ensaio

###############################################################################
# Download and cache the data and return the path to it on disk
fname = ensaio.fetch_caribbean_bathymetry(version=1)
print(fname)

###############################################################################
# Load the CSV formatted data with pandas
data = pd.read_csv(fname)
data

###############################################################################
# Make a PyGMT map with the data points colored by the depth.
fig = pygmt.Figure()
fig.basemap(
    region=[
        data.longitude.min(),
        data.longitude.max(),
        data.latitude.min(),
        data.latitude.max(),
    ],
    projection="M15c",
    frame=True,
)
pygmt.makecpt(cmap="viridis", series=[data.depth_m.min(), data.depth_m.max()])
fig.plot(
    x=data.longitude, y=data.latitude, fill=data.depth_m, cmap=True, style="c0.02c"
)
fig.colorbar(frame='af+l"bathymetric depth [m]"')
fig.coast(land="#666666")
fig.show()
