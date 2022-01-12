"""
Группа  Geektech 14Py - студент Акылбек Мамбетакунов
Месяц 2 - ООП. Домашнее задание №3. (Задача №3)

Задача #3 Магические методы
1. Создать 2 класса с магическими методами
2. 1-ый класс это класс Кинотеатр, в котором будут фильмы и нужно использовать как минимум 2 магических метода
для выведения фильма
3. Должен быть выбор фильмов и цена у каждого разный
4. 2-ой класс это класс Старбакс в котором пишут имена на кофе
5. Если имя больше или равно 9 символов, пишут только 5 символов имени
6. Если имя меньше 9 символов, пишут все символы имени
7. Если имя меньше 5, пишут последние три символа имени
8. Использовать именно магические методы

Задачи 1 и 2 представлены в файлах Акылбек_homework_3_1.py и Акылбек_homework_3_2.py
"""

#Задача 1

class Cinema:

    def __init__(self, film1, film2, film3, cost1, cost2, cost3):
        self.f1 = film1
        self.f2 = film2
        self.f3 = film3
        self.c1 = cost1
        self.c2 = cost2
        self.c3 = cost3

    def choose(self,film):
        if film == self.f1:
            return f'Выбран фильм №1, ниже детали:\n' \
                   f'Название - {self.f1}, цена - {self.c1} сом\n'
        elif film == self.f2:
            return f'Выбран фильм №2, ниже детали:\n' \
                   f'Название - {self.f2}, цена - {self.c2} сом\n'
        elif film == self.f3:
            return f'Выбран фильм №3, ниже детали:\n' \
                   f'Название - {self.f3}, цена - {self.c3} сом\n'
        else:
            pass


    def __str__(self):
        return f'Афиша:\n1) {self.f1}\n2) {self.f2}\n3) {self.f3}\n'

review = Cinema('Spider-Man','Unstoppable','Avatar', 250, 350, 550)

print(f'{review}\n{review.choose("Spider-Man")}')
print(f'{review}\n{review.choose("Unstoppable")}')
print(f'{review}\n{review.choose("Avatar")}')

print(f"{'-+-'*45}\n")

#2 задача
class Starbucks:
    def __init__(self, *visitors):
        self.name = []
        for i in visitors:
            self.name.append(i)

    def __add__(self, f_name):
        self.name.append(f_name)
        return self

    def __sub__(self, other):
        self.name.append(other)
        return self

    def __len__(self):
        return len(self.name)

    def short(self):
        for name in self.name:
            if (len(name) < 5):
                print(f'Посетитель: {name} \nИмя на кофе: {name[-3:]}\n')
            elif (len(name) >= 9):
                print(f'Посетитель: {name} \nИмя на кофе: {name[:-4]}\n')
            else:
                print(f'Посетитель: {name} \nИмя на кофе: {name}\n')


cofee = Starbucks("Гулбарчын", "Леон", "Акылбек", "Нурсултан")
cofee.short()

