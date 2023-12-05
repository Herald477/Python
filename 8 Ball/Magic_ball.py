import random
import os

yes_list = ["yes", "of course", "absolutely"]
no_list = ["no", "never", "absolutely not"]
maybe_list = ["maybe", "im not sure", "the odds are even", "you can try"]

list_select = random.randint(0,2)




os.system("cls")
print("What is your question?")
input(": ")
print(random.choice(yes_list + no_list + maybe_list))