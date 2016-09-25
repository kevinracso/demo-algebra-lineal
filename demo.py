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

Tambien demostramos la eficiencia de solve_triangular vs. solve.
"""

from __future__ import division
import numpy as np


A = np.array([[0, 1, 1, -3],
              [-2, 3, 1,  4],
              [0, 0, 0,  1],
              [3, 1, 0,  0]])

b = np.array([3, -2, 5, 1])



############################################################
# Eficiencia de solve_triangular vs. solve
############################################################
np.random.seed(12389)
A = np.random.randint(-10, 20, size=(100, 100))
for i in range(100):
    for j in range(i):
        A[i, j] = 0

for i in range(100):
    A[i, i] = 1

b = np.random.randint(30, 40, size=100)
