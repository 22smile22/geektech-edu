"""
Группа  Geektech 14Py - студент Акылбек Мамбетакунов
Домашнее задание №3 - Работа с кортежами

Дан кортеж состоящий из разных типов данных:

data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

Создать два пустых списка letters и numbers
Пройтись циклом for по кортежу data_tuple, добавить все строки в список letters, а всё остальное в numbers.
Из списка numbers удалить число 6.13 и переместить True в конец списка letters, затем вставить число 2 между 3 и 1
Отсортировать numbers, реверсировать letters и изменить пару букв в letters.
Преобразовать списки numbers и letters в кортежи

В итоге:
кортеж letters должен выглядеть так:   (True, 'G', 'e', 'e', 'k', 'T', 'e', 'c', 'h')
кортеж numbers должен выглядеть так:   (1, 2, 3)
"""

data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

for j in data_tuple:
    if type(j) == str or type(j) == bool:
        letters.append(j)
    elif type(j) == int or type(j) == float:
        numbers.append(j)

print("")
print(f"Дан кортеж состоящий из разных типов данных: \n{data_tuple}")
print("")

numbers.remove(6.13)
letters[4], letters[5], letters[6], letters[7], letters[8] = \
letters[5], letters[6], letters[7], letters[8], letters[4]
numbers.insert(1, 2)

numbers.sort()
letters.reverse()
letters[1] = 'G'
letters[-2] = 'c'

numbers = tuple(numbers)
letters = tuple(letters)

print(f"В итоге, мы получаем два кортежа.\n1) Кортеж letters: {letters}\n2) Кортеж numbers: {numbers}")
