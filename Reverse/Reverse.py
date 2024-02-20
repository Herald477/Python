import os
result_back = ""
result_for = ""

os.system("cls")
word = input("Word here: ").lower

for backward in reversed(word):
    result_back += backward
    
for forward in word:
    result_for += forward

if result_back == result_for:
    print("This is a Palindrome")

else:
    print("This is NOT a Palindrome")