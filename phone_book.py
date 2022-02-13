#from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import re
import csv

data_file = 'phonebook_raw.csv'

phone_number_pattern = '(8|\+7)?\s*(\(*)(\d{3})(\)*)(\s*|-)(\d{3})(\s*|-)(\d{2})(\s*|-)(\d{2})\s*(\(*)(\w\w\w\.)*\s*(\d{4})*(\))*'

phone_number_format = r'+7(\3)\6-\8-\10 \12\13'

def input_bd():

    with open(data_file, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

def input_contacts_list(contacts_list):
    data_contacts_list = list()

    for contact in contacts_list:
        working_data_contacts_list = list()
        persons_contact = ",".join(contact[:3])
        result = re.findall(r'(\w+)', persons_contact)

        while len(result) < 3:
            result.append('')
        working_data_contacts_list += result
        working_data_contacts_list.append(contact[3])
        working_data_contacts_list.append(contact[4])
        phone_number_pattern_result = re.compile(phone_number_pattern)
        phone_number_format_result = phone_number_pattern_result.sub(phone_number_format, contact[5])
        working_data_contacts_list.append(phone_number_format_result)
        working_data_contacts_list.append(contact[6])
        data_contacts_list.append(working_data_contacts_list)
    return data_contacts_list
    
def duplicates_persons_contacts(data_contacts_list):
    phone_book = dict()

    for contact in data_contacts_list:

        if contact[0] in phone_book:
            contact_value = phone_book[contact[0]]

            for i in range(len(contact_value)):

                if contact[i]:
                    contact_value[i] = contact[i]
        else:
            phone_book[contact[0]] = contact

    return list(phone_book.values())      

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV

def write_data(data_contacts_list):
    
    with open("phonebook.csv", "w", newline='', encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
# Вместо contacts_list подставьте свой список
        datawriter.writerows(data_contacts_list)

data_contacts_list = input_bd()

data_contacts_list_new = input_contacts_list(data_contacts_list)

contacts_of_book = duplicates_persons_contacts(data_contacts_list_new)

write_data(contacts_of_book)