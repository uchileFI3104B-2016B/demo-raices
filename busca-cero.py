#! /usr/bin/env python

"""
Este script busca el punto de interseccion entre seno y coseno
(en el rango 0, pi) usando el metodo de la biseccion.
"""

import numpy as np
import matplotlib.pyplot as plt


x_values = np.linspace(0, np.pi, 100)
plt.clf()
plt.plot(x_values, np.sin(x_values), 'b', label='sin(x)')
plt.plot(x_values, np.cos(x_values), 'r', label='cos(x)')
plt.xlabel('x [radianes]')
plt.legend()


def seno_menos_coseno(x):
    output = np.sin(x) - np.cos(x)
    return output

def biseccion(func, a, b, numero_de_iteraciones=10):
    """
    Busca el cero de la funcion func, ubicado entre a y b
    usando el metodo de la biseccion.
    """
    p = (a + b) / 2
    counter = 0
    while counter < numero_de_iteraciones:
        if func(p) == 0:
            return p
        if func(a) * func(p) > 0:
            a = p
        else:
            b = p
        p = (a + b) / 2
        counter += 1
    return p


cero = biseccion(seno_menos_coseno, 0., 1.5, numero_de_iteraciones=10)

plt.axvline(cero, color='g')


plt.show()
