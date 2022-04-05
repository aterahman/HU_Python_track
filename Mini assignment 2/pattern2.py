class q2b:


    for i in range (0, 9,2):
        for j in range (1, 10):
            if (j < (9 - i)):
                    print(" ",end='')
            else:
                    print("*",end='')

        print()


    for i in range(1,10,2):
        for j in range(9,0,-2):
            if (j > (9 - i)):
                print(' ',end='')
            else:
                print("*",end='')
        print()