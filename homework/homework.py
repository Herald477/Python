import os
def main ():
    os.system("cls")
    print(":homework:")
    homeworks = {}

    while True:
        swe_homework = input("\n\tType in your Swedish Homework: ")
        eng_homework = input("\tType the respective Swedish word in English: ")


        homeworks[swe_homework] = eng_homework

        add = input("\n\tAdd one more? y/n: ")

        if add == "n":
            os.system("cls")
            break
        if add == "y":
            os.system("cls")
            print("\tWhat else?")


    while True:
        print(f"\tAmount of homeworks = {len(homeworks)}")

        for homework in homeworks:
            answer = input(f"\n\t{homework}:")

            if answer == homeworks[homework]:
                print("\tCorrect!")
            else:
                print(f"\tThe correct answer is :{homeworks[homework]}")

        one_more = input("\n\tDo the reherse again? y/n: ")


        if one_more == "n":
            os.system("cls")
            break


main()