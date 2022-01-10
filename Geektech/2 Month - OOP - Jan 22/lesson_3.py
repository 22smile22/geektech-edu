""" 2 Month - OOP - Jan 22 - 10.01.2022"""

import random
from lesson_3_1 import Calculator

rand_int = random.randint(1, 2)
print(rand_int)
calc_2 = Calculator()
print(calc_2.__add__(5))

class CustomUser:
    def __init__(self, first_name, last_name, email, password, age, gender, phone, secret_key, username):
        if isinstance(first_name, str):
            self.first = first_name
        else:
            raise Exception('First name is string')
        if isinstance(last_name, str):
            self.last = last_name
        else:
            raise Exception('Last name is string')
        if isinstance(email, str):
            self.email = email
        else:
            raise Exception('Email is string')
        if isinstance(password, str):
            self.password = password
        else:
            raise Exception('Password is string')
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError('Age is integer')
        if isinstance(gender, str):
            self.gender = gender
        else:
            raise ValueError('Gender is string')
        if isinstance(phone, str):
            self.phone = phone
        else:
            raise ValueError('Phone is string')
        if isinstance(secret_key, str):
            self.secret = secret_key
        else:
            raise ValueError('Secret key is string')
        if isinstance(username, str):
            self.username = username
        else:
            raise ValueError('First name is string')

    def __str__(self):
        return f'Username: {self.username}\n' \
               f'First-name: {self.first}\n' \
               f'Last-name: {self.last}\n' \
               f'Email: {self.email}\n' \
               f'Password: {self.password}\n' \
               f'Age: {self.age}\n' \
               f'Gender: {self.gender}\n' \
               f'Phone: {self.phone}\n' \
               # f'Secret Key: {self.secret}\n'

user_1 = CustomUser(username='telidas', first_name='Adilet', last_name='Saparbek',
                    email='adilet@gamil.com', password='123', age=24,
                    gender='male', phone='0789654123', secret_key='Bish')

print(user_1)

class Admin(CustomUser):
    def __init__(self, first_name, last_name, email, password, age, gender, phone, secret_key, username):
        super().__init__(first_name, last_name, email, password, age, gender, phone, secret_key, username)

    def admin_panel_login(self, password_login):
        if password_login == self.password:
            # print('All info')
            return 'All info'


    def __str__(self):
        return super(Admin, self).__str__()

admin_1 = Admin(username='telidas', first_name='Adilet', last_name='Saparbek',
                    email='adilet@gamil.com', password='123', age=24,
                    gender='male', phone='0789654123', secret_key='Bish')

# print(admin_1)
# admin_1.admin_panel_login('123'))
#print(admin_1.admin_panel_login('123'))

class VIPClient(CustomUser):
    def __init__(self, first_name, last_name, email, password, age, gender, phone, secret_key, username):
        super().__init__(first_name, last_name, email, password, age, gender, phone, secret_key, username)

    def vip_platezhki(self):
        return f'VIP 50$'

    def __str__(self):
        return super(VIPClient, self).__str__()

class SuperUser(Admin, VIPClient):
    def __init__(self, first_name, last_name, email, password, age, gender, phone, secret_key, username):
        super().__init__(first_name, last_name, email, password, age, gender, phone, secret_key, username)

    def __str__(self):
        return super(SuperUser, self).__str__()

sup_user = SuperUser(username='telidas', first_name='Adilet', last_name='Saparbek',
                    email='adilet@gamil.com', password='123', age=24,
                    gender='male', phone='0789654123', secret_key='Bish')

# print(sup_user)
# print(sup_user.vip_platezhki())

