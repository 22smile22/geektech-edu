"""
Группа  Geektech 14Py - студент Акылбек Мамбетакунов
Месяц 2 - ООП. Домашнее задание № 5.

Условия Задания :
1. Файл MOCK_DATA, надо проанализировать сначала
2. Используя модуль re Из файла MOCK_DATA вытащить хаотичные данные и
упорядочить по пунктам (ФИО , почта , расширение файла, код цвета)
3. Использую метод работы с файлом распределить в новые файлы , в
MOCK_DATA есть 4 разделений на ФИО, почту , расширение , код цвета
4. В итоге у вас будет 4 файла , каждый со своими данными

Доп Задание :
1. Сделать все в классах

\d -- Он ищет подряд стоящие ЧИСЛА [0-9]
\D -- Он ищет любые , но не числа
\w -- Ищет любой алфавитный символ [A-Z a-z]
\W -- любой не алфавитный символ
\s -- Ищет пробелы
\S -- специальные символы

"""

import re

def write(reg_compare, file_write):
    for object in reg_compare:
        print(object)
        file_write.write(object + '\n')


file_path = 'MOCK_DATA.txt'

email = 'email.txt'
personal = 'personal.txt'
expand = 'expand.txt'
color = 'color.txt'

file_read = open(file_path, mode='r', encoding='UTF-8')

email_file = open(email, mode='w', encoding='UTF-8')
personal_file = open(personal, mode='w', encoding='UTF-8')
expand_file = open(expand, mode='w', encoding='UTF-8')
color_file = open(color, mode='w', encoding='UTF-8')

text_file = file_read.read()

email_file_search = r'[\w_-]+@[\w_-]+.[\w.]+'
email_result = re.findall(email_file_search, text_file)
personal_file_search = r"[A-Z][a-z_-]+[\s][de\sA-Z'\s]+[a-zA-Z]+"
personal_result = re.findall(personal_file_search, text_file)
expand_file_search = r'[A-Z\s]+[a-zA-Z]+[.][a-z\d]+'
expand_result = re.findall(expand_file_search, text_file)
color_file_search = r'#......'
color_result = re.findall(color_file_search, text_file)


write(email_result, email_file) # email.txt
print(f'Name of file: {email}\n'
      f'Total results of file: {str(len(email_result))}\n')
write(personal_result, personal_file) # personal.txt
print(f'Name of file: {personal}\n'
      f'Total results of file: {str(len(personal_result))}\n')
write(expand_result, expand_file) # expand.txt
print(f'Name of file: {expand}\n'
      f'Total results of file: {str(len(expand_result))}\n')
write(color_result, color_file) # color.txt
print(f'Name of file: {color}\n'
      f'Total results of file: {str(len(color_result))}\n')