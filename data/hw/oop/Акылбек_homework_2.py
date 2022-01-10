"""
Группа  Geektech 14Py - студент Акылбек Мамбетакунов
Месяц 2 - ООП. Домашнее задание №2

Задача #1 Наследование (+ 3 класса объекта )
1. Создать трехступенчатую концепцию (дед-отец-ребенок) любого примера который вам ближе
2. Все три класса должны иметь свои особенные методы и атрибуты как минимум два доп метода у каждого класса
3. Также создать хотя бы по одному объекту к каждому классу

Задача #2 Инкапсуляция (+ 1 класс объекта )
1. Создать один класс в котором вы пропишете по одному методу (внутреннего и защищенного)
2. В этом классе должно быть также по одному атрибуту (внутреннего и защищенного)

Задача #3 Полиморфизм без наследования(+ 3 класса объекта )
1. Создать три разных класса в котором будут одинаковые методы по названию например (attack)
2. Но логика этого самого метода будут разные как в случае примера с мечником , лучником и волшебником

Задача #4 Полиморфизм с наследованием (+ 3 класса объекта )
1. Все тоже самое как в случае с Полиморфизмом без наследование , единственное различие здесь присутствует
наследование трехступенчатой концепций (дед-отец-ребенок)
"""

""" 
---------------------------------------------------------------------------------------------------------------------
1) Наследование 
"""

class Night_oper:
    def __init__(self, calls, journals, monitoring, instructions, social_networks, time_work):
        self.call = calls
        self.journal = journals
        self.monit = monitoring
        self.instr = instructions
        self.social = social_networks
        self.time = time_work

    def __str__(self):
        return f'Приём звонков: {self.call}-линия\n' \
               f'Запись всех событий журнал: {self.journal}\n' \
               f'Мониторинг системы: {self.monit}-уровень\n' \
               f'Следование по инструкциям: {self.instr}\n' \
               f'Время работы: {self.time}\n'

    def occupation(self, name):
        return f'Наименование должности: {name}\n'

class Specialist(Night_oper):
    def __init__(self, calls, journals, monitoring, instructions, social_networks, time_work,
                 private_clients, control_n_opers):
        super().__init__(calls, journals, monitoring, instructions, social_networks, time_work)
        self.priv = private_clients
        self.control = control_n_opers

    def __str__(self):
        return super(Specialist, self).__str__() + f'Обслуживание физ лиц: {self.priv}\n' \
                                                   f'Ответственность за операторами: {self.control}\n'

    def occupation(self, name):
        return f'Наименование должности: {name}\n'

class Senior_spec(Specialist):
    def __init__(self, calls, journals, monitoring, instructions, social_networks, time_work,
                 bank_clients, mentoring, private_clients, control_n_opers):
        super().__init__(calls, journals, monitoring, instructions, social_networks, time_work,
                         private_clients, control_n_opers)
        self.bank = bank_clients
        self.mentor = mentoring

    def __str__(self):
        return super(Senior_spec, self).__str__() + f'Обслуживание банков: {self.bank}\n' \
                                                    f'Обучение специалистов: {self.mentor}\n'

    def occupation(self, name):
        return f'Наименование должности: {name}\n'

class Lead_spec(Senior_spec):
    def __init__(self, calls, journals, monitoring, instructions, social_networks, time_work,
                 global_projects, team_leading, bank_clients, mentoring, private_clients,
                 control_n_opers):
        super().__init__(calls, journals, monitoring, instructions, social_networks, time_work,
                         bank_clients, mentoring, private_clients, control_n_opers)
        self.g_project = global_projects
        self.t_lead = team_leading

    def __str__(self):
        return super(Lead_spec, self).__str__() + f'Участие в глобальных задачах: {self.g_project}\n' \
                                                  f'Контроль за отделом: {self.t_lead}\n'

    def occupation(self, name):
        return f'Наименование должности: {name}\n'

n_oper1 = Night_oper(1, True, 1, True, True, 'c 18.00 до 9.00')
spec_1 = Specialist(2, True, 2, True, True, 'c 08.00 до 17.00', True, True)
senior_1 = Senior_spec(3, True, 3, False, False, 'c 09.00 до 18.00', True, True, False, False)
lead_1 = Lead_spec(4, False, 4, False, False, 'c 10.00 до 16.00', True, True, False, False, False, False)

# print(f"{n_oper1.occupation('Ночные операторы')}{n_oper1}")
# print(f"{spec_1.occupation('Дневные специалисты')}{spec_1}")
# print(f"{senior_1.occupation('Старшие специалисты')}{senior_1}")
# print(f"{lead_1.occupation('Главные специалисты')}{lead_1}")

""" 
---------------------------------------------------------------------------------------------------------------------
2) Инкапсуляция 
"""

class Access:
    def __init__(self, login, password, access_level):
        self._log = login
        self.__password = password # Password is private
        self.acs_level = access_level

    def __str__(self):
        if 1 < self.acs_level == 2:
            return (f'Error: Access denied!!\nYour privilege level is -> {self.acs_level}')
        elif 0 < self.acs_level == 1:
            return (f'Warning: Access limited!\nYour privilege level is -> {self.acs_level}')
        elif self.acs_level == 0:
            return (f'Success: Access granted.\nYour privilege level is -> {self.acs_level}')
        else:
            return ('Fatal Error: You have not a permission!!!')


acs_1 = Access('root', 123, 0)

# print(acs_1)
# print(f'Логин: {acs_1._log}')
# print(f'Пароль: {acs_1.__password})

"""
---------------------------------------------------------------------------------------------------------------------
3) Полиформизм без наследования
"""

class Wallet:
    def __init__(self, brands, tokens, method, os):
        self.brand = brands
        self.token = tokens
        self.method = method
        self.os = os

    def __str__(self):
        return f'Марка: {self.brand}\n' \
               f'Идентификация: {self.token}\n' \
               f'Способ оплаты: {self.method}\n' \
               f'Операционная система: {self.os}\n'

class Apple_Pay(Wallet):
    def pay(self):
        return f'Оплата прошла через {self.method} на {self.brand}\n'

class Samsung_Pay(Wallet):
    def pay(self):
        return f'Оплата прошла через {self.method} на {self.brand}\n'

class Google_Pay(Wallet):
    def pay(self):
        return f'Оплата прошла через {self.method} на {self.brand}\n'

iphone_1 = Apple_Pay('iPhone 13 Pro Max', 'Face ID', 'Apple Pay', 'Apple iOS 15.2')
galaxy_1 = Samsung_Pay('Samsung Galaxy S21', 'Touch ID', 'Samsung Pay','One UI 2.0 - Android 11')
pixel_1 = Google_Pay('Google Pixel 6 Pro', 'Touch ID', 'Google Pay', 'Android 12')

# print(iphone_1)
# print(iphone_1.pay())
#
# print(galaxy_1)
# print(galaxy_1.pay())
#
# print(pixel_1)
# print(pixel_1.pay())


"""
---------------------------------------------------------------------------------------------------------------------
4) Полиформизм с наследованием
"""

class Weapon:
    def __init__(self, type, ammo, range, perfomance):
        self.type = type
        self.ammo = ammo
        self.range = range
        self.perf = perfomance

    def __str__(self):
        return f'Тип оружия: {self.type}\n' \
               f'Тип боеприпасов: {self.ammo}\n' \
               f'Дальность: {self.range} м\n' \
               f'Эффективность: {self.perf}\n'

    def fire(self):
        return f'Первобытные люди для стрельбы использовали - "{self.ammo}"\n'

class Archer(Weapon):
    def __init__(self, arc_char, type, ammo, range, perfomance):
        super().__init__(type, ammo, range, perfomance)
        self.char = arc_char

    def fire(self):
        return f'{self.char} для стрельбы использует - "{self.ammo}"\n'

class Grenadier(Archer):
    def __init__(self, gre_char, arc_char, type, ammo, range, perfomance):
        super().__init__(arc_char ,type, ammo, range, perfomance)
        self.g_char = gre_char

    def fire(self):
        return f'{self.g_char} для стрельбы использует - "{self.ammo}"\n'

class Sniper(Grenadier):
    def __init__(self, sni_char ,gre_char, arc_char, type, ammo, range, perfomance):
        super().__init__(gre_char, arc_char, type, ammo, range, perfomance)
        self.s_char = sni_char

    def fire(self):
        return f'{self.s_char} для стрельбы использует - "{self.ammo}"\n'

weapon_1 = Weapon('Дубина', 'Камни', 0.5, 'Невысокая')
archer_1 = Archer('Лучник','Лук', 'Стрелы', 15.5, 'Средняя')
grenadier_1 = Grenadier('Гренадёр', False, 'Мушкет', 'Свинцовые круглые пули', 50.0, 'Высокая')
sniper_1 = Sniper('Cнайпер', False, False, 'Снайперская винтовка', 'Пули со стальным наконечником', 1500, 'Убойная')

# print(weapon_1)
# print(weapon_1.fire())

# print(archer_1)
# print(archer_1.fire())

# print(grenadier_1)
# print(grenadier_1.fire())

# print(sniper_1)
# print(sniper_1.fire())