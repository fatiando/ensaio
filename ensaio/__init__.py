# Copyright (c) 2021 The Ensaio Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
# Import functions/classes to make the public API
from ._fetchers import (
    fetch_alps_gps,
    fetch_britain_magnetic,
    fetch_british_columbia_lidar,
    fetch_bushveld_gravity,
    fetch_caribbean_bathymetry,
    fetch_earth_geoid,
    fetch_earth_gravity,
    fetch_earth_topography,
    fetch_osborne_magnetic,
    fetch_sierra_negra_topography,
    fetch_southern_africa_gravity,
    fetch_southern_africa_topography,
    locate,
)
from ._version import __version__
