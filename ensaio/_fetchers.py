# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
Functions that fetch each of our sample datasets.
"""
import os
from pathlib import Path

import pooch

REGISTRY = {
    "alps-gps-velocity.csv.xz": {
        "v1": {
            "hash": "md5:195ee3d88783ce01b6190c2af89f2b14",
            "doi": "doi:10.5281/zenodo.5879163",
            "url": "https://github.com/fatiando-data/alps-gps-velocity/releases/download/v1",
        },
    },
    "britain-magnetic.csv.xz": {
        "v1": {
            "hash": "md5:8dbbda02c7e74f63adc461909358f056",
            "doi": "doi:10.5281/zenodo.5879260",
            "url": "https://github.com/fatiando-data/britain-magnetic/releases/download/v1",
        },
    },
    "british-columbia-lidar.csv.xz": {
        "v1": {
            "hash": "md5:354c725a95036bd8340bc14e043ece5a",
            "doi": "doi:10.5281/zenodo.5881887",
            "url": "https://github.com/fatiando-data/british-columbia-lidar/releases/download/v1",
        },
    },
    "bushveld-gravity.csv.xz": {
        "v1": {
            "hash": "md5:368284cc210c6bbe256e9e49e892f262",
            "doi": "doi:10.5281/zenodo.6511942",
            "url": "https://github.com/fatiando-data/bushveld-gravity/releases/download/v1",
        },
    },
    "caribbean-bathymetry.csv.xz": {
        "v1": {
            "hash": "md5:a7332aa6e69c77d49d7fb54b764caa82",
            "doi": "doi:10.5281/zenodo.5882211",
            "url": "https://github.com/fatiando-data/caribbean-bathymetry/releases/download/v1",
        },
    },
    "earth-geoid-10arcmin.nc": {
        "v1": {
            "hash": "md5:39b97344e704eb68fa381df2eb47da0f",
            "doi": "doi:10.5281/zenodo.5882205",
            "url": "https://github.com/fatiando-data/earth-geoid-10arcmin/releases/download/v1",
        },
    },
    "earth-gravity-10arcmin.nc": {
        "v1": {
            "hash": "md5:56df20e0e67e28ebe4739a2f0357c4a6",
            "doi": "doi:10.5281/zenodo.5882207",
            "url": "https://github.com/fatiando-data/earth-gravity-10arcmin/releases/download/v1",
        },
    },
    "earth-topography-10arcmin.nc": {
        "v1": {
            "hash": "md5:c43b61322e03669c4313ba3d9a58028d",
            "doi": "doi:10.5281/zenodo.5882203",
            "url": "https://github.com/fatiando-data/earth-topography-10arcmin/releases/download/v1",
        },
    },
    "osborne-magnetic.csv.xz": {
        "v1": {
            "hash": "md5:b26777bdde2f1ecb97dda655c8b1cf71",
            "doi": "doi:10.5281/zenodo.5882209",
            "url": "https://github.com/fatiando-data/osborne-magnetic/releases/download/v1",
        },
    },
    "sierra-negra-topography.csv.xz": {
        "v1": {
            "hash": "md5:9f6f64d47d26773e37b154cf964724e3",
            "doi": "doi:10.5281/zenodo.6139057",
            "url": "https://github.com/fatiando-data/sierra-negra-topography/releases/download/v1",
        },
    },
    "southern-africa-gravity.csv.xz": {
        "v1": {
            "hash": "md5:1dee324a14e647855366d6eb01a1ef35",
            "doi": "doi:10.5281/zenodo.5882430",
            "url": "https://github.com/fatiando-data/southern-africa-gravity/releases/download/v1",
        },
    },
    "southern-africa-topography.nc": {
        "v1": {
            "hash": "md5:609d14fe4e551c5dcf320cdceedd30e8",
            "doi": "doi:10.5281/zenodo.6481379",
            "url": "https://github.com/fatiando-data/southern-africa-topography/releases/download/v1",
        },
    },
}


def _repository(fname, version):
    """
    Create the Pooch instance that fetches a dataset of a particular version

    Cache location defaults to ``pooch.os_cache("ensaio")`` and can be
    overwritten with the ``ENSAIO_DATA_DIR`` environment variable.

    The data source defaults to the Zenodo DOI and can be switched to the
    GitHub release URL by setting the environment variable
    ``ENSAIO_DATA_FROM_GITHUB=true``.

    Parameters
    ----------
    fname : str
        Name of the data file we want to fetch.
    version : int
        Version number of the dataset that we want to fetch.

    Returns
    -------
    repository : :class:`pooch.Pooch`

    """
    version_str = f"v{version}"
    # Decide if we need to pull data from GitHub or the Zenodo DOIs
    envvar = "ENSAIO_DATA_FROM_GITHUB"
    if envvar in os.environ and os.environ[envvar].lower() == "true":
        source = "url"
    else:
        source = "doi"
    entry = REGISTRY[fname][version_str]
    repository = pooch.create(
        path=Path(pooch.os_cache("ensaio")),
        # Just here so that Pooch doesn't complain about there not being a
        # format marker in the string.
        base_url="{version}",
        version=version_str,
        env="ENSAIO_DATA_DIR",
        retry_if_failed=3,
        registry={fname: entry["hash"]},
        urls={fname: _sanitize_url(entry[source]) + fname},
    )
    return repository


def _sanitize_url(url):
    """
    Makes sure that the URL ends with a trailing ``/`` for Pooch.

    Parameters
    ----------
    url : str
        The URL for downloading the data, with or without a trailing ``/``.

    Returns
    -------
    url : str
        Sanitized download URL.
    """
    if not url.endswith("/"):
        return url + "/"
    return url


def locate():
    """
    Return the location of the system-dependent data cache folder

    This folder is not guaranteed to exist in the file system until a dataset
    has been downloaded.

    The default location is a ``ensaio/`` folder in the system-dependent
    default cache folder. A different path can also be specified through the
    ``ENSAIO_DATA_DIR`` environment variable.

    Returns
    -------
    path : :class:`pathlib.Path`
        Path to the cache folder.
    """
    return _repository(fname="alps-gps-velocity.csv.xz", version=1).abspath.parent


def _check_versions(version, allowed, name):
    """
    Check if the version is in the allowed range, raise an error if not.

    Parameters
    ----------
    version : int
        Integer version of the data.
    allowed : set or list
        List or set of allowed values for the version.
    name : str
        Name of the dataset (used in the error message).

    """
    if version not in allowed:
        raise ValueError(
            f"Invalid version={version} for {name} dataset. Must be one of {allowed}."
        )


def fetch_alps_gps(version):
    """
    Alpine 3-component GPS velocity dataset

    This is a compilation of 3D GPS velocities for the Alps. The horizontal
    velocities are reference to the Eurasian frame. Coordinates are referenced
    to WGS84. All velocity components and even the position have error
    estimates, which is very useful and rare to find in a lot of datasets.

    There ~200 stations in total. The data available are: station ID,
    longitude, latitude (geodetic), height (geometric), ground velocity in the
    East, North, and upward directions, and the estimated uncertainties in each
    of these.

    **Format:** CSV with xz (lzma) compression.

    **Load with:** :func:`pandas.read_csv`

    **Original source:**
    `Sánchez et al. (2018) <https://doi.org/10.1594/PANGAEA.886889>`__

    **Original license:** CC-BY

    **Versions:**

    * `1
      <https://github.com/fatiando-data/alps-gps-velocity/releases/tag/v1>`_
      (doi:`10.5281/zenodo.5879163 <https://doi.org/10.5281/zenodo.5879163>`__)

    Parameters
    ----------
    version : int
        The data version to fetch. See the available versions above.

    Returns
    -------
    fname : :class:`pathlib.Path`
        Path to the downloaded file on disk.

    """
    _check_versions(version, allowed={1}, name="Alps GPS velocity")
    fname = "alps-gps-velocity.csv.xz"
    return Path(_repository(fname, version).fetch(fname))


def fetch_britain_magnetic(version):
    """
    Digitized airborne magnetic survey of Britain

    This is a digitization of an airborne magnetic survey of Britain. Data are
    sampled where flight lines crossed contours on the archive maps. Contains
    only the total field magnetic anomaly, not the magnetic field intensity
    measurements or corrections.

    The exact date of measurements is not available (only the year). The
    horizontal datum is WGS84 but the vertical datum is not specified.

    There are 541,508 measurements in total with 6 columns available: line and
    segment ID, year, longitude, latitude (geodetic), height (unknown datum),
    total field magnetic anomaly.

    Contains British Geological Survey materials © UKRI 2021.

    **Format:** CSV with xz (lzma) compression.

    **Load with:** :func:`pandas.read_csv`

    **Original source:**
    `British Geological Survey
    <https://www.bgs.ac.uk/datasets/gb-aeromagnetic-survey/>`__

    **Original license:** Open Government Licence

    **Versions:**

    * `1
      <https://github.com/fatiando-data/britain-magnetic/releases/tag/v1>`_
      (doi:`10.5281/zenodo.5879260 <https://doi.org/10.5281/zenodo.5879260>`__)

    Parameters
    ----------
    version : int
        The data version to fetch. See the available versions above.

    Returns
    -------
    fname : :class:`pathlib.Path`
        Path to the downloaded file on disk.

    """
    _check_versions(version, allowed={1}, name="Britain aeromagnetic")
    fname = "britain-magnetic.csv.xz"
    return Path(_repository(fname, version).fetch(fname))


def fetch_british_columbia_lidar(version):
    """
    Topography (lidar point cloud) data of the Trail Islands in BC, Canada

    This is a lidar point cloud (ground reflections only) sliced to the small
    `Trail Islands <https://apps.gov.bc.ca/pub/bcgnws/names/21973.html>`__
    to the North of Vancouver. The islands have some nice looking topography
    and their isolated nature creates problems for some interpolation methods.

    The horizontal datum is WGS84 and the elevation is referenced to "mean sea
    level".

    There are ~800,000 measurements in total with 3 columns available:
    longitude, latitude (geodetic), and ground elevation (orthometric).

    **Format:** CSV with xz (lzma) compression.

    **Load with:** :func:`pandas.read_csv`

    **Original source:** `LidarBC
    <https://www2.gov.bc.ca/gov/content/data/geographic-data-services/lidarbc>`__

    **Original license:** Open Government Licence - British Columbia

    **Versions:**

    * `1
      <https://github.com/fatiando-data/british-columbia-lidar/releases/tag/v1>`_
      (doi:`10.5281/zenodo.5881887 <https://doi.org/10.5281/zenodo.5881887>`__)

    Parameters
    ----------
    version : int
        The data version to fetch. See the available versions above.

    Returns
    -------
    fname : :class:`pathlib.Path`
        Path to the downloaded file on disk.

    """
    _check_versions(version, allowed={1}, name="British Columbia lidar")
    fname = "british-columbia-lidar.csv.xz"
    return Path(_repository(fname, version).fetch(fname))


def fetch_bushveld_gravity(version):
    """
    Gravity ground-based data over the Bushveld Complex, Southern Africa

    This dataset contains ground gravity observations over the area that
    comprises the Bushveld Igenous Complex in Southern Africa, including
    preprocessed gravity fields such as the **gravity disturbance** and the
    **bouguer gravity disturbance** (topography-free gravity disturbance). In
    addition, the dataset contains the heights of the observation points
    referenced on the WGS84 reference ellipsoid and over the mean sea-level
    (what can be considered to be the geoid). This dataset was built upon
    a portion of the Southern Africa gravity compilation available through
    `NOAA NCEI <https://www.ngdc.noaa.gov/mgg/gravity/>`__.

    **Format:** CSV with xz (lzma) compression.

    **Load with:** :func:`pandas.read_csv`

    **Original source:** `NOAA NCEI <https://www.ngdc.noaa.gov/mgg/gravity/>`__
    (gravity) and `ETOPO1 <https://doi.org/10.7289/V5C8276M>`__ (topography)

    **Original license:** `public domain
    <https://ngdc.noaa.gov/ngdcinfo/privacy.html>`__ (gravity) and `public
    domain <https://ngdc.noaa.gov/mgg/global/dem_faq.html#sec-2.4>`__
    (topography)

    **Versions:**

    * `1
      <https://github.com/fatiando-data/bushveld-gravity/releases/tag/v1>`_
      (doi:`10.5281/zenodo.6511942 <https://doi.org/10.5281/zenodo.6511942>`__)

    Parameters
    ----------
    version : int
        The data version to fetch. See the available versions above.

    Returns
    -------
    fname : :class:`pathlib.Path`
        Path to the downloaded file on disk.
    """
    _check_versions(version, allowed={1}, name="Bushveld gravity data")
    fname = "bushveld-gravity.csv.xz"
    return Path(_repository(fname, version).fetch(fname))


def fetch_caribbean_bathymetry(version):
    """
    Single-beam bathymetry of the Caribbean

    This dataset is a compilation of several public domain single-beam
    bathymetry surveys of the ocean in the Caribbean. The data display a wide
    range of tectonic activity, uneven distribution, and even clear systematic
    errors in some of the survey lines.

    The horizontal datum is WGS84 and the bathymetric depth is positive
    downwards and referenced to "mean sea level".

    There are 1,938,095 measurements in total with 4 columns available:
    survey ID, longitude, latitude (geodetic), and depth.

    **Format:** CSV with xz (lzma) compression.

    **Load with:** :func:`pandas.read_csv`

    **Original source:** `NOAA NCEI
    <https://ngdc.noaa.gov/mgg/geodas/trackline.html>`__

    **Original license:** Public domain

    **Versions:**

    * `1
      <https://github.com/fatiando-data/caribbean-bathymetry/releases/tag/v1>`_
      (doi:`10.5281/zenodo.5882211 <https://doi.org/10.5281/zenodo.5882211>`__)

    Parameters
    ----------
    version : int
        The data version to fetch. See the available versions above.

    Returns
    -------
    fname : :class:`pathlib.Path`
        Path to the downloaded file on disk.

    """
    _check_versions(version, allowed={1}, name="Caribbean bathymetry")
    fname = "caribbean-bathymetry.csv.xz"
    return Path(_repository(fname, version).fetch(fname))


def fetch_earth_geoid(version):
    """
    Geoid height of the Earth at 10 arc-minute resolution

    The grid is global with node spacing of 10 arc-minutes (grid-node
    registered) and stored in netCDF with CF-compliant metadata.
    The geoid height is derived from the EIGEN-6C4 spherical harmonic model of
    the Earth's gravity field with respect to the WGS84 ellipsoid.

    The horizontal datum is WGS84.

    There are 1081 x 2161 grid points in total. Coordinates are longitude and
    latitude (geodetic).

    **Format:** netCDF4 with zlib compression

    **Load with:** :func:`xarray.load_dataarray` (requires the `netcdf4
    <https://github.com/Unidata/netcdf4-python>`__ library)

    **Original source:** `EIGEN-6C4 model
    <https://doi.org/10.5880/icgem.2015.1>`__

    **Original license:** CC-BY

    **Versions:**

    * `1
      <https://github.com/fatiando-data/earth-geoid-10arcmin/releases/tag/v1>`_
      (doi:`10.5281/zenodo.5882205 <https://doi.org/10.5281/zenodo.5882205>`__)

    Parameters
    ----------
    version : int
        The data version to fetch. See the available versions above.

    Returns
    -------
    fname : :class:`pathlib.Path`
        Path to the downloaded file on disk.

    """
    _check_versions(version, allowed={1}, name="Earth geoid grid")
    fname = "earth-geoid-10arcmin.nc"
    return Path(_repository(fname, version).fetch(fname))


def fetch_earth_gravity(version):
    """
    Gravity of the Earth at 10 arc-minute resolution

    The grid is global with node spacing of 10 arc-minutes (grid-node
    registered) and stored in netCDF with CF-compliant metadata.

    The gravity values are derived from the EIGEN-6C4 spherical harmonic model
    (calculated uniformly at 10 km above the WGS84 ellipsoid). Here "gravity"
    refers to the combined gravitational and centrifugal accelerations.

    The horizontal and vertical datum is WGS84.

    There are 1081 x 2161 grid points in total. Coordinates are longitude and
    latitude (geodetic) plus a non-dimensional coordinate height (geometric).

    **Format:** netCDF4 with zlib compression

    **Load with:** :func:`xarray.load_dataarray` (requires the `netcdf4
    <https://github.com/Unidata/netcdf4-python>`__ library)

    **Original source:** `EIGEN-6C4 model
    <https://doi.org/10.5880/icgem.2015.1>`__

    **Original license:** CC-BY

    **Versions:**

    * `1
      <https://github.com/fatiando-data/earth-gravity-10arcmin/releases/tag/v1>`_
      (doi:`10.5281/zenodo.5882207 <https://doi.org/10.5281/zenodo.5882207>`__)

    Parameters
    ----------
    version : int
        The data version to fetch. See the available versions above.

    Returns
    -------
    fname : :class:`pathlib.Path`
        Path to the downloaded file on disk.

    """
    _check_versions(version, allowed={1}, name="Earth gravity grid")
    fname = "earth-gravity-10arcmin.nc"
    return Path(_repository(fname, version).fetch(fname))


def fetch_earth_topography(version):
    """
    Topography of the Earth at 10 arc-minute resolution

    The grid is global with node spacing of 10 arc-minutes (grid-node
    registered) and stored in netCDF with CF-compliant metadata.

    The values are derived from a spherical harmonic model of the ETOPO1
    bedrock grid. Topography/bathymetry values are referenced to "sea level"
    and are positive upwards. The horizontal datum is WGS84.

    There are 1081 x 2161 grid points in total. Coordinates are longitude and
    latitude (geodetic).

    **Format:** netCDF4 with zlib compression

    **Load with:** :func:`xarray.load_dataarray` (requires the `netcdf4
    <https://github.com/Unidata/netcdf4-python>`__ library)

    **Original source:** `ETOPO1 <https://doi.org/10.7289/V5C8276M>`__

    **Original license:** Public domain

    **Versions:**

    * `1
      <https://github.com/fatiando-data/earth-topography-10arcmin/releases/tag/v1>`_
      (doi:`10.5281/zenodo.5882203 <https://doi.org/10.5281/zenodo.5882203>`__)

    Parameters
    ----------
    version : int
        The data version to fetch. See the available versions above.

    Returns
    -------
    fname : :class:`pathlib.Path`
        Path to the downloaded file on disk.

    """
    _check_versions(version, allowed={1}, name="Earth topography grid")
    fname = "earth-topography-10arcmin.nc"
    return Path(_repository(fname, version).fetch(fname))


def fetch_osborne_magnetic(version):
    """
    Magnetic airborne survey of the Osborne Mine and surroundings, Australia

    This is a section of a survey acquired in 1990 by the Queensland
    Government, Australia. The line data have approximately 80 m terrain
    clearance and 200 m line spacing. Total field anomalies are in nT. The
    flight height was calculated by summing the terrain clearance to
    interpolated values of SRTM (referenced to sea level). The section contains
    the total field magnetic anomalies associated with the Osborne Mine,
    Lightning Creek sill complex, and the Brumby prospect.

    There are ~990,000 measurements in total with 5 columns available: flight
    line number, longitude, latitude (geodetic), height (orthometric), and the
    total field magnetic anomaly.

    **Format:** CSV with xz (lzma) compression.

    **Load with:** :func:`pandas.read_csv`

    **Original source:** `Geophysical Acquisition & Processing Section 2019.
    MIM Data from Mt Isa Inlier, QLD (P1029), magnetic line data, AWAGS
    levelled. Geoscience Australia, Canberra
    <http://pid.geoscience.gov.au/dataset/ga/142419>`__

    **Original license:** CC-BY

    **Versions:**

    * `1
      <https://github.com/fatiando-data/osborne-magnetic/releases/tag/v1>`_
      (doi:`10.5281/zenodo.5882209 <https://doi.org/10.5281/zenodo.5882209>`__)

    Parameters
    ----------
    version : int
        The data version to fetch. See the available versions above.

    Returns
    -------
    fname : :class:`pathlib.Path`
        Path to the downloaded file on disk.

    """
    _check_versions(version, allowed={1}, name="Osborne mine magnetic")
    fname = "osborne-magnetic.csv.xz"
    return Path(_repository(fname, version).fetch(fname))


def fetch_sierra_negra_topography(version):
    """
    Topography of the 2018 lava flows of the Sierra Negra volcano, Ecuador

    This is a structure-from-motion point cloud of the 2018 lava flows of the
    Sierra Negra volcano, located on the Galápagos islands, Ecuador. The survey
    is of a small region on the flank of the volcano. The horizontal datum is
    WGS84 but the vertical datum for "elevation" is unspecified.

    There are ~1,700,000 measurements in total with 3 columns available:
    longitude, latitude (geodetic), elevation.

    **Format:** CSV with xz (lzma) compression.

    **Load with:** :func:`pandas.read_csv`

    **Original source:** `Carr, B. (2020). Sierra Negra Volcano (TIR Flight 3):
    Galápagos, Ecuador, October 22 2018. Distributed by OpenTopography.
    <https://doi.org/10.5069/G957196P>`__

    **Original license:** CC-BY

    **Versions:**

    * `1
      <https://github.com/fatiando-data/sierra-negra-topography/releases/tag/v1>`_
      (doi:`10.5281/zenodo.6139057 <https://doi.org/10.5281/zenodo.6139057>`__)

    Parameters
    ----------
    version : int
        The data version to fetch. See the available versions above.

    Returns
    -------
    fname : :class:`pathlib.Path`
        Path to the downloaded file on disk.

    """
    _check_versions(version, allowed={1}, name="Sierra Negra volcano topography")
    fname = "sierra-negra-topography.csv.xz"
    return Path(_repository(fname, version).fetch(fname))


def fetch_southern_africa_gravity(version):
    """
    Gravity ground-based surveys of Southern Africa

    This dataset is a compilation of several public domain ground measurements
    of gravity from Southern Africa. The observations are the absolute gravity
    values in mGal. The horizontal datum is not specified and heights are
    referenced to "sea level", which we will interpret as the geoid (which
    realization is likely not relevant since the uncertainty in the height is
    probably larger than geoid model differences).

    There are ~14,000 measurements in total with 4 columns available:
    longitude, latitude (geodetic), height (orthometric), and absolute gravity.

    **Format:** CSV with xz (lzma) compression.

    **Load with:** :func:`pandas.read_csv`

    **Original source:** `NOAA NCEI
    <https://ngdc.noaa.gov/mgg/geodas/trackline.html>`__

    **Original license:** Public domain

    **Versions:**

    * `1
      <https://github.com/fatiando-data/southern-africa-gravity/releases/tag/v1>`_
      (doi:`10.5281/zenodo.5882430 <https://doi.org/10.5281/zenodo.5882430>`__)

    Parameters
    ----------
    version : int
        The data version to fetch. See the available versions above.

    Returns
    -------
    fname : :class:`pathlib.Path`
        Path to the downloaded file on disk.

    """
    _check_versions(version, allowed={1}, name="Southern Africa gravity")
    fname = "southern-africa-gravity.csv.xz"
    return Path(_repository(fname, version).fetch(fname))


def fetch_southern_africa_topography(version):
    """
    Topography and bathymetry data for Southern Africa

    This is a topography and bathymetry grid with a resolution of 1 arc-minute
    over Southern Africa. The grid was generated by cropping the ETOPO1 global
    topography grid. The heights are referenced to the mean sea level.

    **Format:** netCDF4 with zlib compression

    **Load with:** :func:`xarray.load_dataarray` (requires the `netcdf4
    <https://github.com/Unidata/netcdf4-python>`__ library)

    **Original source:** `ETOPO1 <https://doi.org/10.7289/V5C8276M>`__

    **Original license:** Public domain

    **Versions:**

    * `1
      <https://github.com/fatiando-data/southern-africa-topography/releases/tag/v1>`_
      (doi:`10.5281/zenodo.6481379 <https://doi.org/10.5281/zenodo.6481379>`__)

    Parameters
    ----------
    version : int
        The data version to fetch. See the available versions above.

    Returns
    -------
    fname : :class:`pathlib.Path`
        Path to the downloaded file on disk.

    """
    _check_versions(version, allowed={1}, name="Southern Africa topography")
    fname = "southern-africa-topography.nc"
    return Path(_repository(fname, version).fetch(fname))
