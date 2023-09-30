def main():
    print("1=Addition, 2=Subtraction, 3=Multiplcation, 4=Division")
    method = int(input("What's the counting method? "))
    d = int(input("How many decimals do you want? "))
    x = float(input("Number for X? "))
    y = float(input("Number for Y? "))

    if method > 1:
        if method > 2:
            if method > 3:
                if y > 0:
                    print(round(x / y, d))
                else:
                    print("You can't divide something with 0!")
            else:
                print(round(x * y, d))
        else:
            print(round(x - y, d))
    else:
        print(round(x + y, d))


main()