""" 2 Month - OOP - Jan 22 - 06.01.2022"""

class Account:
    """
    This is class object which is working with accounts and their personal information
    """
    def __init__(self, name, password, secret_question):
        self.name = name
        self.__password = password  # this is password do not touch
        self._secret = secret_question

    def _password1(self):
        pass

acc = Account('Adilet', password='123', secret_question='Bish')
# print(acc.__password)
# print(acc._secret)
# print(acc._password1)

"""Полиформизм"""

class Character:
    def __init__(self, name, height, skill):
        self.name = name
        self.height = height
        self.skill = skill

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Height : {self.height}\n' \
               f'Skill : {self.skill}\n'

class Magician(Character):
    def attack(self):
        return f'Attacking with spell {self.skill}'

class Paladin(Character):
    def attack(self):
        return f'Attacking with {self.skill}'

class Archer(Character):
    def attack(self):
        return f'Attacking with bow and {self.skill}'

mag = Magician('Gendelf', 200, 'Fireball')
paladin = Paladin('Georg', 210, 'Holy word')
arc = Archer('Zelle', 180, 'Poisoned arrow')

print(mag.attack())
print(paladin.attack())
print(arc.attack())


