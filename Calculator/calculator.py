import os

def main():
    print("1=Addition, 2=Subtraction, 3=Multiplcation, 4=Division")
    method = int(input("What's the counting method? "))
    d = int(input("How many decimals do you want? "))
    x = float(input("Number for X? "))
    y = float(input("Number for Y? "))

        

    if method == 1:
        print(round(x + y, d))
        z = round(x + y, d)
    if method == 2:
        print(round(x - y, d))
        z = round(x - y, d)
    if method == 3:
        print(round(x * y, d))
        z = round(x * y, d)
    if method == 4:
        if y > 0:
            print(round(x / y, d))
            z = round(x / y, d)
        else:
            print("You can't divide with 0!")


    print("________________________________________________________________________________________________________________________")

    if method == 1:
        method = -1
    if method == 2:
        method = -2
    if method == 3:
        method = -3
    if method == 4:
        method = -4

    while z>-999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
        print("Wanna add more numbers? 1=Yes - 2=No")
        con = int(input("Type here: y/n "))


        if con == 2:
            os.system("cls")
            break


        else:
            xn = int(input("What number shall you add? "))

            if method == -1:
                z = z+xn
                print(z)
            if method == -2:
                z = z -xn
                print(z)
            if method == -3:
                z = z * xn
                print(z)
            if method == -4:
                z = z / xn
                print(z)




main()