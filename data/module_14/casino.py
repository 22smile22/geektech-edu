import random

class PythonCasino:
    def __init__(self):
        self.combination_red = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.combination_black = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.lucky_red = random.choice(self.combination_red)
        self.lucky_black = random.choice(self.combination_black)
        self.cash = 0
        print(f'Lucky red: {self.lucky_red}')
        print(f'Lucky black: {self.lucky_black}')

    def compare_combination(self, choice_red, choice_black):
        if choice_red == self.lucky_red and choice_black == self.lucky_black:
            self.cash += 100
            print(f'You win ! Now your balance is {self.cash}')
        elif choice_red == self.lucky_red and choice_black != self.combination_black:
            self.cash += 40
            print(f'You win the red combination, Balance: {self.cash}')
        elif choice_black == self.lucky_black and choice_red != self.combination_red:
            self.cash += 50
            print(f'You win the black combination, Balance: {self.cash}')
        else:
            print('You lose')
