'''
6- Definir una función inversa() que calcule la
inversión de una cadena. Por ejemplo la cadena "estoy probando" 
debería devolver la cadena "odnaborp yotse"
'''

def inversa(cadena=""):
    lista = []
    cadena_Inv = ''
    for i in cadena:
        lista.insert(0,i)
    for i in lista:
        cadena_Inv += i
    return cadena_Inv

cadena = input('Ingresa una cadena: ')
print('Inversa: ', inversa(cadena))

