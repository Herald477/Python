def main():
    import os

    os.system("cls")
    word = input().upper()


    for letter in word:
        print(letter)
        if letter in word == " ":
            print("___")
        else:
            print(letter)



    
    

main()