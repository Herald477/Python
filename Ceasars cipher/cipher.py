import os

os.system("cls")
alphabet = "abcdefghijlkmnopqrstuvwxyz"

word = input("Word here: ")
steps = int(input("How many steps?: "))

output = ""

for letter in word:
    output = ""
    if letter == " ":
        output += " "
    if letter == ",":
        output += ","
    if output == ".":
        output += "."
    else:
        output += alphabet[alphabet.index(letter) + steps]

print(output)