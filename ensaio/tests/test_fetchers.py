# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
Test the dataset download functions and other utilities.
"""

import inspect
import os

import pytest

from .. import _fetchers

FETCH_FUNCTIONS = [
    function
    for name, function in inspect.getmembers(_fetchers, inspect.isfunction)
    if name.startswith("fetch_") and name not in {"fetch_morroco_speleothem_qdm"}
]
FETCH_FUNCTIONS_V2 = [
    _fetchers.fetch_caribbean_bathymetry,
]


@pytest.mark.parametrize("fetch", FETCH_FUNCTIONS)
def test_fetch_datasets(fetch):
    "Check that fetching works and the file exists once downloaded"
    path = fetch(version=1)
    assert path.exists()
    assert "v1" in str(path)


@pytest.mark.parametrize("fetch", FETCH_FUNCTIONS_V2)
def test_fetch_datasets_v2(fetch):
    "Check that fetching v2 works and the file exists once downloaded"
    path = fetch(version=2)
    assert path.exists()
    assert "v2" in str(path)


@pytest.mark.parametrize("file_format", ["matlab", "netcdf"])
def test_fetch_morroco_speleothem(file_format):
    "Check that fetching different formats works"
    extension = {"matlab": ".mat", "netcdf": ".nc"}
    path = _fetchers.fetch_morroco_speleothem_qdm(version=1, file_format=file_format)
    assert path.exists()
    assert "v1" in str(path)
    assert path.suffix == extension[file_format]


def test_fetch_morroco_speleothem_invalid_format():
    "Check that the function fails for invalid formats"
    with pytest.raises(ValueError, match="Invalid data format") as error:
        _fetchers.fetch_morroco_speleothem_qdm(version=1, file_format="csv")
    assert "csv" in str(error)


def test_locate():
    "Check that the cache folder exists by default after a fetch call"
    FETCH_FUNCTIONS[0](version=1)
    path = _fetchers.locate()
    assert path.exists()
    assert path.parts[-1] != "v1"


@pytest.mark.parametrize(
    ("url", "sanitized"),
    [
        ("https://fatiando.org/", "https://fatiando.org/"),
        ("https://fatiando.org", "https://fatiando.org/"),
        ("doi:fatiando/", "doi:fatiando/"),
        ("doi:fatiando", "doi:fatiando/"),
    ],
)
def test_sanitize_url(url, sanitized):
    "Check if url sanitizing works"
    assert _fetchers._sanitize_url(url) == sanitized


@pytest.mark.parametrize(
    "use_github",
    ["True", "False"],
)
def test_data_source_from_github(use_github):
    "Check that GitHub is used as a data source when the env variable is set"
    backup = None
    try:
        backup = os.environ.get("ENSAIO_DATA_FROM_GITHUB")
        os.environ["ENSAIO_DATA_FROM_GITHUB"] = use_github
        repo = _fetchers._repository(fname="alps-gps-velocity.csv.xz", version=1)
        marker = "https://github.com" if use_github == "True" else "doi:"
        assert all(url.startswith(marker) for url in repo.urls.values())
    finally:
        if backup is None:
            os.environ.pop("ENSAIO_DATA_FROM_GITHUB")
        else:
            os.environ["ENSAIO_DATA_FROM_GITHUB"] = backup


def test_check_versions():
    "Make sure an exception is raised for invalid versions"
    with pytest.raises(ValueError, match="Invalid version=3") as error:
        _fetchers._check_versions(version=3, allowed={1, 2}, name="Bla")
    assert "Bla" in str(error)
