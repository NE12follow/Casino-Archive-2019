from slotMachine import *
import time as t
print("Welcome to the casino!")
with open("Username1.txt",mode="r") as f:
    username1 = f.read()
with open("Password1.txt",mode="r") as f:
    password1 = f.read()
with open("Name1.txt",mode="r") as f:
    name1 = f.read()
with open("Chips1.txt",mode="r") as f:
    chips1 = f.read()
    int(chips1)
with open("Username2.txt",mode="r") as f:
    username2 = f.read()
with open("Password2.txt",mode="r") as f:
    password2 = f.read()
with open("Name2.txt",mode="r") as f:
    name2 = f.read()
with open("Chips2.txt",mode="r") as f:
    chips2 = f.read()
    int(chips2)
loggedIn = False
while loggedIn == False:
    passwordMaker=input("Type 1 to make a new login or 2 if you already have a login.\n")
    passwordMaker=int(passwordMaker)
    if passwordMaker == 1:
        if username1 != "":
            name2=input("What is your name?\n")
            with open("Name2.txt",mode="w") as f:
                f.write(name2)
            print("Hello ",name2+"!")
            username2=input("Please enter your new username:  ")
            with open("Username2.txt",mode="w") as f:
                f.write(username2)
            password2=input("Please enter your new password:  ")
            with open("Password2.txt",mode="w") as f:
                f.write(password2)
            with open("Chips2.txt",mode="w") as f:
                f.write("500")
        if username1 == "":
            name1=input("What is your name?\n")
            with open("Name1.txt",mode="w") as f:
                f.write(name1)
            print("Hello ",name1+"!")
            username1=input("Please enter your new username:  ")
            with open("Username1.txt",mode="w") as f:
                f.write(username1)
            password1=input("Please enter your new password:  ")
            with open("Password1.txt",mode="w") as f:
                f.write(password1)
            with open("Chips1.txt",mode="w") as f:
                f.write("500")
    if passwordMaker == 2:
        while True:
            usernameChecker1=input("Please enter your username:  ")
            passwordChecker1=input("Please enter your password:  ")
            if usernameChecker1 == username1:
                if passwordChecker1 == password1:
                    print("Welcome",name1,".")
                    user = 1
                    loggedIn = True
                    break
                else:
                    print("Password is incorrect.")
                    print("You have 3 attempts left for ",username1,".")
                    passwordChecker1=input("Please enter your password:  ")
                    if passwordChecker1 == password1:
                        print("Welcome",name1,".")
                        user = 1
                        loggedIn = True
                        break
                    else:
                        print("Password is incorrect.")
                        print("You have 2 attempts left for ",username1,".")
                        passwordChecker1=input("Please enter your password:  ")
                        if passwordChecker1 == password1:
                            print("Welcome",name1,".")
                            user = 1
                            loggedIn = True
                            break
                        else:
                            print("Password is incorrect.")
                            print("You have 1 attempts left for ",username1,".")
                            passwordChecker1=input("Please enter your password:  ")
                            if passwordChecker1 == password1:
                                print("Welcome",name1,".")
                                user = 1
                                loggedIn = True
                                break
                            else:
                                print("Password is incorrect.")
                                print("You have 0 attempts left for ",username1,".")
                                print("You have been locked out of",username1,".")
                                with open("Username1.txt",mode="w") as f:
                                    f.write("")
                                with open("Password1.txt",mode="w") as f:
                                    f.write("")
                                with open("Name1.txt",mode="w") as f:
                                    f.write("")
                                with open("Chips1.txt",mode="w") as f:
                                    f.write("")
                                break
            if usernameChecker1 == username2:
                if passwordChecker1 == password2:
                    with open("Name2.txt",mode="r") as f:
                        name2 = f.read()
                    print("Welcome",name2,".")
                    user = 2
                    loggedIn = True
                    break
                else:
                    print("Password is incorrect.")
                    print("You have 3 attempts left for ",username2,".")
                    passwordChecker1=input("Please enter your password:  ")
                    if passwordChecker1 == password1:
                        print("Welcome",name2,".")
                        user = 2
                        loggedIn = True
                        break
                    else:
                        print("Password is incorrect.")
                        print("You have 2 attempts left for ",username2,".")
                        passwordChecker1=input("Please enter your password:  ")
                        if passwordChecker1 == password1:
                            print("Welcome",name2,".")
                            user = 2
                            loggedIn = True
                            break
                        else:
                            print("Password is incorrect.")
                            print("You have 1 attempts left for ",username2,".")
                            passwordChecker1=input("Please enter your password:  ")
                            if passwordChecker1 == password2:
                                print("Welcome",name2,".")
                                user = 2
                                loggedIn = True
                                break
                            else:
                                print("Password is incorrect.")
                                print("You have 0 attempts left for ",username2,".")
                                print("You have been locked out of",username2,".")
                                with open("Username2.txt",mode="w") as f:
                                    f.write("")
                                with open("Password2.txt",mode="w") as f:
                                    f.write("")
                                with open("Name2.txt",mode="w") as f:
                                    f.write("")
                                with open("Chips2.txt",mode="w") as f:
                                    f.write("")
                                break
            if usernameChecker1 != username2:
                if usernameChecker1 != username2:
                    print("Username is invalid or nonexistant")

if user == 1:
    while True:
        print("1. Blackjack")
        print("2. Slot machine")
        print("3. COMMING SOON")
        t.sleep(1)
        game = input("Which game do you want to play?\n")
        print("You have "+str(chips1)+" chips to play with.")
        chipSubtotal = int(input("How many are you going to take with you?\n"+"PS bring a multipul of 20\n"))
        chips1 = int(chips1)
        chips1 = chips1-chipSubtotal
        if game == "1":
            print(name1)
        if game == "2":
            t.sleep(0.5)
            print("Loading slot machine...")
            t.sleep(1)
            slotMachine(chipSubtotal,name1,chips1)
            print("Welcome back "+name1+"!")
