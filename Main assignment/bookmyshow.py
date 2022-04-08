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
        self.adminchoice = input("Enter your choice: ")
        return self.adminchoice


    #method to add a new movie
    def addmovie(self):
            print("Enter movie details")
            with open("C:\\Users\\aterahman\\PycharmProjects\\HU_Python_Track\\Main assignment\\movies.csv", 'a',
                  encoding='utf-8-sig') as csv_file:
                    fieldname = ['Title','Genre','Length','Cast','Director','Admin Rating','Language']
                    writer = csv.writer(csv_file, delimiter=',')


                    writer.writerow([input('Title '),input('Genre '),input('Length '),
                             input('Cast '),input('Director '),input('Admin Rating '),
                             input('Language ')])

            # method to add a new movie

    def editmovie(self):
        print("What movie do you want to edit?")
        with open("C:\\Users\\aterahman\\PycharmProjects\\HU_Python_Track\\Main assignment\\movies.csv", 'r',
                  encoding='utf-8-sig') as csv_file:
            fieldname = ['Title', 'Genre', 'Length', 'Cast', 'Director', 'Admin Rating', 'Language']
            editor = csv.reader(csv_file, delimiter=',')
            for row in editor:
                print(row)


    #method to delete a movie
    def deletemovie(self):
        with open("C:\\Users\\aterahman\\PycharmProjects\\HU_Python_Track\\Main assignment\\movies.csv", 'a',
                  encoding='utf-8-sig') as csv_file:
            deleter = csv.reader(csv_file, delimiter=',')



    #method to register new user
    def register(self):
        with open("C:\\Users\\aterahman\\PycharmProjects\\HU_Python_Track\\Main assignment\\userdetails.csv",'a',
             newline='', encoding='utf-8-sig') as csv_file:
            fieldname = ['Username','Password']
            writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=fieldname)

            writer.writerow({'Username':input("Enter New Username\n"),
                             'Password':input("Enter New Password\n")})


    #method to login as customer
    def userlogin(self):
        print("\n******Welcome User*******\n1. Book Tickets\n2. Cancel Tickets\n3. Give User Rating\n4. Logout")
        self.userchoice = input("Enter choice: ")


    #method to book tickets
    def booktickets(self):
        with open("C:\\Users\\aterahman\\PycharmProjects\\HU_Python_Track\\Main assignment\\movies.csv", 'r',
                  encoding='utf-8-sig') as csv_file:
            view = csv.reader(csv_file, delimiter = ',')

            for row in view:
                print(row)


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

        adminchoice = ob.adminloginscreen()
        while (adminchoice != '4'):
            if(adminchoice=='1'):
                ob.addmovie()
            elif(adminchoice=='2'):
                ob.editmovie()
            elif(adminchoice=='3'):
                ob.deletemovie()
            elif(adminchoice=='4'):
                ob.welcomescreen()
            adminchoice = ob.adminloginscreen()


    else:
        while(ob.loginchecker(username,password) != (True, True)):
            print("INVALID LOGIN DETAILS RE-ENTER")
            ob.loginscreen()



elif(choice=='2'):
    ob.register()
    ob.welcomescreen()

elif(choice=='3'):
    SystemExit