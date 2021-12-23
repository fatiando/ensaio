# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
.. _developers:

Using Ensaio in your project
----------------------------

One of the main use cases of Ensaio is to provide reproducible and
easy-to-access data for the documentation of other Python projects.
These are a few tips and tricks for using Ensaio in your own project.
"""
###############################################################################
# Importing a specific version
# ++++++++++++++++++++++++++++
#
# The recommended way to import Ensaio is:

import ensaio.v1 as ensaio

fname = ensaio.fetch_southern_africa_gravity()

###############################################################################
# .. note::
#
#     Replace ``v1`` with the version you want.
#
# Major releases of the data collection that
# break backwards compatibility (and would be likely to break your code) are
# encapsulated in their own modules.
# So using the :mod:`ensaio.v1` module will make sure your code works with
# any version of Ensaio.
#
# Of course, please try to update your code to use newer versions of the data
# collection whenever possible.

###############################################################################
# Download from GitHub on CI
# ++++++++++++++++++++++++++
#
# By default, the data source for Ensaio is an archive with a given DOI.
# You can also specify alternative data download URLs using the
# ``ENSAIO_V1_URL`` environment variable (each data version gets their own
# variable so adjust accordingly).
#
# We recommend using the environment variable to download from the
# GitHub release of the data when running on continuous integration (CI).
# This will minimize the load that is placed on public data servers like
# Zenodo.
# When using GitHub Actions, this may even make the downloads much faster since
# the data source is likely physically closer to the CI infrastructure.
#
# See the ``URL`` module-level variables for each version to find the exact URL
# you need (like :const:`ensaio.v1.URL`).
#
# .. important::
#
#     You may need to update the URL whenever you update Ensaio to access new
#     data added in a minor data release.
#
