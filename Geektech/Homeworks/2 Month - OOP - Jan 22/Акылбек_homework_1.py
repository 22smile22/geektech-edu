"""
Группа  Geektech 14Py - студент Акылбек Мамбетакунов
Месяц 2 - ООП. Домашнее задание №1

1) Создать суперкласс Animal и его классы (пример: Млекопитающиеся, Пресмыкающиеся)
Они должны быть связаны через наследование
2) Класс Animal имеет общие параметры животных
3) Класс Млекопитающих и других имеют свои особенные методы атрибуты и методы
4) Создать объекты животных и классов
"""

class Animal:
    def __init__(self, species, name):
        if isinstance(species, str):
            self.species = species
        else:
            raise ValueError('Species must be a string')
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name should be string')

    def __str__(self):
        return f'Класс животного: {self.species}\n' \
               f'Название вида: {self.name}\n'

class Mammal(Animal):
    def __init__(self, species, name, human, predator, tail):
        super().__init__(species, name)
        if isinstance(human, bool):
            self.human = human
        else:
            raise ValueError('Human must be a boolean')
        if isinstance(predator, bool):
            self.predator = predator
        else:
            raise ValueError('Predator must be boolean')
        if isinstance(tail, bool):
            self.tail = tail
        else:
            raise ValueError('Tail must be boolean')

    def __str__(self):
        return super(Mammal, self).__str__() + f'Относится ли к человеку? {self.human}\n' \
                                               f'Хищник? {self.predator}\n' \
                                               f'Наличие хвоста? {self.tail}\n'

class Human(Mammal):
    def __init__(self, species, name, human, predator, tail, avg_age, sex, avg_weight, avg_height):
        super().__init__(species, name, human, predator, tail)
        if isinstance(avg_age, int):
            self.age = avg_age
        else:
            raise ValueError('Age must be integer')
        if isinstance(sex, str):
            self.sex = sex
        else:
            raise ValueError('Sex must be string')
        if isinstance(avg_weight, float):
            self.weight = avg_weight
        else:
            raise ValueError('Weight must be float')
        if isinstance(avg_height, int):
            self.height = avg_height
        else:
            raise ValueError('Height must be integer')


    def __str__(self):
        return super(Human, self).__str__() + f'Средняя продолжительность жизни: {self.age} л.\n' \
                                              f'Пол: {self.sex}\n' \
                                              f'Средний рост: {self.weight} см.\n' \
                                              f'Средний вес {self.height} кг.\n'
class Tiger(Mammal):
    def __init__(self, species, name, human, predator, tail, home_animal, paws):
        super().__init__(species, name, human, predator, tail)
        if isinstance(home_animal, str):
            self.home = home_animal
        else:
            raise ValueError('Home animal must be string')
        if isinstance(paws, int):
            self.paw = paws
        else:
            raise ValueError('Paws should be integer')

    def __str__(self):
        return super(Tiger, self).__str__() + f'Домашнее животное? {self.home}\n' \
                                              f'Наличие лап? {self.paw} лапы\n'

mouse_1 = Mammal('Млекопитающий', "Мышь", False, False, True)
human_1 = Human('Млекопитающий', "Человек", True, True, False, 75, "Мужчина", 1.70, 70)
tiger_1 = Tiger('Млекопитающий', "Тигр", False, True, True, "Дикое", 4)
print(f'{mouse_1}\n{human_1}\n{tiger_1}')


class Reptilia(Animal):
    def __init__(self, species, name, eggs, skin):
        super().__init__(species, name)
        if isinstance(eggs, bool):
            self.eggs = eggs
        else:
            raise ValueError('Eggs must be a boolean')
        if isinstance(skin, str):
            self.skin = skin
        else:
            raise ValueError('Skin should be string')

    def __str__(self):
        return super(Reptilia, self).__str__() + f'Откладывают яйца? {self.eggs}\n' \
                                                 f'Тип кожи: {self.skin}\n'

class Snake(Reptilia):
    def __init__(self, species, name, eggs, skin, haematocryal, flakiness, avg_lenght):
        super().__init__(species, name, eggs, skin)
        if isinstance(haematocryal, bool):
            self.cold = haematocryal
        else:
            raise ValueError('Cold must be boolean')
        if isinstance(flakiness, str):
            self.flake = flakiness
        else:
            raise ValueError('Flake must be string')
        if isinstance(avg_lenght, float):
            self.lenght = avg_lenght
        else:
            raise ValueError('Lenght should be float')

    def __str__(self):
        return super(Snake, self).__str__() + f'Теплокровный?  {self.cold}\n' \
                                              f'Есть чешуя? {self.flake}\n' \
                                              f'Средняя длина: {self.lenght}м.\n'

reptile_1 = Reptilia('Пресмыкающиеся', "Рептилия", True, "Сухой")
snake_1 = Snake('Пресмыкающиеся', "Змея обыкновенная", True, "Сухой", False, "Да", 6.5)
print(f'{reptile_1}\n{snake_1}')