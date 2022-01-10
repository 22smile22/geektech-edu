""" 2 Month - OOP - Jan 22 - 03.01.2022"""

class Car:
    # brand = "Mercedes"
    # model = 'C-class 340'
    # engine = 'Germany'
    # fuel = 3.5
    # color = 'grey'

    def __init__(self, brand, model, engine, fuel, color, passengers_quantity, price):
        if isinstance(brand, str):
            self.brand = brand
        else:
            raise ValueError('Brand should be string0')
        if isinstance(model, str):
            self.model = model
        else:
            raise ValueError('Model should be string0')
        if isinstance(engine, str):
            self.engine = engine
        else:
            raise ValueError('Engine should be string0')
        if isinstance(fuel, float):
            self.fuel = fuel
        else:
            raise ValueError('Fuel should be float0')
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError('Color should be string0')
        if isinstance(passengers_quantity, int):
            self.pass_q = passengers_quantity
        else:
            raise ValueError('Passengers should be integer0')
        if isinstance(price, int):
            self.price = price
        else:
            raise ValueError('Price should be integer0')

    def tunning(self, price_t):
        total = self.price + price_t
        return f'Total price of Car: {total}\n'

    def __str__(self): #constructor output in string
        return f'Brand: {self.brand}\n' \
               f'Model: {self.model}\n' \
               f'Engine: {self.engine}\n' \
               f'Fuel: {self.fuel}\n' \
               f'Color: {self.color}\n' \
               f'Passengers Quantity: {self.pass_q}\n' \
               f'Price: {self.price}$\n'

# global brand
# def card():
#     brand = 'Mercedes'
# print(brand)

car_1 = Car(brand='Mercedes', model='S-class', engine='Germany bomb',
            fuel=5.0, color='black', passengers_quantity=5, price=50000)
car_2 = Car(brand='Lexus', model='570', engine='Katana',
            fuel=5.7, color='silver', passengers_quantity=8, price=134789)

# print(car_1.color, car_2.color)
print(car_1)
print(car_1.tunning(1654))
print(car_2)
print(car_2.tunning(1963))


# car_1 = Car()
# print(car_1.color)
# print(car_1.fuel)
#
# car_2 = Car()
# print(car_2.color)


