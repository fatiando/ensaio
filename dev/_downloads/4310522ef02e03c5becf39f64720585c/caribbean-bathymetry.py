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
tectonic activity and uneven distribution.

**Original source:** `NOAA NCEI
<https://ngdc.noaa.gov/mgg/geodas/trackline.html>`__

**Pre-processing:** `Source code for preparation of the original dataset for
redistribution in Ensaio
<https://github.com/fatiando-data/caribbean-bathymetry>`__

.. admonition:: Changes in version 2
    :class: note

    In version 1, there were 1,938,095 data taking up a larger area. The
    data were ``depth_m`` and positive downward. Version 2, cropped the
    data to make it more manageable and converted the depths to bathymetric
    heights (negative downward).

"""
import pandas as pd
import pygmt

import ensaio

###############################################################################
# Download and cache the data and return the path to it on disk
fname = ensaio.fetch_caribbean_bathymetry(version=2)
print(fname)

###############################################################################
# Load the CSV formatted data with pandas
data = pd.read_csv(fname)
data

###############################################################################
# Make a PyGMT map with the data points colored by the bathymetry.
fig = pygmt.Figure()
pygmt.makecpt(
    cmap="cmocean/topo+h",
    series=[data.bathymetry_m.min(), data.bathymetry_m.max()],
)
fig.plot(
    x=data.longitude,
    y=data.latitude,
    fill=data.bathymetry_m,
    cmap=True,
    style="c0.02c",
    projection="M15c",
    frame=True,
)
fig.colorbar(frame='af+l"bathymetry [m]"')
fig.coast(land="#666666")
fig.show()
