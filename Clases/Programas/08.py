#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Moctezuma Soto, Fernando
310126070
Taller de herramientas computacionales

Programa que imprime "Hoy es miércoles"
'''


x = 10.5;  y = 1.0/3;  z = 15.3
# x, y, z = 10.5, 1.0/3, 15.3

H = """El punto en R3 es:
(x, y, z) = (%.2f, %g, %G)
""" % (x, y, z)
print H


G = """
El punto en R3 es:
(x, y, z) = ({laX:.2f}, {laY:g}, {laZ:G})
""" .format(laX=x, laY=y, laZ=z)
print G



import math as m
from math import sqrt 
#from math import *

x=16
x=input("¿Cuál es el valor al que le quieres calcular la raiz?: ")
print "La raíz cuadrada de %.2f es %f" % (x, m.sqrt(x))
print sqrt(16.5)
 
