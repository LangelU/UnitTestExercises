import math
import pytest

def getAreaOfACircle(radius):
    pi = math.pi
    res = pi * (radius ** 2)
    return res

def test_area_of_a_circle():
    assert getAreaOfACircle(5) == 78.53981633974483
    assert getAreaOfACircle(10) == 314.1592653589793

""" 
Escribe una prueba unitaria para una función
que calcule el área de un círculo dado su radio.
La fórmula es: área = pi * radio^2. 
"""
