import math
class filterposneg:

        #given list
        lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]

        def fun(var):
                return abs(var)


        neg = list(map(fun, (filter(lambda x: x<0, lst1))))

        print(neg)


