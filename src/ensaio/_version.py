# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
Format the automatically generated version information from setuptools_scm.
"""

# This file is generated automatically by setuptools_scm
from . import _version_generated

# Add a "v" to the version number made by setuptools_scm
__version__ = f"v{_version_generated.version}"
