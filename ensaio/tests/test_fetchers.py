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
    if name.startswith("fetch_")
]


@pytest.mark.parametrize("fetch", FETCH_FUNCTIONS)
def test_fetch_datasets(fetch):
    "Check that fetching works and the file exists once downloaded"
    path = fetch(version=1)
    assert path.exists()


def test_locate():
    "Check that the cache folder exists by default after a fetch call"
    FETCH_FUNCTIONS[0](version=1)
    path = _fetchers.locate()
    assert path.exists()
    assert path.parts[-1] != "v1"


@pytest.mark.parametrize(
    "url,sanitized",
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
        backup = os.environ.get("ENSAIO_DATA_FROM_GITHUB", None)
        os.environ["ENSAIO_DATA_FROM_GITHUB"] = use_github
        repo = _fetchers._repository(fname="alps-gps-velocity.csv.xz", version=1)
        if use_github == "True":
            marker = "https://github.com"
        else:
            marker = "doi:"
        assert all(url.startswith(marker) for url in repo.urls.values())
    finally:
        if backup is None:
            os.environ.pop("ENSAIO_DATA_FROM_GITHUB")
        else:
            os.environ["ENSAIO_DATA_FROM_GITHUB"] = backup


def test_check_versions():
    "Make sure an exception is raised for invalid versions"
    with pytest.raises(ValueError) as error:
        _fetchers._check_versions(version=3, allowed={1, 2}, name="Bla")
    assert "Bla" in str(error)
