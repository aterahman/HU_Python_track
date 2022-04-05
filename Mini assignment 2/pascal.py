import math

#class to print the pascal's triangle
class q2a:

    i=0

    #Inputting number of rows of the pattern
    n = input("Enter N")
    n = int(n)

    #variable that will help in printing the 0s in the pattern
    m = n-1

    #loop that will print the pattern
    for i in range(n):
        print(f"{(int(math.pow(11,i))*(int(math.pow(10,m))))}")
        m=m-1

