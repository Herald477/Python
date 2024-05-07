f = open("text.txt", "r")
lines = f.readlines()

remove = input("Who do you want to remove?: ")

for line in lines:
    print(line)