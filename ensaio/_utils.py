# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
Misc utilities used throughout the package.
"""
import os


def download_url(url, env=None):
    """
    Get the download URL from the source or the environment variable if set.

    Makes sure that the URL ends with a trailing ``/`` for Pooch.

    Parameters
    ----------
    url : str
        The canonical URL for downloading the data.
    env : str
        Name of an environment variable that can be used to replace the
        canonical URL.

    Returns
    -------
    url : str
        Sanitized download URL.
    """
    if env is not None and env in os.environ and os.environ[env]:
        url = os.environ[env]
    if not url.endswith("/"):
        url = url + "/"
    return url
