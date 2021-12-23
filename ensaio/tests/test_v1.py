# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
Test the version 1 dataset download functions.
"""
import inspect

import pytest

from .. import v1

FETCH_FUNCTIONS = [
    function
    for name, function in inspect.getmembers(v1, inspect.isfunction)
    if name.startswith("fetch_")
]


@pytest.mark.parametrize("fetch", FETCH_FUNCTIONS)
def test_v1_fetch_datasets(fetch):
    "Check that fetching works and the file exists once downloaded"
    path = fetch()
    assert path.exists()


def test_v1_locate():
    "Check that the cache folder exists by default after a fetch call"
    FETCH_FUNCTIONS[0]()
    path = v1.locate()
    assert path.exists()
