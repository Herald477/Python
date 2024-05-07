dictionary = {}

word = input("Word here: ").upper()

for letter in word:
    if letter in dictionary:
        dictionary[letter] += 1
    else:
        dictionary[letter] = 1
    if letter == " ":
        del dictionary[" "]

print(dictionary)