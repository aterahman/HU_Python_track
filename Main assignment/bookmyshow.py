import csv

#class to show display screen
class bookmyshow:

    #displays the welcome screen
    def welcomescreen(self):
        print("******Welcome to BookMyShow*******\n1. Login\n2. Register new account\n3. Exit\n")

    #takes the user input
    def userinput(self):
        self.input = input("Enter: ")
        return self.input


    #scrren that will allow user to to enter username and password
    def loginscreen(self):
        print("\n******Welcome to BookMyShow*******")
        print("**NOTE: For admin login Username: 'admin' && Password: 'password'**")
        self.username=input("Username: ")
        self.password=input(("Password: "))
        return self.username, self.password

    #opens the csv file containing the user login details
    def loginchecker(self, username, password):
        usnverify = False
        pwdverify = False
        with open("C:\\Users\\aterahman\\PycharmProjects\\HU_Python_Track\\Main assignment\\userdetails.csv",
              encoding='utf-8-sig') as csv_file:
                csvreader = csv.DictReader(csv_file, delimiter=',')
                line_count = 0
                for row in csvreader:
                    if (row['Username']==username):
                        usnverify= True

                    if (row['Password']==password):
                        pwdverify=True


        return usnverify,pwdverify


    #method to show admin login screen
    def adminloginscreen(self):
        print("\n******Welcome Admin*******\n1. Add New Movie Info\n2. Edit Movie Info\n3. Delete Movies\n4. Logout")
        self.choice = input("Enter your choice")


    #method to add a new movie
    def addmovie(self):
            print("Enter movie details")
            with open("C:\\Users\\aterahman\\PycharmProjects\\HU_Python_Track\\Main assignment\\movies.csv", 'a',
                  encoding='utf-8-sig') as csv_file:
                    fieldname = ['Title','Genre','Length','Cast','Director','Admin Rating','Language']
                    writer = csv.DictWriter(csv_file, delimiter=',' ,fieldnames=fieldname)

                    writer.writeheader()
                    writer.writerow({'Title':input('Title '),'Genre':input('Genre '),'Length':input('Length '),
                             'Cast':input('Cast '),'Director':input('Director '),'Admin Rating':input('Admin Rating '),
                             'Language':input('Language ')})



    #method to register new user
    def register(self):
        with open("C:\\Users\\aterahman\\PycharmProjects\\HU_Python_Track\\Main assignment\\userdetails.csv",'a',
             newline='', encoding='utf-8-sig') as csv_file:
            fieldname = ['Username','Password']
            writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=fieldname)

            writer.writerow({'Username':input("Enter New Username\n"),
                             'Password':input("Enter New Password\n")})


ob = bookmyshow()
ob.welcomescreen()
choice = ob.userinput()

#goes to the login screen if the choice is 1
if(choice == '1'):

    #stores the entered username for verification
    loginlist = ob.loginscreen()
    username = loginlist[0]
    password = loginlist[1]

    #verifies if the user has logged in as admin
    if(username=='admin' and password=='password'):
        ob.adminloginscreen()
    else:
        while(ob.loginchecker(username,password) != (True, True)):
            print("INVALID LOGIN DETAILS RE-ENTER")
            ob.loginscreen()


elif(choice=='2'):
    ob.register()
    ob.welcomescreen()