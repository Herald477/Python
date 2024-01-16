import random
import os

1 == "Rock"
2 == "Paper"
3 == "Scissor"

computer_points = 0

user_points = 0


while True:
    computer_number = random.randint(1, 3)

    user_input = int(input("1=Rock, 2=Paper, 3=Scissor: "))

    input_number = user_input - computer_number


    if user_input == computer_number:
        print("Draw. Try again")

    if input_number == -1 or input_number == -2:
        print("You lost")

        user_points = 0
        computer_points += 1

    if input_number == 1 or input_number == 2:
        print("You won")

        computer_points = 0
        user_points += 1

    if computer_points == 3:
        print("Computer wins!")
        break

    if user_points == 3:
        print("User wins!")
        break