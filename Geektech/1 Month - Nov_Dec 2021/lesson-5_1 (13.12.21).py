print("")

abiturients1 = [
    {'name': "Irina", 'ORT': 150},
    {'name': "Wayne", 'ORT': 220},
    {'name': "Fred", 'ORT': 90}
]

abiturients2 = [
    {'name': "Anton", 'ORT': 150},
    {'name': "Eliza", 'ORT': 220},
    {'name': "Timur", 'ORT': 90}
]

def list_students(list):
    for i in list:
        for k, v in i.items():
            print(f'{k}: {v}')

# list_students(abiturients1)
# list_students(abiturients2)

def add_student(list, name, ORT):
    list.append(dict(name=name, ORT=ORT))
    list_students(list)

add_student(abiturients2, 'Paul', 160)

def del_student(list, name):
    for i in list:
        if name.title() == i['name']:
            del_s = list.pop(list.index(i))
            print(f"{del_s['name']} Удалён из студентов!")
        list_students(list)

del_student(abiturients1, 'Wayne')

while 1:
    user = input()
    if user == 1:
        add_student()
    elif user == 2:
        del_student()