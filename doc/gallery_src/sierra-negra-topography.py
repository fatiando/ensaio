# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
Topography of the 2018 lava flows of the Sierra Negra volcano, Ecuador
----------------------------------------------------------------------

This is a structure-from-motion point cloud of the 2018 lava flows of the
Sierra Negra volcano, located on the Galápagos islands, Ecuador. The survey
covers a small region at the flank of the volcano and shows different
structures and terrain roughness on the lava flows.

**Original source:** `Carr, B. (2020). Sierra Negra Volcano (TIR Flight 3):
Galápagos, Ecuador, October 22 2018. Distributed by OpenTopography.
<https://doi.org/10.5069/G957196P>`__

"""
import pandas as pd
import pygmt

import ensaio

###############################################################################
# Download and cache the data and return the path to it on disk
fname = ensaio.fetch_sierra_negra_topography(version=1)
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
    x=data.longitude, y=data.latitude, color=data.elevation_m, cmap=True, style="c0.01c"
)
fig.colorbar(frame='af+l"elevation [m]"')
fig.show()
