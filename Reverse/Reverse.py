import os
result_back = ""

os.system("cls")
print("Atleast 2 letters!")
word = input("Word here: ").lower()

if len(word) >= 2:
    
    for backward in reversed(word):
        result_back += backward

    if result_back == word:
        print("This is a Palindrome")

    else:
        print("This is NOT a Palindrome")
else:
    print("Input 2 or more letters!")