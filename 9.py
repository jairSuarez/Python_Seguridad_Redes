'''
9- Definir una función generar_n_caracteres() 
que tome un entero n y devuelva el caracter 
multiplicado por n. Por ejemplo: 
generar_n_caracteres(5, "x") debería devolver "xxxxx".
'''

def generar_n_caracteres(num=0, character=''):
    return character * num

try:
    caracter = input('Ingresa un caracter: ')
    numero = int(input('# de veces a repetir: '))
    print(generar_n_caracteres(numero,caracter))
except ValueError:
    print('Ingresa un caracter y un numero entero, respectivamente.')
