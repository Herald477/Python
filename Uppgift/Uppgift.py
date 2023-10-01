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
                    z = round(x / y, d)
                else:
                    print("You can't divide something with 0!")
            else:
                print(round(x * y, d))
                z = round(x * y, d)
        else:
            print(round(x - y, d))
            z = round(x - y, d)
    else:
        print(round(x + y, d))
        z = round(x + y, d)

    print("________________________________________________________________________________________________________________________")

    if method == 1:
        method = -1
    if method == 2:
        method = -2
    if method == 3:
        method = -3
    if method == 4:
        method = -4

    while z>-9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
        print("Wanna add more numbers? 1=Yes - 2=No")
        con = int(input("Type here: "))
        xn = int(input("What number shall you add? "))



        if con == 2:
            break

        else:
            if method == -1:
                print(z)
            if method == -2:
                print(z)
            if method == -3:
                print(z)
            if method == -4:
                print(z)


            print("________________________________________________________________________________________________________________________")






main()