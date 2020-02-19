#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Combination_vdW/rules"
shortDesc = u""
longDesc = u"""
Two vdW species combining together.
"""

entry(
    index = 1,
    label = "Adsorbate1;Adsorbate2",
    kinetics = SurfaceArrheniusBEP(
        A = (1.0e13, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.5,
        E0 = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""Made up"""
)
