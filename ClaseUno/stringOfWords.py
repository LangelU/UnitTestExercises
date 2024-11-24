import math
import pytest

def getOrderedList(string = ""):
    orderedList = ""
    arrayOfWords = string.split()

    if len(arrayOfWords) == 0:
        return None
    
    orderedArray = sorted(arrayOfWords)

    for i, word in enumerate(orderedArray):
        if i == 0:
            orderedList = orderedList + word
        else:
            orderedList = orderedList + " " + word

    return orderedList

def test_area_of_a_circle():
    assert getOrderedList("uno dos tres cuatro") == "cuatro dos tres uno"
    assert getOrderedList("uno dos dos uno tres cuatro") == "cuatro dos dos tres uno uno"
    assert getOrderedList("") == None

""" 
Escribe una función que reciba una cadena de texto
y devuelva la misma cadena pero con las palabras
ordenadas alfabéticamente. Luego, escribe pruebas unitarias
que cubran los siguientes casos:
- Una cadena con palabras en orden aleatorio.
- Una cadena con palabras repetidas.
- Una cadena vacía. 
"""
