""" 2 Month - OOP - Jan 22 - 20.01.2022
algo_14.py
"""

import random

door = ['goat', 'auto']

def choose_doors(choices):
    choice = random.choice(choices)
    print('You did your choice')
    option = input('One of the dorr revelead, and it is not prize door'
                   'Do you want to change your mind?\n')
    if option == 'n':
        if choice == 'auto':
            print(f'Your choice was {choice}')
            print('You win auto')
        elif choice == 'goat':
            print('You loose, it is not prize door')
    elif option == 'y':
        print(f'Your original choice was {choice}')
        if choice == 'goat':
            choice = 'auto'
            print(f'You new choice {choice}')
            print('You win the auto')
        elif choice == 'auto':
            choice = 'goat'
            print(f'You new choice {choice}')
            print('You loose, it is not prize door')

choose_doors(door)

