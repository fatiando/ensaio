# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
Topography of the Earth at 10 arc-minute resolution
---------------------------------------------------

The grid is grid-node registered and stored in netCDF with CF-compliant
metadata. The values are derived from a spherical harmonic model of the ETOPO1
bedrock grid. Topography values are referenced to "sea level" and are positive
upwards.

**Original source:** `ETOPO1 <https://doi.org/10.7289/V5C8276M>`__

"""
import pygmt
import xarray as xr

import ensaio.v1 as ensaio

###############################################################################
# Download and cache the data and return the path to it on disk.
fname = ensaio.fetch_earth_topography()
print(fname)

###############################################################################
# Load the netCDF grid with xarray.
data = xr.load_dataarray(fname)
data

###############################################################################
# Make a PyGMT pseudo-color map of the grid in a Mollweide projection.
fig = pygmt.Figure()
fig.basemap(
    region="g",
    projection="W15c",
    frame=True,
)
fig.grdimage(data, cmap="etopo1", shading="+nt0.5")
fig.colorbar(frame='af+l"topography [m]"')
fig.coast(shorelines=True, resolution="c", area_thresh=1e4)
fig.show()
