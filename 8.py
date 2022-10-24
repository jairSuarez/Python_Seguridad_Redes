'''
8- Definir una función superposicion() que tome dos listas 
y devuelva True si tienen al menos 1 miembro en común o 
devuelva False de lo contrario. 
Escribir la función usando el bucle for anidado. 
'''

def superposicion(lista1=[],lista2=[]):
    coincidencias = 0
    for i in lista1:
        for j in lista2:
            if i == j:
                coincidencias += 1
    return coincidencias > 0

lista1 = []
lista2 = []

while True:
    miembro1 = input('Ingresa un elemento para la lista 1, exit=salir. R= ')
    if miembro1.lower() == 'exit':
        print('lista 1 completa. Pasando a lista 2...\n')
        break
    else:
        lista1.append(miembro1)
        
while True:
    miembro2 = input('Ingresa un elemento para la lista 2, exit=salir. R= ')
    if miembro2.lower() == 'exit':
        break
    else:
        lista2.append(miembro2)

print('\nExisten miebros en comun en lista 1 y 2: ', superposicion(lista1,lista2))

