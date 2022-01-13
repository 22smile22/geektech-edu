class CompareCards:
    def __init__(self, player_list, computer_list):
        self.player_list = player_list
        self.computer_list = computer_list

    def compare_results(self):
        if sum(self.player_list) > 21 and sum(self.computer_list) < 21:
            print(f'Our cards: {sum(self.player_list)}, Computer wins! Computer: {sum(self.computer_list)}')
            return True
        elif sum(self.player_list) < 21 and sum(self.computer_list) > 21:
            print(f'Our cards: {sum(self.player_list)}, You win! Congrats! Computer: {sum(self.computer_list)}')
            return True
        elif sum(self.player_list) > 21 and sum(self.computer_list) > 21:
            print(f'Draw! Our cards: {sum(self.player_list)}, Computer: {sum(self.computer_list)}')
            return True

    