import os
petals = int(input("Amount of flower petals: "))

for i in range(petals):
    if i % 2 == 0:
        print("Love Me")
    else:
        print("Don't Love Me")