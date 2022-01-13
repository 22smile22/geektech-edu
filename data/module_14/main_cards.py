import random
from module_14.compare import CompareCards
from module_14.casino import PythonCasino

class BlackJack:
    def __init__(self):
        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.player = [random.choice(self.cards), random.choice(self.cards)]
        self.computer = [random.choice(self.cards), random.choice(self.cards)]
        self.die_or_win = [0, 0, 1000, 0]

    def game(self):
        print('Choose option:')
        print('1. Draw cards')
        print('2. Draw cards only to player')
        print('3. Draw cards only to computer')
        print('4. Russian Roulette')
        print(f'Your cards: {sum(self.player)}')
        print(f'Computer cards: {sum(self.computer)}')
        choice = int(input('Your choice: '))
        while True:
            compare_1 = CompareCards(player_list=self.player,
                                     computer_list=self.computer)
            if choice == 1:
                self.player.append(random.choice(self.cards))
                self.computer.append(random.choice(self.cards))
                if compare_1.compare_results():
                    break
                else:
                    pass
            elif choice == 2:
                self.player.append(random.choice(self.cards))
                if compare_1.compare_results():
                    break
                else:
                    pass
            elif choice == 3:
                self.computer.append(random.choice(self.cards))
                if compare_1.compare_results():
                    break
                else:
                    pass
            elif choice == 4:
                self.player.append(random.choice(self.die_or_win))
                self.computer.append(random.choice(self.die_or_win))
                if compare_1.compare_results():
                    break
                else:
                    pass

        print('Restart Option: ')
        print('1. \'y\' = Restart Black Jack')
        print('2. \'another\' = Start Casino Game')
        restart_or_no = input('\nDo you want to restart or play another game: ')
        if restart_or_no == 'y':
            black = BlackJack()
            black.game()
        elif restart_or_no == 'another':
            casino_1 = PythonCasino()
            choice_red = int(input('Red Combination Choice: '))
            choice_black = int(input('Black Combination Choice: '))
            casino_1.compare_combination(choice_red=choice_red,
                                         choice_black=choice_black)
        else:
            pass

# black_cards = BlackJack()
# black_cards.game()

def choose_game(choice):
    while True:
        if choice == 'b':
            black = BlackJack()
            black.game()
            break
        elif choice == 'c':
            casino_1 = PythonCasino()
            choice_red = int(input('Red Combination Choice: '))
            choice_black = int(input('Black Combination Choice: '))
            casino_1.compare_combination(choice_red=choice_red,
                                         choice_black=choice_black)
            break

print('Game Option: ')
print('1. Black Jack (b)')
print('2. Casino (c)')
choice = input('Your game choice: ')
choose_game(choice=choice)
