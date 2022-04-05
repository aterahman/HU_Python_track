import math
class q2c:

    #printing the first triangle as per the question
    
    for i in range(5):
        for j in range(5 - i):
            print('   ', end='')

        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i or i == 5 - 1:
                print(' * ', end='')
            else:
                print('   ', end='')
        print()