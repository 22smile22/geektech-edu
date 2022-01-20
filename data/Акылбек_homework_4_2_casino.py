"""
Группа  Geektech 14Py - студент Акылбек Мамбетакунов
Месяц 2 - ООП. Домашнее задание №4. (Задача №2)

1. Создать многомодульную игру в казино
2. Сам запуск игры в отдельном файле
3. Логика выигрыша или проигрыща в отдельном файле
4. Логика Фортуны также в отдельном файле

Правила игры такие:

1. Есть массив чисел от 1 до 30, каждый раз вы делаете ставку на определенную слоту из чисел и ставите деньги
2. Рандомно выбирается выигрышная слота, если вы выигрываете, вам причисляются сумма двойная которую вы поставили
3. В начале игры у вас также есть деньги например 1000$, но в конце мы понимаем вы в выигрыше или в проигрыше
4. Также по окончанию игры, вы имеете возможность сыграть в фортуну, для увеличения прибыли или наоборот увеличения долга
5. Фортуна должна быть такая: на верю и не верю
6. Судья показывает вам дверь, и говорит кто за дверью (за дверью всегда мифические животные), если вы угадываете
то получаете прибыль, если нет - то увеличивается долг
7. То что говорит судья не всегда соответствует тому что есть за дверью.
"""

from random import choice
class CasinoPlay:
    def __init__(self,money, value):
        self.money = money
        self.add_take = value

    def game(self, number, bid):
        random_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        random = choice(random_list)
        print(f'Ваша ставка {number}, сумма ставки {bid}')
        if random == number:
            self.add_take += bid
            self.money = self.money + bid
            print(f'Вышло число: {random}\nВаш выигрыш! {bid}$, Банк: {self.money}$')
            return True
        elif random != number:
            self.add_take -= bid
            self.money = self.money - bid
            print(f'Вышло число: {random}\nВаш проигрыш {bid}$, Банк: {self.money}$')
            return True
        else:
            print(f'Неприменимо!')
            return True
