'''
3- Definir una función que calcule 
la longitud de una lista o una cadena dada. 
'''

def long_lista_cadena(lista=[]):
    cont = 0
    for i in lista:
        cont += 1
    return cont

try:
    opcion = int(input('Ingresa cadena (1) o elementos de una lista (2) R=  '))
    if opcion == 1:
        cadena = input('Ingresa una cadena: ')
        print(f'Longitud de la cadena "{cadena}" = {long_lista_cadena(cadena)}')
    elif opcion == 2:
        lista = []
        while True:
            elemento = input('Ingresa elemento, exit=salir. R= ')
            if elemento == "exit":
                print(lista)
                print(f'Longitud de la lista = {long_lista_cadena(lista)}')
                break
            lista.append(elemento)
            elemento = ""
    else:
        print('Opcion no válida. Sólo hay opción 1 y 2.')
except ValueError:
    print("La opcion debe ser un numero entero.")