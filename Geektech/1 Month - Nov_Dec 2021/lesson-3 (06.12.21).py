strings = 'python'
ints = 25
floats = 2.5
bools = True or False

#   if, elif, else
# != == >=

# names = [strings, ints, floats, bools, 23, 44, 'word']
# names = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# print(names[0])

# print(names)
# print(names[1:5:2])
# print(names[0:-1:2])
# print(names[::-1])
# print(names[0:5])

# names2 = names[1:4]
# print(names2)

words = ['oop','apple','game']
numbers = [9, 2, 7, 4, 3, 2]
# numbers = [1, 2, 3, 4, 5, 'abc']
# words = list('2 Month - OOP - Jan 22, pyth, rtr')
# words = ['2 Month - OOP - Jan 22, pyth, rtr']

print(numbers.index(9))
print(numbers.count(2))

""" Реверс списка """
# numbers.reverse()

""" сортировка списка """
# words.sort()
# numbers.sort()
# s_numbers = sorted(numbers)

# print(s_numbers)
# print(words)

""" изменить элемент списка """
# numbers[0] = 'one'

""" слияние списков и/или расширение"""
# numbers += words
# numbers.extend(words)

""" добавление элемента в список """
# numbers.append(2.7) #added in end of the list
# numbers.insert(2, 2.1) #added in choosed position of the list

# print(type(words))
# print(type(numbers))

print(numbers)

""" удаление из списка """
# deleted = numbers.pop(3)
# print(deleted)
# del numbers[2]
# numbers.remove('abc')
# print(numbers)