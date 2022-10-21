'''
3- Definir una función que calcule 
la longitud de una lista o una cadena dada. 
'''
from random import randint

def long_lista_cadena(lista=[]):
    cont = 0
    for i in lista:
        cont += 1
    return cont

lista = ['a',1,2,'b','c',3,2,3,4,5,6,6,23,'w']

print(f'Longitud de la lista/cadena = {long_lista_cadena(lista)}')
