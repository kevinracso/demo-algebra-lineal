# Algebra Lineal

Uso de algunas funciones de algebra lineal

- Resolveremos el problema A x = b, con:

        A = | 0 1 1 -3|
            |-2 3 1  4|
            | 0 0 0  1|
            | 3 1 0  0|

        b = |  3|
            | -2|
            |  5|
            |  1|

Probamos con `scipy.linalg.solve`, `scipy.linalg.solve_triangular`.
