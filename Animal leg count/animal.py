def calculate(cow, pig, chicken):
    cow = cow * 4
    pig = pig * 4
    chicken = chicken * 2
    return cow + pig + chicken

print("How many cows?")
cow = int(input(": "))

print("How many pigs?")
pig = int(input(": "))

print("How many chickens?")
chicken = int(input(": "))

print(f"{calculate(cow, pig, chicken)} legs")