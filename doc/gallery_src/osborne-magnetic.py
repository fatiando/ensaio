# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
Magnetic airborne survey of the Osborne Mine, Australia
-------------------------------------------------------

This is a section of a survey acquired in 1990 by the Queensland
Government, Australia. The line data have approximately 80 m terrain
clearance and 200 m line spacing. The section contains
the total field magnetic anomalies associated with the Osborne Mine,
Lightning Creek sill complex, and the Brumby prospect.

**Original source:**
`Geophysical Acquisition & Processing Section 2019. MIM Data from Mt Isa
Inlier, QLD (P1029), magnetic line data, AWAGS levelled. Geoscience Australia,
Canberra <http://pid.geoscience.gov.au/dataset/ga/142419>`__

"""
import pandas as pd
import pygmt

import ensaio

###############################################################################
# Download and cache the data and return the path to it on disk
fname = ensaio.fetch_osborne_magnetic(version=1)
print(fname)

###############################################################################
# Load the CSV formatted data with pandas
data = pd.read_csv(fname)
data

###############################################################################
# Make a PyGMT map with the data points colored by the total field magnetic
# anomaly.
fig = pygmt.Figure()
fig.basemap(
    projection="M15c",
    region=[
        data.longitude.min(),
        data.longitude.max(),
        data.latitude.min(),
        data.latitude.max(),
    ],
    frame="af",
)
scale = 1500
pygmt.makecpt(cmap="polar+h", series=[-scale, scale], background=True)
fig.plot(
    x=data.longitude,
    y=data.latitude,
    color=data.total_field_anomaly_nt,
    style="c0.075c",
    cmap=True,
)
fig.colorbar(
    frame='af+l"total field magnetic anomaly [nT]"',
    position="JBC+h+o0/1c+e",
)
fig.show()

###############################################################################
# The anomaly at the bottom left is the Osborne Mine. The ones on the top right
# are the Lightning Creek sill complex (the largest) and the Brumby prospect
# (one of the smaller anomalies).
