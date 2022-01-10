#print('vdvxvxcvcx afas fdbcx asdaxz')


# names = ['jack', 'mary', 'wayne']
names2 = 'jack', 'mary', 'wayne'
# names3 = ('jack', 'mary', 'wayne')
#
#
# # names2 += names3
#
# # names2 = list(names2)
# # names = tuple(names)
# #
# # print(names2)
# # print(type(names2))
# # print(type(names))
# # print(type(names3))
#
strings = []
numbers = list()
bools = []
tpl_lst = []

objects = [
    'list', 'tuple', 2, 5, 2.9, True, False,
    [1, 2, 3], names2
]

# objects = [
#     'list', 2, False, names2
# ]

while len(objects) != 0:
    for i in objects:
    # print(i)
        if type(i) == str:
            strings.append(objects.pop(objects.index(i)))
        elif type(i) == int or type(i) == float:
            numbers.append(objects.pop(objects.index(i)))
        elif type(i) == bool:
            bools.append(objects.pop(objects.index(i)))
        elif type(i) == list or type(i) == tuple:
            tpl_lst.append(objects.pop(objects.index(i)))


print(objects)
print(strings)
print(numbers)
print(bools)
print(tpl_lst)


# bool()
#
# print(bool('qwe'))
# print(bool(0))
#
# c = 0
# while 'abc':
#     print(c)
#     c += 1
