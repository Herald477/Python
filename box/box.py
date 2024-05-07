word = input("Word here: ")

space = int(input("Spaces here: "))

length = len(word)

spaceamount = length + (space*2) + 2
spaceamount = " " * spaceamount

space_ = " " * space
boxfloor = length + (space*2) + 6

boxfloor = "#" * boxfloor

print(boxfloor)
print("#", spaceamount, "#")
print("#", space_, word, space_, "#")
print("#", spaceamount, "#")
print(boxfloor)

