
def register():
    with open("storage.txt", "r") as rd:
        with open("password.txt", "r") as pw:
            print("*---Register---*")
            uname = input("Create Username: ")
            passw = input("Input Password: ")
            if (uname not in rd.read()):
                app = open("storage.txt", "a")
                print(uname, file=app)
                app = open("password.txt", "a")
                print(passw, file=app)
                print("\t\tAccount Successfully Registered!")
            else:
                print("\t\tUsername Already exist!")

def login():
    with open("storage.txt", "r") as rd:
        with open("password.txt", "r") as pw:
            print("*---Log In---*")
            uname = input("Username: ")
            passw = input("Password: ")
            username = rd.readlines()
            password = pw.readlines()
            unm = [un.strip() for un in username]
            passwrd = [pas.strip() for pas in password]
            if (uname in unm and passw in passwrd) and (unm.index(uname) == passwrd.index(passw)):
                print("\t\tYou Succesfully Login!")
            else:
                print("\t\t Incorrect Password")

def chens_pas():
    with open("storage.txt", "r") as rd:
        with open("password.txt", "r") as pw:
            print("*---Log In to change password---*")
            uname = input("Username: ")
            passw = input("Password: ")
            username = rd.readlines()
            password = pw.readlines()
            unm = [un.strip() for un in username]
            passwrd = [pas.strip() for pas in password]
            if (uname in unm and passw in passwrd) and (unm.index(uname) == passwrd.index(passw)):
                new_pass = input("New Password: ")            
                app = open("password.txt", "a")
                print(new_pass, file=app)
                print("\t\tPassword Change Successfully!")
            else:
                print("\t\tSyntax Error!")                
while True:
    user = input("Register \t(R) \nLogin \t\t(L) \nChange Paassword (CP)")
    if user == "R":
        register()
    elif user == "L":
        login()
    elif user == "CP":
        chens_pas()
    else:
        print("\t\tInvalid Command")

