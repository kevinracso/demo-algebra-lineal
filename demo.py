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
from scipy.linalg import solve, solve_triangular, lu, inv


A = np.array([[0, 1, 1, -3],
              [-2, 3, 1,  4],
              [0, 0, 0,  1],
              [3, 1, 0,  0]])

b = np.array([3, -2, 5, 1])

# Solucion directa
x_solve = solve(A, b)

# Ahora PLU
P, L, U = lu(A)
P_inv = inv(P)

b_prima = np.dot(P_inv, b)
y = solve_triangular(L, b_prima, lower=True, unit_diagonal=True)
x_plu = solve_triangular(U, y)

"""
Los metodos anteriores entregan el mismo resultado, obviamente.
La ventaja de uno sobre el otro, depende del problema (por ejemplo, ver Tarea nro. 4)
"""

############################################################
# Eficiencia de solve_triangular vs. solve

# Estudiamos una matriz triangular superior de 100x100 elementos
############################################################
np.random.seed(12389)
Abig = np.random.randint(-10, 20, size=(100, 100))
for i in range(100):
    for j in range(i):
        Abig[i, j] = 0

for i in range(100):
    Abig[i, i] = 1

b = np.random.randint(30, 40, size=100)


"""
usando %timet en ipython comprobamos que solve_triangular es ~10 veces mas rapido que solve para este caso. Tambien inv(A) x b es mas lento que solve.

Los tres metodos equivalentes para despejar x son:

%timeit solve(A, b)
%timeit solve_triangular(A, b)
%timeit np.dot(inv(A), b)
"""
