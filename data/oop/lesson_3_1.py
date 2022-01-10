""" 2 Month - OOP - Jan 22 - 10.01.2022"""

class Calculator:

    def __add__(self, other):
        return 6 + other

    def __sub__(self, other, number):
        summary = other - number
        return summary

    def __mul__(self, other, number, number_2, number_3, number_4):
        summary = other * number * number_2 * number_3 * number_4
        return summary

    def __truediv__(self, other, number):
        summary = other / number
        return summary

    def __len__(self, string_some):
        return len(string_some)



calc = Calculator()
print(calc.__add__(6))
print(calc.__sub__(9, 9))
print(calc.__mul__(1, 2, 3, 4, 5))
print(calc.__truediv__(9, 2))
print(calc.__len__('adilet'))

