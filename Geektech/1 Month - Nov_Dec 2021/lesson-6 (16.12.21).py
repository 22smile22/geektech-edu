# word = ['python', '2 Month - OOP - Jan 22', 'exceptions', 'lambda']
# def bigger(list, func):
#     for i in list:
#         print(func(i))

# def up_letter(words):
#     return words.title() + '!'

# lf = lambda words: words.title() + '!'

# bigger(word, lambda word: word.title() + '!')

# bigger(word, lf)
# print(type(lf))
# bigger(word, up_letter())
# ----------

# lambda значение: выражение

# new = lambda x=2, y=3: (x * 3) / y
# print(new())

word = ('one', 'two', 'three', 'four', '12')
numbers = [1, 2, 3, 4, 5]

# new = dict(zip(word, numbers))
# print(new)

# a = list(filter(lambda x: len(x) <= 3, word))
# a = list(filter(lambda x: x >= 2 and x <= 4, numbers))
# print(a)
# print(type(a))

b = list(map(lambda x: x * x, numbers))
print(b)

# ----------

# word = ('one', 'two', 'three', 'four')
# numbers = [1, 2, 3, 4]

# dct = {}
#
# c = 0
# while c < len(word):
#     dct[word[c]] = numbers[c]
#     c += 1
#     print(dct)

# fltr = lambda x: x ** 2
# print(fltr(5))

