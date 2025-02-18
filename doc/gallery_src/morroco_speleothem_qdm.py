# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
QDM magnetic microscopy dataset of a speleothem from Morocco
------------------------------------------------------------

High-resolution magnetic map of a stalagmite sample from Wintimdouine Cave,
Morocco, created using Quantum Diamond Microscope (QDM) measurements at Harvard
University. The data were collected to explore the magnetic remanence
properties of hematite and magnetite within the sample, providing insight into
past geomagnetic field variations recorded in cave deposits.

**Original source:** Carmo, Janine; Fu, Roger; Trindade, Ricardo; Piascik,
Samuel (2023). QDM magnetic microscopy dataset of a speleothem from
Morocco. figshare. Dataset.
`10.6084/m9.figshare.22965200.v1 <https://doi.org/10.6084/m9.figshare.22965200.v1>`__

**Pre-processing:** `Source code for preparation of the original dataset for
redistribution in Ensaio
<https://github.com/fatiando-data/morroco-speleothem-qdm>`__

"""
import matplotlib.pyplot as plt
import xarray as xr

import ensaio

###############################################################################
# Download and cache the data and return the path to it on disk. We'll use the
# netCDF version because it's smaller and can be loaded with xarray easily.
fname = ensaio.fetch_morroco_speleothem_qdm(version=1, format="netcdf")
print(fname)

###############################################################################
# Load the netCDF grid with xarray
data = xr.load_dataarray(fname)
data

###############################################################################
# Make a pseudo-color map of the magnetic microscopy data and adjust the scale
# because of some very strong sources.
fig, ax = plt.subplots(1, 1, figsize=(9, 4.8), layout="constrained")
scale = 2500
data.plot.imshow(ax=ax, cmap="RdBu_r", vmin=-scale, vmax=scale)
ax.set_aspect("equal")
plt.show()
