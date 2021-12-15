# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
from pathlib import Path

import pooch

DOI = "10.5281/zenodo.5167357"

_REPOSITORY = pooch.create(
    path=Path(pooch.os_cache("ensaio")) / "v1",
    base_url=f"doi:{DOI}/",
    registry={
        "alps-gps-velocity.csv.xz": "md5:195ee3d88783ce01b6190c2af89f2b14",
        "britain-magnetic.csv.xz": "md5:8dbbda02c7e74f63adc461909358f056",
        "british-columbia-lidar.csv.xz": "md5:354c725a95036bd8340bc14e043ece5a",
        "caribbean-bathymetry.csv.xz": "md5:a7332aa6e69c77d49d7fb54b764caa82",
        "earth-geoid-10arcmin.nc": "md5:39b97344e704eb68fa381df2eb47da0f",
        "earth-gravity-10arcmin.nc": "md5:56df20e0e67e28ebe4739a2f0357c4a6",
        "earth-topography-10arcmin.nc": "md5:c43b61322e03669c4313ba3d9a58028d",
        "southern-africa-gravity.csv.xz": "md5:1dee324a14e647855366d6eb01a1ef35",
    },
)


def fetch_alps_gps():
    """
    Fetch the Alpine 3-component GPS velocity dataset

    This is a compilation of 3D GPS velocities for the Alps. The horizontal
    velocities are reference to the Eurasian frame. All velocity components and
    even the position have error estimates, which is very useful and rare to
    find in a lot of datasets.

    There 186 stations in total. The data available are: station ID, longitude,
    latitude (geodetic), height (geometric), ground velocity in the East,
    North, and upward directions, and the estimated uncertainties in each of
    these.

    **Format:** CSV with xz (lzma) compression.

    **Load with:** :func:`pandas.read_csv`

    **Original source:**
    `Sánchez et al. (2018) <https://doi.org/10.1594/PANGAEA.886889>`__

    Returns
    -------
    fname : :class:`pathlib.Path`
        Path to the downloaded file on disk.

    """
    return Path(_REPOSITORY.fetch("alps-gps-velocity.csv.xz"))