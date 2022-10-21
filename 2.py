'''
2- Definir una función max_de_tres(), 
que tome tres números como argumentos y devuelva el mayor de ellos.
'''

def max_de_tres(num1=0, num2=0, num3=0):
    try:
        float(num1)
        float(num2)
        float(num3)
        if num1 > num2 and num1 > num3:
            return f'El número mayor es {num1}'
        elif num2 > num1 and num2 > num3:
            return f'El número mayor es {num2}'
        elif num3 > num1 and num3 > num2:
            return f'El número mayor es {num3}'
        else:
            return 'Todos los valores son iguales.'
    except ValueError:
        return 'Todos los valores deben ser numéricos.'

numero1 = input('Ingresa 1er número: ')
numero2 = input('Ingresa 2do número: ')
numero3 = input('Ingresa 3er número: ')

print(max_de_tres(numero1, numero2, numero3))
