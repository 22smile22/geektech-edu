import re

my_text = 'Vasya, 1998, vasya@gmail.com, 4000$, male* ' \
          'Adilet, 1997, adilet@intel.com, 50089750$, male* ' \
          'Aidana, 2000 aidana@yandex.ru, 890976$, female% ' \
          'Aman, 1999, aman@mail.ru, 789$, male* ' \
          'Regina, 1999 regina@yahoo.ru 69$, female% ' \
          'Lol, 6789, lol@gmail.com 9087$, none? '

"""
\d -- Он ищет подряд стоящие ЧИСЛА [0-9]
\D -- Он ищет любые, но не числа
\w -- Ищет любой алфавитный символ [A-Z a-z]
\W -- Любой не алфавитный символ
\s -- Ищет пробелы
\S -- специальные символы
"""

# what_search = r'\d{4}'
# what_search = r'\w+'
# what_search = r'\D{2}'
# what_search = r'\W{2}'
# what_search = r'\s'
# what_search = r'\S{3}'
# what_search = r'[A-Z]'
# what_search = r'[a-z]'
# what_search = r'[A-Z][a-z]+'
# what_search = r'[a-z]+'


# what_search = r'\d+[$]'
# what_search = r'\w+[%*?]'

# what_search = r'@\w+.\w+'
# what_search = r'@\w+\S\w+'

# what_search = r'[5-9]'
# what_search = r'[5-9]'



# what_search = r'Vasya'
# what_search = r'Lol'
# what_search = r'aman'
# what_search = r'@mail.ru'
# what_search = r'@'
# results = re.match(what_search, my_text)
# results = re.search(what_search, my_text)
# results = re.findall(what_search, my_text)
# print(results)
# print(f'Годы рождения: {results}')
""""------------------------------"""

file_path = 'demo_mock_data.txt'
result_file_path = 'results.txt'

file_reader = open(file_path, mode='r', encoding='Latin-1')
result_file = open(result_file_path, mode='w', encoding='Latin-1')
my_text_file = file_reader.read()

what_search = r'[\w_-]+(?!jbullochj5)@(?!so-net)(?!intel)(?!yahoo)(?!amazon)[\w+_-]+.[\w+.]+'
results = re.findall(what_search, my_text_file)

for item in results:
    print(item)
    result_file.write(item + '\n')

print(f'Total results of file: {str(len(results))}')

