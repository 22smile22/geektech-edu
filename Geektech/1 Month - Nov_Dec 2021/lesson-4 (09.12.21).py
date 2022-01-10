# dict = {key: value}

dct = (['apple', 'яблоко'], ['lemon', 'лимон'], ['orange', 'апельсин'])

"""convert to dict any list, tuple"""
dict_en_ru = dict(dct)
dict_en_ru['orange'] = 'мандарин'

"""a problem with changed, needed .copy()"""
new = dict_en_ru.copy()
# new = dict_en_ru.deecopy()
new['orange'] = 'аыафаы'

# print(dct)
print(dict_en_ru)
print(new)

student = dict(name='Jessica', last_name='Alba')
print("")


"""The key must be a unique"""
student1 = {
    "name": "Mary",
    "age": 20,
    "height": 1.65,
    1: True,
    'hobby': ['books', 'chess'],
    "name2": 'Marina'
}

# print(student1["name"])
# print(student1["age"])

# """add or change dict"""
# student1['job'] = 'doctor'
# student1['age'] = 21
#
# """delete dict"""
# del student1[1] #, student1['name']
# student1.pop('name2')
#
# """add to list in dict"""
# student1['hobby'].append('cooking')
#
# """extend dict for another dict"""
# student1.update(student)

"""view separately dict values: keys->values"""
# print(student1.keys())
# print(student1.values())
# print(student1.items()) # view dict in tuples
# # print(student1)

# for k, v in student1.items():
#     print(f'{k}: {v}')
#     # print(k,':', v)
