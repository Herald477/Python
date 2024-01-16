import os
os.system("cls")

Player1 = True

Number = 0

#player 1
while Number <= 21:
    while Player1 == True:
        print("Player 1")
        Player1_number = int(input(": "))

        if Player1_number >= 4:
            os.system("cls")
            print("Try again")
        if Player1_number <= 0:
            os.system("cls")
            print("Try again")

        if Player1_number == 1 or Player1_number == 2 or Player1_number == 3:
            Number += Player1_number
            os.system("cls")
            print(Number)
            Player1 = False
            
    if Number == 21:
        if Player1 == False:
            print("Player 1 Wins!")
            break
        if Player1 == True:
            print("Player 2 wins!")
            break
    if Number > 21:
        print("You Fail!")
        break
    
    #player 2
    while Player1 == False:
        print("Player 2")
        Player2_number = int(input(": "))

        if Player2_number >= 4:
            os.system("cls")
            print("Try again")
        if Player2_number <= 0:
            os.system("cls")
            print("Try again")
        
        if Player2_number == 1 or Player2_number == 2 or Player2_number == 3:
            Number += Player2_number
            os.system("cls")
            print(Number)
            Player1 = True
    
    if Number == 21:
        if Player1 == False:
            print("Player 1 Wins!")
            break
        if Player1 == True:
            print("Player 2 wins!")
            break
    if Number > 21:
        print("You Fail!")
        break