"""
Группа  Geektech 14Py - студент Акылбек Мамбетакунов
Месяц 2 - ООП. Домашнее задание № 6.

Задание No Алгоритм

1) Даны два значения ( numbers , desired_sum )
2) Первая это список из чисел
3) Вторая это число которое должно получиться из двух чисел

Смысл :
Нужно сделать так чтобы возвращался индекс двух чисел которые в сумме возвращают желаемую сумму
Например есть список из таких чисел [2, 7, 11, 15] желаемая сумма является число 9,
значит должен возвращаться индекс [0, 1] потому что только сумма этих двух чисел является желаемой
Подсказка : Нужно использовать циклы for
ДОП домашка : Сделать в классах
"""

"""Через процедуру"""

print('\n1) Реализация программы через процедуру\n')
numbers = [2, 7, 11, 15]
desired_sum = int(input('Введите сумму:\n'))

def find():
    for value in range(len(numbers) - 1):
        if (numbers[value] + (numbers[value + 1])) == desired_sum:
            print(f'Индекс чисел: {[value, value + 1]}')

find()
print('-'*50)

"""Через классы"""

class Summary:
    print('2) Реализация программы через классы - ООП\n')
    def __init__(self):
        self.numbers = [2, 7, 11, 15]
        self.desired_sum = int(input('Введите сумму:\n'))

    def Find(self):
        for value in range(len(self.numbers) - 1):
            if (self.numbers[value] + (self.numbers[value + 1])) == self.desired_sum:
                return ([value, value + 1])

print('Индекс чисел: {}'.format(Summary.Find(Summary())))

