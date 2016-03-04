#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sin
from math import cos
from math import pi


# PART 0 - Julian to Gregorian calendar
def gdate(jd):
    L = jd + 68569
    N = 4 * L / 146097
    L = L - (146097 * N + 3) / 4
    I = 4000 * (L + 1) / 1461001
    L = L - 1461 * I / 4 + 31
    J = 80 * L / 2447
    K = L - 2447 * J / 80
    L = J / 11
    J = J + 2 - 12 * L
    I = 100 * (N - 49) + I + L

    year = I
    month = J
    day = K
    return {"y": year, "m": month, "d": day}

# PART 1 - Calculate current Julian day
# - julian_date is the Julian date
# - n is the Julian day since Jan 1st, 2000 12:00
# - 0.0008 is the fractional Julian Day for leap seconds and terrestrial
#   time.
#   currently = 68.184 / 86400 without DUT1
julian_date = 0
n = julian_date - 2451545.0 + 0.0008

# PART 2 - Mean solar noon
# - j_star is an approximation of mean solar time at l_w
# - lw is the longitude west (west is positive, east is negative) of the
#   observer on the Earth
lw = 49
j_star = lw / 360 + n

# PART 3 - Solar mean anomaly
# - m is the solar mean anomaly
m = (357.5291 + 0.98560028 * j_star) % 360

# PART 4 - Equation of the center
# - c is the equation of the center
c = 1.9148 * sin(m) + 0.0200 * sin(2 * m) + 0.0003 * sin(3 * m)

# PART 5 - Ecliptic longitude
# - lamb is the ecliptic longitude
# - 102.9372 is a value for the argument of perihelion
lamb = (m + c + 180 + 102.9372) % 360

# PART 6 - Solar transit
# - j_transit is the hour angle for solar transit (or solar noon)
# - 0.0053 * sin(m) - 0.0069 * sin(2 * lam) is a simplified version of
#   the equation of time
j_transit = 2451545.0 + j_star - (0.0053 * sin(m) - 0.0069 * sin(2 * lamb))

# PART 7 - Declination of the Sun
# - delta  is the declination of the sun
sin_delta = sin(lamb) * sin(23.44)

# PART 8 - Hour angle
# - wo is the hour angle from the observer's zenith
# - phi is the north latitude of the observer (north is positive, south
#   is negative) on the Earth. 0 is the equator
phi = 49
cos_wo = (sin(-0.83) - sin(phi) * sin_delta) / (cos(phi) * cos(sin_delta))

# PART 9 - Calculate sunrise and sunset
# - j_set is the actual Julian date of sunset
# - j_rise is the actual Julian date of sunrise
j_set = j_transit + (cos_wo / 360)
j_rise = j_transit - (cos_wo / 360)

# print "Sunrise: " + str(gdate(2440588))
print "Sunrise: " + str(gdate(j_rise)) + " (" + str(j_rise) + ")"
print "Sunset: " + str(gdate(j_set)) + " (" + str(j_set) + ")"
