import os
import sqlite3
from sqlite3 import Error


def main():
    while True:
        add_car_to_table()
        list_car_table()

        answer = input("\nAdd car?\n: ")
        if (answer != "J"):
            break

def add_car_to_table():
    os.system('cls' if os.name == 'nt' else 'clear')
    carbrand = input("Add car brand: ")
    carmodel = input("Add car model: ")

    sqliteConnection = sqlite3.connect("database.db")
    cursor = sqliteConnection.cursor()
    sqlite_insert_query = f"""insert into Cars
                            (brand, model)
                            VALUES
                            ('{carbrand}', '{carmodel}')"""
    

    cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("\nAdded car to DB\n")
    cursor.close()
    sqliteConnection.close()



def list_car_table():
    sqliteConnection = sqlite3.connect("database.db")
    cursor = sqliteConnection.cursor()

    sqlite_select_query = """SELECT * from cars ORDER by brand"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()

    for row in records:
        print(f"\tID: {row[0]}, \tBRAND: {row[1]}, \tMODEL: {row[2]}")
    
    cursor.close()
    sqliteConnection.close()

    print("The connection is closed")


main()