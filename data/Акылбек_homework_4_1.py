"""
Группа  Geektech 14Py - студент Акылбек Мамбетакунов
Месяц 2 - ООП. Домашнее задание №4. (Задача №1)

1. Создать класс TimeDesk, в котором будет один атрибут seconds
2. Надо в методе придумать логику конвертера секунд на дни, часы, минуты и секунды
3. Если дано 70 секунд, то вывод должен составить 0 дней, 0 часов, 1 минута и 10 секунд
4. Если дано 86401 секунда, то вывод должен составить 1 день, 0 часов, 0 минут и 1 секунд
5. Нельзя использовать вспомогательные (встроенные) модули
"""

class TimeDesk:
    def __init__(self, seconds):
        self.second = seconds

    def time(self):
        sec = self.second % 60
        mint = self.second // 60
        mint %= 60
        hour = self.second // 60
        hour %= 24
        day = self.second // 86400
        return f'{day} день, {hour} часов, {mint} минут, {sec} секунд'

sec1 = TimeDesk(70).time()
sec2 = TimeDesk(86401).time()

print('{}\n{}'.format(sec1, sec2))

