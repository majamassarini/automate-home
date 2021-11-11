# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini


class Position(object):
    """
    An object which describe the position of an object.
    """

    def __init__(
        self,
        bottom_altitude: float,
        upper_altitude: float,
        min_azimuth: float,
        max_azimuth: float,
    ):
        self.bottom_altitude = bottom_altitude
        self.upper_altitude = upper_altitude
        self.min_azimuth = min_azimuth
        self.max_azimuth = max_azimuth

    def __str__(self):
        return "(altitude: %s-%s, azimuth: %s-%s)" % (
            self.bottom_altitude,
            self.upper_altitude,
            self.min_azimuth,
            self.max_azimuth,
        )

    def is_sun_over(self, sun_position: "home.scheduler.trigger.sun.Position") -> bool:
        """
        Given the sun position, say if the object is hit by the sun

        :param sun_position: the sun *Position*
        :return: is the object hit by the sun?
        """
        if (self.bottom_altitude <= sun_position.altitude <= self.upper_altitude) and (
            self.min_azimuth <= sun_position.azimuth <= self.max_azimuth
        ):
            return True
        else:
            return False
