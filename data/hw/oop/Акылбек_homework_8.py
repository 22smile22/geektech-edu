"""
Группа  Geektech 14Py - студент Акылбек Мамбетакунов
Месяц 2 - ООП. Домашнее задание № 8.

Задание
1. Создать базу данных для записи личных дел
2. Сделать проверку на выполнение , и если он
выполнен то надо его удалить
3. Также нужна произвольная возможность записи
новых личных дел"""

import sqlite3

try:
    dba = sqlite3.connect('server-home.sqlite3')
    sql = dba.cursor()
    print(f"База данных подключена к SQLite\n")

    sql.execute( """CREATE TABLE IF NOT EXISTS things (
      Issue  TEXT,
      Purpose  TEXT,
      Date  TEXT,
      Money  INTEGER,
      Mark   NUMERIC
    )
    """
    )

    def view():
        for data in sql.execute("SELECT * FROM things"):
                    print(data)

    def insert():
        global my_case, my_goal, my_date, my_paid
        while 1:
            select = input('Insert or change rows or exit?\n'
                           'Press i or c or q: ')
            if select.capitalize() == 'I':
                my_case = input('\nInput a case: ')
                my_goal = input('Input a goal: ')
                my_date = input('Enter a date: ')
                my_paid = int(input('Enter a money: '))

                if sql.fetchone() is None:
                    sql.execute(f"INSERT INTO things VALUES (?, ?, ?, ?, ?)",
                                (my_case, my_goal, my_date, my_paid, 'No'))
                    dba.commit()
                    print('Case added')
                    view()
                    delete()
            elif select.capitalize() == 'C':
                view()
                update()
            elif select.capitalize() == 'Q':
                break
            else:
                print('Incorrect input!!! Please try again')
                continue

    def delete():
        sql.execute(f"SELECT * FROM things WHERE Mark = 'Yes'")
        if sql.fetchall():
            sql.execute(f"DELETE FROM things WHERE Mark = 'Yes'")
            print(f'Case deleted\n')
            dba.commit()
            view()
            update()
        else:
            update()

    def update():
        global mark, choice
        while 1:
            mark = input("\nWould you like note a mark 'Yes' - to complete of case?\n"
                         "Press yes/no: ")
            if mark.capitalize() == 'Yes' or mark.capitalize() == 'Y':
                print('List of cases:')
                view()
                while 1:
                    choice = input("\nSelect a case which will be a marked or exit(press exit or q): ")
                    db_select = sql.execute(f"SELECT Issue FROM things WHERE Issue = '{choice}'").fetchone()
                    if db_select is not None:
                        if choice == db_select[0]:
                            sql.execute(f"UPDATE things SET Mark = 'Yes' "
                                        f"WHERE Issue = '{choice}' "
                                        f"AND Mark = 'No'")
                            view()
                            dba.commit()
                        elif choice.capitalize() == 'Exit' or choice.capitalize() == 'Q':
                            break
                        else:
                            print('There is no such case!!')
                            continue
                    elif db_select is None:
                        break
                    else:
                        break

            elif mark.capitalize() == 'No' or mark.capitalize() == 'N':
                close = input('\nWould you like to add new row in notebook?\n'
                              'Press yes/no: ')
                if close.capitalize() == 'No' or close.capitalize() == 'N':
                    print('The notebook is closed\n')
                    break
                elif close.capitalize() == 'Yes' or close.capitalize() == 'Y':
                    insert()
                else:
                    print('Incorrect input!!! Please try again')
                    continue
            else:
                print('Incorrect input!!! Please try again')
                continue

    if __name__ == "__main__":
        insert()

    sql.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (dba):
        dba.close()
        print("Соединение с SQLite закрыто")