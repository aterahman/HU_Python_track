import math
class q2c:

    for i in range(1,6):
        for j in range(1,10):
            if(i==1):
                if(j==5):
                    print(" * ",end='')
                else:
                    print("   ",end='')

            else:
                if(j==(5- int(math.pow(2,i-2)))):
                    print(" * ",end='')

                elif(j== (5+ (math.pow(2,i-2)))):
                        print(" * ",end='')

                else:
                    print("   ",end='')

        print()
