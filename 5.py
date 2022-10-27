'''
Nombre: Jair Alfonso Suárez Flores

5- Escribir una funcion sum() y una función multip() 
que sumen y multipliquen respectivamente todos los números de una lista.
Por ejemplo: sum([1,2,3,4]) debería devolver 10 y 
multip([1,2,3,4]) debería devolver 24
'''

def sum(lista=[]):
    resultado = 0
    for i in lista:
        resultado += i
    return resultado

def multip(lista=[]):
    resultado = 1
    for i in lista:
        resultado *= i
    return resultado 

numeros = []

while True:
    num = input('Ingresa un numero, s=salir. R = ')
    if num.lower() == 's':
        break
    else:
        try:
            num = int(num)
            numeros.append(num)
        except:
            continue
print('Numeros ingresados: ', numeros)
print(f'Suma de todos los números: {sum(numeros)}')
print(f'Multiplicación de todos los números: {multip(numeros)}')


