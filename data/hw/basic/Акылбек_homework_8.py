"""
Группа  Geektech 14Py - студент Акылбек Мамбетакунов
Домашнее задание № 8

Создать программу “Таблица умножения”.

Программа должна запрашивать у пользователя имя и количество попыток.
Затем работать в бесконечном цикле до истечения указанных попыток.

Программа должна запрашивать произведение двух случайных чисел от 1 до 9.
После ввода пользователем ответа, выводить на экран правильный ответ.

Каждый вопрос-ответ записывать в файл results.txt

В этот же файл дописать итоговый отчёт с указанием имени, количества попыток и затраченного времени.
"""

import random
import datetime

user_count = int(input('Сколько попыток? '))
name = input("Введите имя: ")
count = 0
stopwatch = datetime.datetime.now()

while 1:
    while user_count > 0:
        user_count -= 1
        count += 1
        num1, num2 = random.randint(1,9), random.randint(1,9)
        user = int(input(f"{num1} * {num2} = ? "))
        mult = num1 * num2

        if user == mult:
            print(f"Правильный ответ: {mult}")
            with open('result.txt', 'a', encoding='UTF-8') as file:
                file.write(f"{num1} * {num2} = {user} ({mult}) Правильно\n")
        elif user != mult:
            print(f"Правильный ответ: {mult}")
            with open('result.txt', 'a', encoding='UTF-8') as file:
                file.write(f"{num1} * {num2} = {user} ({mult}) Неправильно\n")
        else:
            pass


    if count == 1 or count == 21:
        with open('result.txt', 'a', encoding='UTF-8') as file:
            file.write(f"Была {count} попытка, потраченное время: "
                       f"{datetime.datetime.now() - stopwatch}, имя: {name}\n")
    elif count >= 11 and count <= 20:
        with open('result.txt', 'a', encoding='UTF-8') as file:
            file.write(f"Было {count} попыток, потраченное время: "
                       f"{datetime.datetime.now() - stopwatch}, имя: {name}\n")
    else:
        with open('result.txt', 'a', encoding='UTF-8') as file:
            file.write(f"Было {count} попытки, потраченное время: "
                       f"{datetime.datetime.now() - stopwatch}, имя: {name}\n")

    with open('result.txt', 'a', encoding='UTF-8') as file:
            file.write(f"\n")
    break