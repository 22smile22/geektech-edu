"""
Группа  Geektech 14Py - студент Акылбек Мамбетакунов
Месяц 2 - ООП. Домашнее задание №3. (Задача №1)

Задача #1 Множественное Наследование (Ромбовидный)
1. Создать 4 класса и с помощью их преобразовать РОМБОВИДНЫЙ тип множественного наследования
2. У суперкласса должно быть не меньше 4 атрибутов
3. У каждого класса должно быть не меньше 2 методов
4. Также должны быть соблюдены def __str__(self) + super()
5. К каждому классу создать объект (в итоге будет не меньше 4 объектов)

Задачи 2 и 3 представлены в файлах Акылбек_homework_3_2.py и Акылбек_homework_3_3.py
"""

class Terminator:
    def __init__(self, model, structure, fuel, weapon, service):
        self.model = model
        self.structure = structure
        self.fuel = fuel
        self.weapon = weapon
        self.service = service

    def __str__(self):
        return f'Модель: {self.model}\n'\
               f'Строение: {self.structure}\n' \
               f'Вид питания: {self.fuel}\n' \
               f'Оружие: {self.weapon}\n' \
               f'Cрок службы: {self.service} лет\n'

class T_1000(Terminator):

        def liquid(self, liquid):
            if liquid == self.weapon:
                return """Особенность Т-1000: Состоит из жидкого металла\n"""

        def form (self, form):
            if form == self.structure:
                return """Преимущество Т-1000: Может принимать любую форму"""

        def __str__(self):
            return super(T_1000, self).__str__()


class TX(Terminator):

    def prog(self, prog):
        if prog == self.weapon:
            return f'Особенность Т-Х: Может программировать любую технику нано-частицами\n'

    def emotion(self, emotion):

        if emotion == self.structure:
            return f'Особенность Т-Х: Частично Искусственная Личность - испытывает собственные эмоции '

    def __str__(self):
        return super(TX, self).__str__()


class T_3000(T_1000, TX):

    def nano(self, nano):
        if nano == self.weapon:
            return f'Особенность Т-3000: Принимает любую внешность'

    def mag(self, magnetic):
        if magnetic == self.structure:
            return f'Особенность Т-3000: Формирует магнитное поле'

    def special(self):
        return f'Преимущество Т-3000: Является следующей ступенью развития терминаторов ' \
               'и включает в себя все особенности Т-1000 и Т-Х'

    def __str__(self):
        return super(T_3000, self).__str__()

t_800 = Terminator('T-800 по имени Боб','Металлический эндоскелет','Огнестрельное','Изотопное',120)
t_1000 = T_1000('T-1000 по имени Патрик', 'Жидкий кристалл', 'Резонансный', 'Холодное', 150)
tx = TX('Т-Х по имени Кристина', 'Жидкий эндоскелет', 'Термоядерный', 'Плазменное', 160)
t_3000 = T_3000('T-3000 по имени Джон Коннор', 'Нанобот', 'Ионный', 'Пушка Гаусса', 200)

print(t_800)
print(f'{t_1000}\n{t_1000.form("Жидкий кристалл")}\n{t_1000.liquid("Холодное")}')
print(f'{tx}\n{tx.emotion("Жидкий эндоскелет")}\n{tx.prog("Плазменное")}')
print(f'{t_3000}\n{t_3000.nano("Пушка Гаусса")}\n{t_3000.mag("Нанобот")}')
print(t_3000.special())
