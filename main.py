import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# 1.поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно.
# В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
# 2. привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой:
# +7(999)999-99-99 доб.9999
# 3. объединить все дублирующиеся записи о человеке в одну.
# TODO 1: выполните пункты 1-3 ДЗ
# rr = re.sub(r'[()]', str(contacts_list))
# pprint(rr)
contacts_slit = re.compile(r'(\+7|8)+\s*\(*(\d{3})\)*[-\s]?(\d{3})[-\s]?(\d{2})[\s-]?(\d+)')
text_2 = contacts_slit.sub('+7(\\2)-\\3-\\4-\\5', str(contacts_list))
pprint(text_2)
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(text_2)
