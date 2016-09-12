#! /usr/bin/env python

"""
Este script busca el punto de interseccion entre seno y coseno
(en el rango 0, pi) usando el metodo de la biseccion.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect

x_values = np.linspace(0, np.pi, 100)
plt.clf()
plt.plot(x_values, np.sin(x_values), 'b', label='sin(x)')
plt.plot(x_values, np.cos(x_values), 'r', label='cos(x)')
plt.xlabel('x [radianes]')


def seno_menos_coseno(x):
    output = np.sin(x) - np.cos(x)
    return output

def biseccion(func, a, b, itermax=100, tolerancia=1e-4):
    """
    Busca el cero de la funcion func, ubicado entre a y b
    usando el metodo de la biseccion.
    """
    p = (a + b) / 2
    counter = 0
    while (np.fabs(func(p)) > tolerancia) and (counter < itermax):
        if func(p) == 0:
            return p
        if func(a) * func(p) > 0:
            a = p
        else:
            b = p
        p = (a + b) / 2
        counter += 1
    return p


cero = biseccion(seno_menos_coseno, 0., 1.5, tolerancia=0.1)
cero_mejor = biseccion(seno_menos_coseno, 0., 1.5, tolerancia=1e-5)

cero_scipy = bisect(seno_menos_coseno, 0, 1.5, xtol=1e-5)

#plt.axvline(cero, color='g')
plt.axvline(cero_mejor, color='k', label='esta implementacion')
plt.axvline(cero_scipy, color='c', label='scipy')

plt.legend()
# plt.show()
plt.savefig('raiz.png')
