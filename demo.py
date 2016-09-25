#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Demostracion del uso de la librearia scipy.linalg para resolver sistemas de
ecuaciones.

En particular resolvemos A x = b con

A = np.array([[ 0, 1, 1, -3],
              [-2, 3, 1,  4],
              [ 0, 0, 0,  1],
              [ 3, 1, 0,  0]])

b = np.array([3, -2, 5, 1]).transpose()
"""

import numpy as np


A = np.array([[0, 1, 1, -3],
              [-2, 3, 1,  4],
              [0, 0, 0,  1],
              [3, 1, 0,  0]])

b = np.array([3, -2, 5, 1])
