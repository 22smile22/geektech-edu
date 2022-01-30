""" 2 Month - OOP - Jan 22 - 27.01.2022
"""

import sqlite3
from random import randint

database_1 = sqlite3.connect('server.sqlite3')
sql = database_1.cursor()


sql.execute(
    """CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    cash INT
    )
    """
)
database_1.commit()

def register_user():
    global user_login, user_password, balance
    user_login = input('Login: ')
    user_password = input('Password: ')
    number = randint(1, 2)

    for i in sql.execute(f"SELECT cash FROM users WHERE login = '{user_login}'"):
        balance = i[0]


    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
    # sql.execute(f"INSERT INTO users WHERE login ='{user_login}'")
        sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_login, user_password, 0))
        database_1.commit()
        print('User registered')
        # for value in sql.execute("SELECT login FROM users"):
        for value in sql.execute("SELECT * FROM users"):
            print(value)
    else:
        if number == 1:
            sql.execute(f"UPDATE users SET cash = {100 + balance} WHERE login = '{user_login}'")
            print('You won money')
            database_1.commit()
            for value in sql.execute("SELECT * FROM users"):
                print(value)
        else:
            sql.execute(f"DELETE FROM users WHERE login = '{user_login}'")
            database_1.commit()
            print('You lose\nYou wiped from our database, it is just business')
            for value in sql.execute("SELECT * FROM users"):
                print(value)

if __name__ == "__main__":
    register_user()

