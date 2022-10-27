'''
Nombre: Jair Alfonso Suárez Flores

4- Escribir una función que tome un 
carácter y devuelva True si es una vocal, 
de lo contrario devuelve False.
'''

def esVocal(caracter = ""):
    caracter = caracter.lower()
    vocales = ['a','e','i','o','u']
    if caracter in vocales:
        return True
    return False

caracter = input('Ingresa un carcater: ')

if esVocal(caracter):
    print(f'"{caracter}" es una vocal.')
else:
    print(f'"{caracter}" no es una vocal.')
