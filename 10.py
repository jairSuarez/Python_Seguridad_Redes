


for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                if a+c==d and a*b==c and c-b==b and a*4==d:
                    print('A B C D = ',a,b,c,d)
                    break

                    
                    