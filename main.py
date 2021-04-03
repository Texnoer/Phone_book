import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


def list_update(contacts_list):
    new_list =[]
    for contacts in contacts_list:
        new_data = []
        name = ",".join(contacts[0:3])
        result = re.findall(r'(\w+)', name)
        while len(result) < 3:
            result.append('')
        new_data += result
        new_data.append(contacts[3])
        new_data.append(contacts[4])
        phone_pattern = re.compile(patteren)
        changed_phone = phone_pattern.sub(sub_patteren, contacts[5])
        new_data.append(changed_phone)
        new_data.append(contacts[6])
        new_list.append(new_data)
    return new_list


# удаление дубликата
def remove_duplicates(new_list):
    phone_book = {}
    for contact in new_list:
        if contact[0] in phone_book:
            contact_data = phone_book[contact[0]]
            for i in range(len(contact_data)):
                if contact[i]:
                    contact_data[i] = contact[i]
        else:
            phone_book[contact[0]] = contact
    return list(phone_book.values())


# код для записи файла в формате CSV
def write_contact(new_list):
    with open("phonebook.csv", "w", encoding='utf-8') as f:
      datawriter = csv.writer(f, delimiter=',')
      datawriter.writerows(new_list)


if __name__ == '__main__':
    patteren = r'(\+7|8)+\s*\(*(\d{3})\)*[-\s]?(\d{3})[-\s]?(\d{2})[\s-]?(\d+)\s*(\(*)(\w\w\w\.)*\s*(\d{4})*(\))*'
    sub_patteren = r'+7(\2)-\3-\4-\5 \7\8'
    up_new_list = list_update(contacts_list)
    contact_book = remove_duplicates(up_new_list)
    write_contact(contact_book)
    print(contact_book)

