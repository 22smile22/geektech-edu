# print("Hello, John!")
# print("Hello, Anna!")
print ("")

# def greetings(name: str):
#     # print("Hello, {}!".format(name))
#     print("Hello, {}!".format(name.capitalize()))
#
# greetings('Azamat')
# print(type(greetings('Azamat')))
# greetings('John')
# greetings('fred')
# # greetings('fred'.title())

# def upper_letter(arg: str):
#     return arg.upper()

# upped_word = upper_letter('bbs')
# print(upped_word)
# print(type(upped_word))

# print(upper_letter('bbs'))
#
# def upper_letter(arg):
#     return arg
#
# print(upper_letter('1'))


# def plus(a, c, b=2):
#     # return a + b
#     return (a - c) * b
#
# # print(plus(5, 3))
# print(plus(6, 3, 2))

# def pplus (a, b, c):
#     return (a - b) * c == 9
#
# print(pplus(6, 3, 2))


# def plus(*args): # *args преобразовывает все аргументы в единый кортеж
#     return round(sum(args) / len(args), 2)
#
# print(plus(4, 8, 6, 5, 56, 345))

# def plus(a, *args, b=3):
# def plus(a,  b=3, *args):
#     print(args)
#     return sum(args) + a + b
#
# print(plus(3, 4, 5))

# def menu(breakfast, lunch, dinner):
#     return dict(breakfast=breakfast, lunch=lunch, dinner=dinner)
#     # return {'breakfast': breakfast}
#
# print(menu("каша", "пельмени", "плов"))
# print(menu(dinner="лагман", breakfast="яичница", lunch="борщ"))

# def menu(**kwargs): # **kwargs преобразовывает именнованные аргументы в словарь
#     return kwargs
#
# print(menu(first='первый', second='второй', third='третий'))
