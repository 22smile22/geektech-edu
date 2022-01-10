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

from random import randint
from time import time
global user

secret = randint(1, 100)
count = 0
stopwatch = time()

range_5 = []
range_10 = []
range_100 = []

for i in range(1,6):
    s5_plus = secret + i
    range_5.append(s5_plus)
    s5_minus = secret - i
    range_5.append(s5_minus)

for j in range(6,11):
    s10_plus = secret + j
    range_10.append(s10_plus)
    s10_minus = secret - j
    range_10.append(s10_minus)

for k in range(0,100):
    k += 1
    range_100.append(k)

while 1:
    count += 1
    try:
        print('')
        user = int(input('Программа загадало число от {} до {}.\n'
                         'Ваше число: '.format(range_100[0],len(range_100))))
        if user in range_100:
            if user == secret:
                print('\nВы ввели число: {} \n'
                        'Программа загадало число = {} \n'
                        'Вы угадали, ура!\n'.format(user,secret))
                print('>>> Неверные попытки: {}'.format(count - 1))
                print('--> Прошло {} секунд.'.format(round(time() - stopwatch)))
                break
            elif user in range_5:
                print('Очень близко')
            elif user in range_10:
                print('Близко')
            elif user < secret:
                print('Ваше число меньше "<"')
            elif user > secret:
                print('Ваше число больше ">"')
            else:
                print('Не угадали')
        else:
            print('Ошибка!!! -- Вводите только числа от {} до {}'
                  .format(range_100[0],len(range_100)))
    except ValueError:
        print('Ошибка!!! -- Вводите только целые числа')