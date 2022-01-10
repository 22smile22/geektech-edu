fast_food = {
    "Гамбургер": 100,
    "Шаурма": 160,
    "Хот-дог": 85,
    "Самсы": 45,
}

"""
Написать программу, при которой человеку показывается меню и он по продукту узнает стоимость
"""

def menu():
    #print(fast_food.keys())
    for k, v in fast_food.items():
        print(f'{k} {v}')

def choice():
    menu()
    print("")
    product = input("Выберите продукт: ")
    lst = []
    if product in fast_food.keys():
        print(f'Цена: {fast_food.get(product)} cом')
    else:
        print("Такого продукта нет в меню")

while 1:
    print("")
    a = "Сделайте ваш заказ"
    print(a)
    choice()
    choice2 = input('Что-нибудь ещё?\n')
    if choice2 == 'Нет':
        break
    elif choice2 == 'Да':
        continue
    else:
        print("Простите? Не могли бы повторить ещё раз")


