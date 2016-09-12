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

plt.show()
