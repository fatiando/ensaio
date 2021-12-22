# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
Test the misc utilities.
"""
import os

import pytest

from .._utils import download_url


@pytest.mark.parametrize(
    "url,sanitized",
    [
        ("https://fatiando.org/", "https://fatiando.org/"),
        ("https://fatiando.org", "https://fatiando.org/"),
        ("doi:fatiando/", "doi:fatiando/"),
        ("doi:fatiando", "doi:fatiando/"),
    ],
)
def test_download_url(url, sanitized):
    "Check if the output is a sanitized url for different inputs."
    assert download_url(url) == sanitized


@pytest.mark.parametrize(
    "url,sanitized",
    [
        ("https://fatiando.org/", "https://fatiando.org/"),
        ("https://fatiando.org", "https://fatiando.org/"),
        ("doi:fatiando/", "doi:fatiando/"),
        ("doi:fatiando", "doi:fatiando/"),
    ],
)
def test_download_url_env(url, sanitized):
    "Check if the setting an environment variable works"
    env = "ENSAIO_TEST_VARIABLE"
    try:
        os.environ[env] = url
        assert download_url(url="bla", env=env) == sanitized
    finally:
        os.environ.pop(env)
