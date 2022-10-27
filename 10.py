'''
Nombre: Jair Alfonso Suárez Flores

A B C y D  son cifras de un solo dígito.
Todas ellas forman parte de las siguientes ecuaciones:
A + C = D
A x B = C
C - B = B
A x 4 = D
Encuentra los valores de A B C y D.
Indica la solución como una cifra de cuatro dígitos.
'''


for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                if a+c==d and a*b==c and c-b==b and a*4==d:
                    print('A B C D = ',a,b,c,d)
                    break

                    
                    