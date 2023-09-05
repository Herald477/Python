import random
print("\n_________________________________________________\n")
print(".:Gissa Talet:.")
print("gissa ett tal mellan 1 och 10, 3 försök!\n")

slumptal = random.randint(1, 10)
print(slumptal)
i=0
hittat = False

while i<3:
    gissatal = input("Gissa ett tal ")
    if slumptal == int(gissatal):
        hittat = True
        print("Rätt svar!")
        break

    i += 1
if hittat:
        print("Grattis!")

else:
        print("Fel svar loser!")

print("_______________________________________________________")