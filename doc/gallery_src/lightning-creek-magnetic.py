# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
Magnetic anomaly grid of the Lightning Creek Sill Complex, Australia
--------------------------------------------------------------------

This is a section of an airborne survey acquired in 1990 by the Queensland
Government, Australia. The grid has 50 m resolution (UTM coordinates) and
is at a uniform orthometric height of 500 m.

**Original source:**
`Geophysical Acquisition & Processing Section 2019. MIM Data from Mt Isa
Inlier, QLD (P1029), magnetic line data, AWAGS levelled. Geoscience Australia,
Canberra <http://pid.geoscience.gov.au/dataset/ga/142419>`__

"""
import pygmt
import xarray as xr

import ensaio

###############################################################################
# Download and cache the data and return the path to it on disk
fname = ensaio.fetch_lightning_creek_magnetic(version=1)
print(fname)

###############################################################################
# Load the netCDF grid with xarray
data = xr.load_dataarray(fname)
data

###############################################################################
# Make a PyGMT pseudo-color map of the total field magnetic anomaly.
fig = pygmt.Figure()
scale = 2500
pygmt.makecpt(cmap="polar+h", series=[-scale, scale], background=True)
fig.grdimage(
    grid=data,
    cmap=True,
    shading="+a45+nt0.1",
    projection="X15c/17c",
    frame="af",
)
fig.colorbar(
    frame='af+l"total field magnetic anomaly [nT]"',
    position="JBC+h+o0/1c+e",
)
fig.show()

###############################################################################
# The anomaly at the top right is the  Lightning Creek sill complex.
