#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Combination_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 49,
    label = "CH2O_1* + CH2O_2* <=> HCOOCH3* + Cu*",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A = (2.527e14, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (25.5972083, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 49 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d
"""
)
