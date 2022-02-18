# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
Magnetic airborne survey of Britain
-----------------------------------

This is a digitization of an airborne magnetic survey of Britain. Data are
sampled where flight lines crossed contours on the archive maps. Contains
only the total field magnetic anomaly, not the magnetic field intensity
measurements or corrections.

Unfortunately, the exact date of measurements is not available (only the year).

Contains British Geological Survey materials © UKRI 2021.

**Original source:**
`British Geological Survey
<https://www.bgs.ac.uk/datasets/gb-aeromagnetic-survey/>`__

"""
import numpy as np
import pandas as pd
import pygmt

import ensaio

###############################################################################
# Download and cache the data and return the path to it on disk
fname = ensaio.fetch_britain_magnetic(version=1)
print(fname)

###############################################################################
# Load the CSV formatted data with pandas
data = pd.read_csv(fname)
data

###############################################################################
# Make a PyGMT map with the data points colored by the total field magnetic
# anomaly.

fig = pygmt.Figure()
scale = np.percentile(data.total_field_anomaly_nt, 95)
pygmt.makecpt(cmap="polar", series=[-scale, scale])
fig.plot(
    x=data.longitude,
    y=data.latitude,
    style="c0.02c",
    color=data.total_field_anomaly_nt,
    cmap=True,
    projection="M15c",
)
fig.colorbar(frame='af+l"nT"', position="jBL+h+w7c/0.2c+o1/2")
fig.coast(shorelines=True)
fig.basemap(frame="afg")
fig.show()
