"""
Группа  Geektech 14Py - студент Акылбек Мамбетакунов
Месяц 2 - ООП. Домашнее задание №3. (Задача №2)

Задача #2 Множественное Наследование (Один ко многим)
1. Создать 4 класса, один из которых будет супер-классом, от которого наследуются остальные 3 класса
2. У супер-класса должно быть как минимум 4 атрибута (def __init__(self, atribut, atribut2):)
3. У каждого класса должно быть минимум 2 метода (def method(self): )
4. Также должны быть соблюдены def __str__(self) + super()
5. К каждому классу создать по одному объекту (в итоге должно быть 4 объекта)

Задачи 1 и 3 представлены в файлах Акылбек_homework_3_1.py и Акылбек_homework_3_3.py
"""

class PaymentCards:
    def __init__(self, embossing, chip, nfc, magstripe, wallet):
        self.embos = embossing
        self.chip = chip
        self.nfc = nfc
        self.mag = magstripe
        self.wallet = wallet

    def __str__(self):
        return f'Способ изготовления: {self.embos}\n' \
               f'Микропроцессор: {self.chip}\n' \
               f'Бесконтактный модуль: {self.nfc}\n' \
               f'Магнитная полоса: {self.mag}\n' \
               f'Оцифровка карты: {self.wallet}\n' \


class VisaClassic(PaymentCards):
    def __init__(self, embossing, chip, nfc, magstripe, wallet, vc_class):
        super().__init__(embossing, chip, nfc, magstripe, wallet)
        self.vc = vc_class

    def GlobalSupport(self, note):
        if note == self.vc:
            return f'Для данного класса карт - Доступна поддержка 24/7'

    def EmergencyAid (self, note):
        if note == self.vc:
            return f'Для данного класса карт - Доступна Экстренная служба поддержки\n'


    def __str__(self):
        return super(VisaClassic, self).__str__() + \
               f'Пометка: {self.vc}\n'

class AmexGold(VisaClassic):
    def __init__(self, embossing, chip, nfc, magstripe, wallet, vc_class, vc_gold):
        super().__init__(embossing, chip, nfc, magstripe, wallet, vc_class)
        self.gold = vc_gold

    def MedicalAid (self, note):
        if note == self.vc:
            return f'Для данного класса карт {self.gold} - Доступна медицинская помощь и услуги\n'

    def Discount (self, note):
        if note == self.vc:
            return f'Для данного класса карт {self.gold} - Доступны Скидки и Привилегии'

    def __str__(self):
        return super(AmexGold, self).__str__() + \
               f'Категория: {self.gold}\n'

class MastercardPlatinum(VisaClassic):
    def __init__(self, embossing, chip, nfc, magstripe, wallet, vc_class, vc_plat):
        super().__init__(embossing, chip, nfc, magstripe, wallet, vc_class)
        self.plat = vc_plat

    def Insurance (self, note):
        if note == self.vc:
            return f'Для данного класса карт {self.plat} - Доступно страхование'

    def Warranty(self, note):
        if note == self.vc:
            return f'Для данного класса карт {self.plat}- Доступна расширеннная гарантия\n'

    def __str__(self):
        return super(MastercardPlatinum, self).__str__() + \
               f'Категория: {self.plat}\n'

class UnionPayDiamond(VisaClassic):
    def __init__(self, embossing, chip, nfc, magstripe, wallet, vc_class, vc_inf):
        super().__init__(embossing, chip, nfc, magstripe, wallet, vc_class)
        self.inf = vc_inf

    def VipService(self, note):
        if note == self.vc:
            return f'Для данного класса карт {self.inf} - Доступна VIP служба'

    def Concierge(self, note):
        if note == self.vc:
            return f'Для данного класса карт {self.inf} - Доступен Консьерж Сервис'

    def __str__(self):
        return super(UnionPayDiamond, self).__str__() + \
               f'Категория: {self.inf}\n'

card = PaymentCards('Индент-печать', True, True, True,'Issuer Wallet')
xag = VisaClassic('Эмбоссированная-печать', f'Rosan {1486731} 03/19', "PayWave", True, 'Apple/Google Pay', 'Visa Classic')
xau = AmexGold('Обратная-печать', f'Gemalto SGP U{1133365}A 1217', "ExpressPay", True, 'Samsung/PayRing', 2, 'AmeX Gold')
xpt = MastercardPlatinum('Вертикальная-печать', f'Alioth-{18073}-03-04/21', "PayPass", True, 'Garmin/Swatch Pay', 3, 'MC Platinum')
xin = UnionPayDiamond('Металлическая-печать', f'HB{18290415}-HICo', "QuickPass", True, 'Huawei/Xiaomi Pay', 4, 'UPI Diamond')

print(f'{xag}\n{xag.GlobalSupport("Visa Classic")}\n{xag.EmergencyAid("Visa Classic")}')
print(f'{xau}\n{xau.Discount(2)}\n{xau.MedicalAid(2)}')
print(f'{xpt}\n{xpt.Insurance(3)}\n{xpt.Warranty(3)}')
print(f'{xin}\n{xin.Concierge(4)}\n{xin.VipService(4)}')