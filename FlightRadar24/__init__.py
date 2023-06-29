# -*- coding: utf-8 -*-

"""
API for FlightRadar24.

This API provides flight and airport data available to the public
on the FlightRadar24 website. If you want to use the data collected
using this API commercially, you need to subscribe to the Business plan.

See more information at:
https://www.flightradar24.com/premium/
https://www.flightradar24.com/terms-and-conditions
"""

__author__ = "Jean Loui Bernard Silva de Jesus"
__version__ = "1.3.9"

from .api import FlightRadar24API, FlightTrackerConfig
from .entities import Airport, Flight
