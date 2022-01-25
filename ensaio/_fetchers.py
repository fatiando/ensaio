# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
"""
Functions that fetch each of our sample datasets.
"""
import os
from pathlib import Path

import pooch

REGISTRY = {
    "v1": [
        {
            "fname": "southern-africa-gravity.csv.xz",
            "hash": "md5:1dee324a14e647855366d6eb01a1ef35",
            "doi": "doi:10.5281/zenodo.5882430",
            "url": "https://github.com/fatiando-data/southern-africa-gravity/releases/download/v1",
        },
    ],
}


def _repository(version):
    """
    Create the Pooch instance that fetches the datasets of a particular version

    Cache location defaults to ``pooch.os_cache("ensaio")`` and can be
    overwritten with the ``ENSAIO_DATA_DIR`` environment variable.

    The data source defaults to the Zenodo DOI and can be switched to the
    GitHub release URL by setting the environment variable
    ``ENSAIO_DATA_FROM_GITHUB=true``.

    Parameters
    ----------
    version : int
        Version number of the datasets that we want to fetch.

    Returns
    -------
    repository : :class:`pooch.Pooch`

    """
    version_str = f"v{version}"
    envvar = "ENSAIO_DATA_FROM_GITHUB"
    if envvar in os.environ and os.environ[envvar].lower() == "true":
        source = "url"
    else:
        source = "doi"
    urls = {
        entry["fname"]: _sanitize_url(entry[source]) + entry["fname"]
        for entry in REGISTRY[version_str]
    }
    registry = {entry["fname"]: entry["hash"] for entry in REGISTRY[version_str]}
    repository = pooch.create(
        path=Path(pooch.os_cache("ensaio")),
        # Just here so that Pooch doesn't complain about there not being a
        # format marker in the string.
        base_url="{version}",
        version=version_str,
        env="ENSAIO_DATA_DIR",
        retry_if_failed=3,
        registry=registry,
        urls=urls,
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
    return _repository(version=1).abspath.parent


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

    Returns
    -------
    fname : :class:`pathlib.Path`
        Path to the downloaded file on disk.

    """
    _check_versions(version, allowed={1}, name="Southern Africa gravity")
    return Path(_repository(version).fetch("southern-africa-gravity.csv.xz"))
