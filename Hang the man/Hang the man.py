import os

os.system("cls")
word = input(": ").upper()
letter_hidden = word

for letter_hidden in word:
    if letter_hidden == "E" or letter_hidden == "O" or letter_hidden == "L" or letter_hidden == "H":
        print("X")

    else:
        print(letter_hidden)
    
while True:    
    letter_guess = input("Guess a letter: ").upper

    if letter_guess == letter_hidden:
        print(letter_hidden)
