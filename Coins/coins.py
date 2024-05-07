money = [100, 50, 30, 5]
product = True

def count_money(money_list : list, cost : True):
    cost = 250
    balance = 0
    balance += money_list[0] * 1
    balance += money_list[1] * 2
    balance += money_list[2] * 5
    balance += money_list[3] * 10

    price = balance - cost
    if price >= 0:
        cost = True
        print("True")
    else:
        cost = False
        print("False")

    return balance, price

print(count_money(money, product))