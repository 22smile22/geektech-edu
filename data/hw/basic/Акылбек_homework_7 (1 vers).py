"""
Группа  Geektech 14Py - студент Акылбек Мамбетакунов
Домашнее задание № 7

Написать программу, которая загадывает одно случайное число от 1 до 100, а пользователь старается угадать.

>> Программа должна запрашивать у пользователя целое число, в бесконечном цикле, пока оно не будет отгадано.

>> Исключать ошибки ввода букв и ограничить ввод числа больше 100 и меньше 0,
   подсказывать пользователю корректный ввод для каждого отдельного случая.

>> Если пользователь отгадал число, вывести на экран количество потраченных попыток и секунд затем выйти из программы.
   Программа должна подсказывать знаком “>” или “<”, “очень близко” при радиусе 5 и “близко” при 10.
"""

import random
import time

global user

secret = random.randint(1, 100)

count = 0
stopwatch = time.time()

while 1:
    count += 1
    try:
        print('')
        user = int(input('Программа загадало число от 0 до 100.\n'
                         'Введите целое положительное число:\n'))
    except ValueError:
        print('Вводите только целые числа')

    if user < 0 or user > 100:
        print(f'Вводите только числа от 1 до 100')

    if user == secret:
        print('Вы ввели число: {} \nПрограмма загадало число = {} \n'
              'Вы угадали, ура!\n'.format(user,secret))
        print('Количество неверных попыток: {}'.format(count - 1))
        print('--> Прошло {} секунд.'.format(round(time.time() - stopwatch)))
        break
    elif user == secret - 5 or user == secret + 5:
        print('Очень близко')
    elif user == secret - 10 or user == secret + 10:
        print('Близко')
    elif user < secret:
        print('Ваше число меньше ">"')
    elif user > secret:
        print('Ваше число больше "<"')
    else:
        print("Не угадали")
