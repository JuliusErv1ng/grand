'''GRAND software package
'''
from .tools import geomagnet, topography
from .tools.topography import geoid_undulation, Reference, Topography

# RK
from .tools.geomagnet import Geomagnet
from .tools import coordinates
from .tools.coordinates import Coordinates, CartesianRepresentation, SphericalRepresentation, \
							   GeodeticRepresentation, Geodetic, \
							   GRANDCS, LTP, ECEF, HorizontalVector, Horizontal,\
							   Rotation

from .logging import getLogger, Logger
from . import logging, store


__all__ = ['geomagnet', 'getLogger', 'store', 'topography', 'ECEF',
		   'Geodetic', 'GeodeticRepresentation', 'GRANDCS', 'coordinates',
		   'Logger', 'LTP', 'SphericalRepresentation', 'CartesianRepresentation', 'Rotation']

logger:Logger = getLogger(__name__)