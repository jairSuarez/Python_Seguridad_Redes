'''
Nombre: Jair Alfonso Suárez Flores

1- Definir una función max() que tome como 
argumento dos números y devuelva el mayor de ellos. 
'''
def max(num1=0, num2=0):
    try:
        float(num1)
        float(num2)
        if num1 > num2:
            return f'El número mayor es: {num1}'
        elif num2 > num1:
            return f'El número mayor es: {num2}'
        else:
            return f'El número {num1} y {num2} son iguales.'
    except ValueError:
        return 'Sólo se admiten números.'

numero1 = input('Ingresa un número: ')
numero2 = input('Ingresa otro número: ')

print(max(numero1, numero2))


        

