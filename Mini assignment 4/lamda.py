import math


class lamda:

    #lambda expression to find roots of the eqn
    eqn = lambda a, b, c : print(f"Roots of the equation are {(((-b)+math.sqrt((b*b)-(4*a*c)))/(2*a))} and "
                                 f"{(((-b)-math.sqrt((b*b)-(4*a*c)))/(2*a))} ")

    a= int(input("Enter a"))
    b= int(input("Enter b"))
    c= int(input("Enter c"))

    print(f" Equation is : {a}x^2 + {b}x + {c} = 0")
    eqn(a,b,c)