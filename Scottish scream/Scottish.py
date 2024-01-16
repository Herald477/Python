text_before = input().upper()
text_after = " "

for letter in text_before:   
    if letter == "A" or letter == "I" or letter == "O" or letter == "U" or letter == "Y":
        print("E")

    else:
        print(letter)
    
    text_after += letter