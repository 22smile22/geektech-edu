""" 2 Month - OOP - Jan 22 - 03.01.2022"""

class Phone:
    def __init__(self, number, camera, screen, CPU, memory, touch_id, flash):
        if isinstance(number, str):
            self.number = number
        else:
            raise ValueError('Number is not str')
        if isinstance(camera, float):
            self.camera = camera
        else:
            raise ValueError('Camera should be float')
        if isinstance(screen, bool):
            self.screen = screen
        else:
            raise Exception('Screen is boolean ')
        if isinstance(CPU, float):
            self.CPU = CPU
        else:
            raise ValueError('CPU is float!!!')
        if isinstance(memory, int):
            self.memory = memory
        else:
            raise ValueError('Passengers should be integer')
        if isinstance(touch_id, bool):
            self.touch = touch_id
        else:
            raise ValueError('Touch ID is boolean')
        if isinstance(flash, bool):
            self.flash = flash
        else:
            raise ValueError('Flash is boolean')

    def __str__(self):
        return f'Number: {self.number}\n' \
               f'Camera: {self.camera}\n' \
               f'Screen: {self.screen}\n' \
               f'CPU: {self.CPU}\n' \
               f'Memory: {self.memory}\n' \
               f'Touch ID: {self.touch}\n' \
               f'Flash: {self.flash}\n'

nokia_6300 = Phone('+996666321', 1.2, False, 0.7, 512, False, True)
print(nokia_6300)

class IPhone(Phone):
    def __init__(self, number, camera, screen, CPU, memory, touch_id, flash, ecosystem, fame, icloud):
        super().__init__(number, camera, screen, CPU, memory, touch_id, flash)
        if isinstance(ecosystem, bool):
            self.eco = ecosystem
        else:
            raise ValueError('Ecosystem is boolean')
        if isinstance(fame, str):
            self.fame = fame
        else:
            raise ValueError('Fame is string')
        if isinstance(icloud, int):
            self.cloud = icloud
        else:
            raise ValueError('Icloud is integer')

    # def calc(self):

    def __str__(self):
        return super(IPhone, self).__str__() + f'\nEcosystem {self.eco}\n' \
                                               f'Fame: {self.fame}\n' \
                                               f'ICloud: {self.cloud}\n'

iphone_1 = IPhone('+996556996', 16.0, True, 2.4, 512, True, True, True, 'This is Iphone',
                  icloud=32)
print(iphone_1)

