def slotsMachine(chips):
    import random
    num1=0
    startChips = chips
    int(chips)
    print ("Welcome to the fruit machine version 1.0!")
    print ("You have",chips ,",each swing costs 20 chips.")
    fruit = ['Cherry','Bell','Lemon','Orange','Star','Skull']
    while chips>=20:
        if chips==0:
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
            print(symbol1)
            print(symbol2)
            print(symbol3)
        elif ready1 == 'chips':
            chipMod = int(input('h0w much ch1ps ya w0nt ß01?'))
            chips = chipMod
            print('you now have',chips)
            symbol1=random.choice(fruit)
            symbol2=random.choice(fruit)
            symbol3=random.choice(fruit)
            print("You rolled:")
            print(symbol1)
            print(symbol2)
            print(symbol3)
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
            if chips<0:
                chips=0
            
        if ready1=="run":
            print ("You won ",chips,"chips!")
            if chips>startChips:
                print("You have more chips than you started with!")
                quit()
            elif chips==startChips:
                print("You got your chips back!")
                quit()
            else:
                print("You lost some chips!")
                quit()




    print("You can't bet anymore!")
    if chips<=0:
        print("You don't have any chips left!")
    print("Restart to try again!")
            
               
slotsMachine(500)
