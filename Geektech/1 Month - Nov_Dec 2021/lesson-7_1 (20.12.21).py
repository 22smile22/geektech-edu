import random
import datetime

start = datetime.datetime.now()
students = [1, 2, 3, 4, 5, 7, 8, 10, 12, 15, 16, 17, 18]
# print(len(students))

# while len(students) != 0:
#     print(students.pop(students.index(random.choice(students))))
#     input('Next! ')
#     print(students)
#     # print(students)
# end = datetime.datetime.now() - start
# print('Опрос завершился\n'
#       f"Время программы: {end}"
#       )

import time

def timer(start):
    while start >= 0:
        print(start)
        time.sleep(1)
        start -= 1

# timer(5)

def stopwatch():
    start = 0
    while 1:
        print(start)
        time.sleep(1)
        start += 1
        # if start == 60:
        #     print()

stopwatch()
