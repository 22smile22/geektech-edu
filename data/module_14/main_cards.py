import random
from module_14.compare import CompareCards

class BlackJack:
    def __init__(self):
        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.player = [random.choice(self.cards), random.choice(self.cards)]
        self.computer = [random.choice(self.cards), random.choice(self.cards)]

    def game(self):
        print('Choose option:')
        print('1. Draw cards')
        print('2. Draw cards only to player')
        print('3. Draw cards only to computer')
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

black_cards = BlackJack()
black_cards.game()
