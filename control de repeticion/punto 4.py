from typing import List

lista = [6, 11, 16, 21]
def sumar(lista):
    if lista == []:
       suma = 0
    else:
        suma = lista[0] + sumar(lista[1:])
    return suma 
print(sumar(lista))
