# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
import os
from pathlib import Path

import pooch

DOI = "10.5281/zenodo.5167357"


def cache_folder():
    """
    The location of the data cache for v1 datasets

    Returns
    -------
    cache : :class:`pathlib.Path`
        Path to the cache folder.
    """
    return Path(pooch.os_cache("ensaio")) / "v1"


def _make_repository():
    """
    Create the :class:`pooch.Pooch` instance that is used to download the data.

    Set's the cache location to the OS default plus ``ensaio/v1`` and can be
    set manually using the ``ENSAIO_V1_DATA_DIR`` environment variable.

    The download URL can be set using the ``ENSAIO_V1_URL`` environment
    variable (default is ``doi:10.5281/zenodo.5167357``).

    Returns
    -------
    repository : pooch.Pooch

    """
    url_var = "ENSAIO_V1_URL"
    if url_var in os.environ and os.environ[url_var]:
        url = os.environ[url_var]
    else:
        url = f"doi:{DOI}"
    if not url.endswith("/"):
        url = url + "/"
    repository = pooch.create(
        path=cache_folder(),
        base_url=url,
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
        # The name of an environment variable that can overwrite the path
        env="ENSAIO_V1_DATA_DIR",
    )
    return repository


def fetch_alps_gps():
    """
    Alpine 3-component GPS velocity dataset

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

    **Datum:** WGS84

    **Original source:**
    `Sánchez et al. (2018) <https://doi.org/10.1594/PANGAEA.886889>`__

    **Original license:** CC-BY

    Returns
    -------
    fname : :class:`pathlib.Path`
        Path to the downloaded file on disk.

    """
    repository = _make_repository()
    return Path(repository.fetch("alps-gps-velocity.csv.xz"))


def fetch_britain_magnetic():
    """
    Digitized airborne magnetic survey of Britain

    This is a digitization of an airborne magnetic survey of Britain. Data are
    sampled where flight lines crossed contours on the archive maps. Contains
    only the total field magnetic anomaly, not the magnetic field intensity
    measurements or corrections.

    The exact date of measurements is not available (only the year).

    There are 541,508 measurements in total with 6 columns available: line and
    segment ID, year, longitude, latitude (geodetic), height (unknown datum),
    total field magnetic anomaly.

    Contains British Geological Survey materials © UKRI 2021.

    **Format:** CSV with xz (lzma) compression.

    **Load with:** :func:`pandas.read_csv`

    **Datum:** WGS84

    **Original source:**
    `British Geological Survey
    <https://www.bgs.ac.uk/datasets/gb-aeromagnetic-survey/>`__

    **Original license:** Open Government Licence

    Returns
    -------
    fname : :class:`pathlib.Path`
        Path to the downloaded file on disk.

    """
    repository = _make_repository()
    return Path(repository.fetch("britain-magnetic.csv.xz"))


def fetch_british_columbia_lidar():
    """
    Lidar point cloud data of the Trail Islands in BC, Canada

    This is a lidar point cloud (ground reflections only) sliced to the small
    `Trail Islands <https://apps.gov.bc.ca/pub/bcgnws/names/21973.html>`__
    to the North of Vancouver. The islands have some nice looking topography
    and their isolated nature creates problems for some interpolation methods.

    There are 829,733 measurements in total with 3 columns available:
    longitude, latitude (geodetic), and ground elevation (orthometric).

    **Format:** CSV with xz (lzma) compression.

    **Load with:** :func:`pandas.read_csv`

    **Datum:** WGS84

    **Original source:** `LidarBC
    <https://www2.gov.bc.ca/gov/content/data/geographic-data-services/lidarbc>`__

    **Original license:** Open Government Licence - British Columbia

    Returns
    -------
    fname : :class:`pathlib.Path`
        Path to the downloaded file on disk.

    """
    repository = _make_repository()
    return Path(repository.fetch("british-columbia-lidar.csv.xz"))


def fetch_caribbean_bathymetry():
    """
    Single-beam bathymetry of the Caribbean

    This dataset is a compilation of several public domain single-beam
    bathymetry surveys of the ocean in the Caribbean. The data display a wide
    range of tectonic activity, uneven distribution, and even clear systematic
    errors in some of the survey lines.

    There are 1,938,095 measurements in total with 4 columns available:
    survey ID, longitude, latitude (geodetic), and depth (positive downwards
    and referenced to "sea level").

    **Format:** CSV with xz (lzma) compression.

    **Load with:** :func:`pandas.read_csv`

    **Datum:** WGS84

    **Original source:** `NOAA NCEI
    <https://ngdc.noaa.gov/mgg/geodas/trackline.html>`__

    **Original license:** Public domain

    Returns
    -------
    fname : :class:`pathlib.Path`
        Path to the downloaded file on disk.

    """
    repository = _make_repository()
    return Path(repository.fetch("caribbean-bathymetry.csv.xz"))


def fetch_earth_geoid():
    """
    Geoid height of the Earth at 10 arc-minute resolution

    The grid is global with node spacing of 10 arc-minutes (grid-node
    registered) and stored in netCDF with CF-compliant metadata.

    The geoid height is derived from the EIGEN-6C4 spherical harmonic model of
    the Earth's gravity field.

    There are 1081 x 2161 grid points in total. Coordinates are longitude and
    latitude (geodetic).

    **Format:** netCDF4 with zlib compression

    **Load with:** :func:`xarray.load_dataarray` (requires the `netcdf4
    <https://github.com/Unidata/netcdf4-python>`__ library)

    **Datum:** WGS84

    **Original source:** `EIGEN-6C4 model
    <https://doi.org/10.5880/icgem.2015.1>`__

    **Original license:** CC-BY

    Returns
    -------
    fname : :class:`pathlib.Path`
        Path to the downloaded file on disk.

    """
    repository = _make_repository()
    return Path(repository.fetch("earth-geoid-10arcmin.nc"))


def fetch_earth_gravity():
    """
    Gravity of the Earth at 10 arc-minute resolution

    The grid is global with node spacing of 10 arc-minutes (grid-node
    registered) and stored in netCDF with CF-compliant metadata.

    The gravity values are derived from the EIGEN-6C4 spherical harmonic model
    (calculated uniformly at 10 km above the WGS84 ellipsoid). Here "gravity"
    refers to the combined gravitational and centrifugal accelerations.

    There are 1081 x 2161 grid points in total. Coordinates are longitude and
    latitude (geodetic) plus a non-dimensional coordinate height (geometric).

    **Format:** netCDF4 with zlib compression

    **Load with:** :func:`xarray.load_dataarray` (requires the `netcdf4
    <https://github.com/Unidata/netcdf4-python>`__ library)

    **Datum:** WGS84

    **Original source:** `EIGEN-6C4 model
    <https://doi.org/10.5880/icgem.2015.1>`__

    **Original license:** CC-BY

    Returns
    -------
    fname : :class:`pathlib.Path`
        Path to the downloaded file on disk.

    """
    repository = _make_repository()
    return Path(repository.fetch("earth-gravity-10arcmin.nc"))


def fetch_earth_topography():
    """
    Topography/bathymetry of the Earth at 10 arc-minute resolution

    The grid is global with node spacing of 10 arc-minutes (grid-node
    registered) and stored in netCDF with CF-compliant metadata.

    The values are derived from a spherical harmonic model of the ETOPO1
    bedrock grid. Topography values are referenced to "sea level" and are
    positive upwards.

    There are 1081 x 2161 grid points in total. Coordinates are longitude and
    latitude (geodetic).

    **Format:** netCDF4 with zlib compression

    **Load with:** :func:`xarray.load_dataarray` (requires the `netcdf4
    <https://github.com/Unidata/netcdf4-python>`__ library)

    **Datum:** WGS84

    **Original source:** `ETOPO1 <https://doi.org/10.7289/V5C8276M>`__

    **Original license:** Public domain

    Returns
    -------
    fname : :class:`pathlib.Path`
        Path to the downloaded file on disk.

    """
    repository = _make_repository()
    return Path(repository.fetch("earth-topography-10arcmin.nc"))


def fetch_southern_africa_gravity():
    """
    Gravity ground-based surveys of Southern Africa

    This dataset is a compilation of several public domain ground measurements
    of gravity from Southern Africa. The observations are the absolute gravity
    values in mGal. The horizontal datum is not specified and heights are
    referenced to "sea level", which we will interpret as the geoid (which
    realization is likely not relevant since the uncertainty in the height is
    probably larger than geoid model differences).

    There are 14,359 measurements in total with 4 columns available: longitude,
    latitude (geodetic), height (orthometric), and absolute gravity.

    **Format:** CSV with xz (lzma) compression.

    **Load with:** :func:`pandas.read_csv`

    **Datum:** WGS84

    **Original source:** `NOAA NCEI
    <https://ngdc.noaa.gov/mgg/geodas/trackline.html>`__

    **Original license:** Public domain

    Returns
    -------
    fname : :class:`pathlib.Path`
        Path to the downloaded file on disk.

    """
    repository = _make_repository()
    return Path(repository.fetch("southern-africa-gravity.csv.xz"))
