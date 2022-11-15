def slotMachine(chips,name,chips1):
    import random
    import time as t
    num1=0
    chips = int(chips)
    startChips = int(chips)
    print ("Hello, "+name+".")
    print ("Welcome to the fruit machine version 1.0!")
    print ("You have",chips ,",each swing costs 20 chips.")
    fruit = ['Cherry','Bell','Lemon','Orange','Star','Skull']
    while chips >= 20:
        if chips == 0:
            break
        ready1=input("Would you like to roll or run?\n")
        if ready1=="roll":
            num1=0
            chips=chips-20
            print("You now have ",chips,"chips")
            symbol1=random.choice(fruit)
            symbol2=random.choice(fruit)
            symbol3=random.choice(fruit)
            print("You rolled:")
            t.sleep(0.666666666)
            print(symbol1)
            t.sleep(0.333333333)
            print(symbol2)
            t.sleep(0.333333333)
            print(symbol3)
            t.sleep(1)
            if symbol1=="Skull" and symbol2=="Skull" and symbol3=="Skull":
                print("You got three skulls so you lost all your chips!")
                break
            if symbol1=="Skull":
                if symbol2=="Skull" or symbol3=="Skull":
                    print("You got two skulls so you lost 100 chips!")
                    chips=chips-100
                    print("You now have ", chips,"chips")
                    num1=1
            elif symbol2=="Skull":
                if symbol1=="Skull" or symbol3=="Skull":
                    print("You got two skulls so you lost 100!")
                    chips=chips-100
                    print("You now have ", chips,"chips")
                    num1=1
            elif symbol3=="Skull":
                if symbol2=="Skull" or symbol1=="Skull":
                    print("You got two skulls so you lost 100!")
                    chips=chips-100
                    print("You now have ", chips,"chips")
                    num1=1
            if symbol1=="Bell" and symbol2=="Bell" and symbol3=="Bell":
                print("You got 3 bells so you win 500")
                chips=chips+500
                print("You now have ", chips,"chips")
                num1=1
            if num1!=1:
                if symbol1==symbol2:
                    print("You won 50 chips!")
                    chips=chips+50
                    print("You now have ", chips,"chips")
                if symbol1==symbol3:
                    print("You won 50 chips!")
                    chips=chips+50
                    print("You now have ", chips,"chips")
                if symbol2==symbol3:
                    print("You won 50 chips!")
                    chips=chips+50
                    print("You now have ", chips,"chips")
                    
        if ready1=="run":
            print ("You won ",chips,"chips!")
            if chips>startChips:
                print("You have more chips than you started with!")
                chips1 = chips1 + chips
                with open("Chips1.txt",mode="w") as f:
                    f.write(str(chips1))
                t.sleep(5)
                break
            elif chips==startChips:
                print("You got your chips back!")
                chips1 = chips1 + chips
                with open("Chips1.txt",mode="w") as f:
                    f.write(str(chips1))
                t.sleep(5)
                break
            else:
                print("You lost some chips!")
                chips1 = chips1 + chips
                with open("Chips1.txt",mode="w") as f:
                    f.write(str(chips1))
                t.sleep(5)
                break
                



    if chips != 0:
        print("You can't bet anymore!")
        if chips<=0:
            print("You don't have any chips left!")
        chips1 = chips1 + chips
        with open("Chips1.txt",mode="w") as f:
            f.write(str(chips1))
        print("Restart to try again!")
