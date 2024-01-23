while True:
    number_input = input("Enter a number: ").split()
    print(number_input)
    for i in range(len(number_input)):
        print(number_input[i] + number_input[i-1] + number_input[i+1])