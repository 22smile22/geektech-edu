"""
Группа  Geektech 14Py - студент Акылбек Мамбетакунов
Месяц 2 - ООП. Домашнее задание №3. (Задача №1)

Задача #1 Множественное Наследование (Ромбовидный)
1. Создать 4 класса и с помощью их преобразовать РОМБОВИДНЫЙ тип множественного наследования
2. У суперкласса должно быть не меньше 4 атрибутов
3. У каждого класса должно быть не меньше 2 атрибутов
4. Также должны быть соблюдены def __str__(self) + super()
5. К каждому классу создать объект (в итоге будет не меньше 4 объектов)

Задачи 2 и 3 представлены в файлах Акылбек_homework_3_2.py и Акылбек_homework_3_3.py
"""

class Terminator:
    def __init__(self, structure, fuel, weapon, service):
        self.structure = structure
        self.fuel = fuel
        self.weapon = weapon
        self.model = service

    def __str__(self):
        return f'Строение: {self.structure}\n' \
               f'Вид питания: {self.fuel}\n' \
               f'Оружие: {self.weapon}\n' \
               f'Cрок службы: {self.model} лет\n'

class T_1000(Terminator):
    def __init__(self, structure, fuel, weapon, model, liqid, form):
        super().__init__(structure, fuel, weapon, model)
        self.liq = liqid
        self.form = form

    def __str__(self):
        return super(T_1000, self).__str__() + \
               f'Особенность 1: {self.liq}\n' \
               f'Особенность 2: {self.form}\n'

class TX(Terminator):
    def __init__(self, structure, fuel, weapon, model):
        super().__init__(structure, fuel, weapon, model)

    def special(self, prog, emotion):
        self.prog = prog
        self.emot = emotion
        print(f'Особенность 3: {self.prog}\n'
              f'Особенность 4: {self.emot}\n')

    def __str__(self):
        return super(TX, self).__str__() +



class T_3000(T_1000, TX):
    def __init__(self, structure, fuel, weapon, model, liqid, form, nano, magnetic):
        super().__init__(structure, fuel, weapon, model, liqid, form)

        self.nano = nano
        self.magn = magnetic

    def __str__(self):
        return super(T_3000, self).__str__() + \
               f'Особенность 5: {self.nano}\n' \
               f'Особенность 6: {self.magn}\n'

t_800 = Terminator('Металлический эндоскелет','Огнестрельное','Изотопное',120)
t_1000 = T_1000('Жидкокристаллический', 'Резонансный', 'Холодное', 150, 'Жидкий металл', 'Принимает любую форму')
t_x = TX('Жидко-метталический эндоскелет', 'Термоядерный', 'Плазменное', 160)
t_x_spec = TX.special('Программируемые нано-частицы', 'Собственные эмоции')
t_3000 = T_3000('Нанобот', 'Ионный', 'Огнестрельное', 200, False, False, 'Принимает любую внешность', 'Формирует магнитное поле')

print(t_800)
print(t_1000)
print(f'{t_x_spec}')
print(t_3000)