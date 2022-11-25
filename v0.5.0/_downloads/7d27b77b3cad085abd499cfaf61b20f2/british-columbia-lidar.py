# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
Topography of the Trail Islands in British Columbia, Canada
-----------------------------------------------------------

This is a lidar point cloud (ground reflections only) sliced to the small
`Trail Islands <https://apps.gov.bc.ca/pub/bcgnws/names/21973.html>`__
to the North of Vancouver. The islands have some nice looking topography and
their isolated nature creates problems for some interpolation methods.

**Original source:** `LidarBC
<https://www2.gov.bc.ca/gov/content/data/geographic-data-services/lidarbc>`__

**Pre-processing:** `Source code for preparation of the original dataset for
redistribution in Ensaio
<https://github.com/fatiando-data/british-columbia-lidar>`__

"""
import pandas as pd
import pygmt

import ensaio

###############################################################################
# Download and cache the data and return the path to it on disk
fname = ensaio.fetch_british_columbia_lidar(version=1)
print(fname)

###############################################################################
# Load the CSV formatted data with pandas
data = pd.read_csv(fname)
data

###############################################################################
# Make a PyGMT map with the data points colored by the elevation.
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
pygmt.makecpt(cmap="viridis", series=[data.elevation_m.min(), data.elevation_m.max()])
fig.plot(
    x=data.longitude, y=data.latitude, color=data.elevation_m, cmap=True, style="c0.05c"
)
fig.colorbar(frame='af+l"elevation [m]"')
fig.show()
