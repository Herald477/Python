def calculate(a, b, c):
    a = a * a
    b = b * b
    c = c * c
    ab = a + b
    if ab == c:
        print("It matches!")
    else:
        print("Doesn't match!")

a = int(input("Enter number for A: "))
b = int(input("Enter number for B: "))
c = int(input("Enter number for C: "))

calculate(a, b, c)