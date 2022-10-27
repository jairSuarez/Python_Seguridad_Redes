'''
Nombre: Jair Alfonso Suárez Flores

7 - Definir una función es_palindromo() que reconoce 
palíndromos (es decir, palabras que tienen el mismo
aspecto escritas invertidas), ejemplo: 
es_palindromo("radar") tendría que devolver True.
'''

#Se reusa la función "inversa()" para este ejercicio.
def inversa(cadena=""):
    lista = []
    cadena_Inv = ''
    for i in cadena:
        lista.insert(0,i)
    for i in lista:
        cadena_Inv += i
    return cadena_Inv

def es_palindromo(palabra):
    #En la palabra se quitan los espacios y se deja en minúsculas
    palabra = palabra.replace(' ','').lower()
    return palabra == inversa(palabra)

frase = input('Ingresa una frase: ')

print(f'{frase} es palindromo: ', es_palindromo(frase))