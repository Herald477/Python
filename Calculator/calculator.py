import os

def main():
    print("1=Addition, 2=Subtraction, 3=Multiplcation, 4=Division")
    method = int(input("What's the counting method? "))

    d = int(input("How many decimals do you want? "))
    x = float(input("Number for X? "))
    y = float(input("Number for Y? "))

        

    if method == 1:
        z = round(x + y, d)
        print(z)
    if method == 2:
        z = round(x - y, d)
        print(z)
    if method == 3:
        z = round(x * y, d)
        print(z)
    if method == 4:
        if y > 0:
            z = round(x / y, d)
            print(z)
        else:
            print("You can't divide with 0!")


    print("________________________________________________________________________________________________________________________")

    while True:
        print("Want to add more numbers? 1=Yes - 2=No")
        con = int(input("Type here: y/n "))

        if con == 2:
            os.system("cls")
            break


        else:
            xn = int(input("What number shall you add? "))

            if method == 1:
                z = z + xn
                print(z)
            if method == 2:
                z = z - xn
                print(z)
            if method == 3:
                z = z * xn
                print(z)
            if method == 4:
                z = z / xn
                print(z)

            os.system("cls")



main()