#defining a class named StringClass
class StringClass:

    #creating a constructor to take input of string
    def __init__(self,str):
        self.str = str

    #method to find length of string
    def length(self):
        print(len(self.str))

    #method to convert string to list pof characters
    def listchar(self):
        list=[]
        list[:0]=self.str
        print(list)

#initializing an object and calling the constructors and methods
ob= StringClass(input("Please enter the string\n"))
ob.length()
ob.listchar()
