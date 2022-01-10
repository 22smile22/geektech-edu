# from templates2 import greetings as g
# import templates2
#
# # greetings('Azamat')
# templates2.greetings('Samat')
# g('Kanat')

from pprint import pprint
import random
from random import randint, choice
from datetime import datetime
import time

# a = {
#     1: 5,
#     2: 6
# }
# guys = ['jack','alice','murat', 'anna', 'gregoriy']

# print(random.randint(1, 5))
# print(random.choice(guys))
# print(random.sample(guys, 2))
# pprint.pprint(a)
# pprint(random.sample(guys, 2))
# print(randint(1, 5))
# print(choice(guys))

# print(datetime.now())
# print(datetime.datetime.now())

# start = datetime.now()

# time.sleep(5)
# print(datetime.now().hour)


def greetings(name):
    hours = datetime.now().hour
    if hours >= 4 and hours <= 11:
        print(f'Доброе утро! {name}')
    elif 12 >= hours <= 17:
        print(f'Добрый день! {name}')
    elif 18 >= hours <= 23:
        print(f'Добрый вечер! {name}')
    else:
        print(f'Доброй ночи! {name}')

greetings('azat')


