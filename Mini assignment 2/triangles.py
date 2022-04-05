import math
class q2c:

    #printing the first triangle as per the question (scalar triangle)

    for i in range(5):
        for j in range(5 - i):
            print('   ', end='')

        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i or i == 5 - 1:
                print(' * ', end='')
            else:
                print('   ', end='')
        print()

    #printing second pattern as per question (Right angled triangle)

    print("---------------------------------------------------------")
    for a in range(0,5):
        for b in range(0,5):
            if a==0 or b==4 or a==b:
                print(" * ",end='')
            else:
                print("   ",end='')
        print("\n")