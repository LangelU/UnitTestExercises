import math
import pytest

def getlargestNumberOfAList(list = []):
    if not list:
        return None
    largestNumber = list[0]
    for number in list:
        if number > largestNumber:
            largestNumber = number
    return largestNumber

def test_area_of_a_circle():
    assert getlargestNumberOfAList([1,2,3,8,4,5,6]) == 8
    assert getlargestNumberOfAList([-1,-2,-3,-8,-4,-5,-6]) == -1
    assert getlargestNumberOfAList([]) == None

""" 
Crea una función que reciba una lista de números
y devuelva el número mayor. Escribe una prueba unitaria
que verifique que la función devuelve el número mayor correctamente.
Asegúrate de incluir casos con números negativos y listas vacías. 
"""