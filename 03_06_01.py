import re
import os
import json

#Task 1

# Написати функцію, яка за допомогою регулярних виразів розбиває текст на окремі слова і знаходить частоту окремих слів.

# import re
#
# text = ('Написати функцію, яка виразів розбиває текст за допомогою і знаходить частоту окремих '
#         'слів регулярних виразів розбиває текст на окремі слова і знаходить частоту окремих слів.')
# pattern = r"[\s,]+"
# sep_words = re.split(pattern, text)
# print(sep_words)
# for word in sep_words:
#     words_count = sep_words.count(word)
#     print(f'{word}: {words_count}')


#Task 4
# result = re.findall(r"Test", string)
# print("Список усіх знайдених співпадінь:", result)
# print("Кількість усіх співпадінь =", len(result))

# Напишіть функцію, яка буде аналізувати текст, що надходить до неї, і виводити тільки унікальні слова на екран,
# загальну кількість слів і кількість унікальних слів.

# text = ('Написати функцію, яка виразів розбиває текст за допомогою і знаходить частоту окремих '
#         'слів регулярних виразів розбиває текст на окремі слова і знаходить частоту окремих слів.')
#
# def words_counter(text):
#     pattern = r"[\s,]+"
#     uniq_words = []
#     repeated_words = {}
#     sep_words = re.split(pattern, text)
#     for word in sep_words:
#         words_count = sep_words.count(word)
#         if words_count > 1:
#             repeated_words[word] = words_count
#
#         else:
#             uniq_words.append(word)
#     print('Uniq words: {uniq_words}'.format(uniq_words=uniq_words))
#     print(repeated_words)
#
# words_counter(text)

# Task 2

# Написати функцію, яка за допомогою регулярних виразів з файлу витягує дані про
# дату народження, телефон та електронну адресу. Дані потрібно записати до іншого файлу

# PATH = os.path.abspath(__file__ + '/..')
# file_name_read = os.path.join(PATH, 'CBS.log')
#
# def read_file():
#     PATH = os.path.abspath(__file__ + '/..')
#     file_name_read = os.path.join(PATH, 'CBS.log')
#     with open(file_name_read, "r", encoding="utf-8") as file:
#         text = file.read()
#     return text
#
# def extract_users(text):
#     patern_fullname = r"[A-ZА-ЯІЇҐЄ][a-zа-яіїґє]+(?:\s+[A-ZА-ЯІЇҐЄ][a-zа-яіїґє]+){1,2}"
#     patern_birthday = r"(?:Дата народження|Народився|День народження):?\s*([0-9]{1,2}[.\-/ ]?(?:[0-9]{1,2}|січня|лютого|березня|квітня|травня|червня|липня|серпня|вересня|жовтня|листопада|грудня)[.\-/ ]?[0-9]{2,4})"
#     patern_phone = r"(?:Телефон|Тел):?\s*([\+0-9\s().-]{10,})"
#     patern_email = r"(?:Електронна пошта|Email|Пошта):?\s*([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
#
#     user_blocks = re.split(r"\n\s*\d+\.\s", text)
#     user_data_list = []
#
#     for block in user_blocks:
#         if not block.strip():
#             continue
#
#         user = {}
#
#         fullname_match = re.search(patern_fullname, block)
#         birthday_match = re.search(patern_birthday, block, re.IGNORECASE)
#         phone_match = re.search(patern_phone, block)
#         email_match = re.search(patern_email, block)
#
#         user["fullname"] = fullname_match.group() if fullname_match else "не знайдено"
#         user["birthday"] = birthday_match.group(1) if birthday_match else "не знайдено"
#         user["phone"] = phone_match.group(1) if phone_match else "не знайдено"
#         user["email"] = email_match.group(1) if email_match else "не знайдено"
#
#         user_data_list.append(user)
#
#     return user_data_list
#
#
# def add_user_data(data_to_write):
#     file_name_write = 'users.txt'
#     mode = 'w' if not os.path.exists(file_name_write) else 'a'
#     with open(file_name_write, mode, encoding="utf-8") as f:
#         json.dump(data_to_write, f, ensure_ascii=False, indent=4)
#         f.write('\n')
#     if mode == 'w':
#         print(f"Файл '{file_name_write}' створено та записано перші дані.")
#     else:
#         print(f"Дані дописано у файл '{file_name_write}'.")
#
#
# text = read_file()
# data_to_write = extract_users(text)
# add_user_data(data_to_write)


#Task 3
# Користувач вводить з клавіатури пропозицію. Написати функцію, яка друкуватиме на екран останні 3 символи кожного слова.

# def print_last_3_chars(sentence: str):
#     words = sentence.split()
#     for word in words:
#         last_chars = word[-3:] if len(word) >= 3 else word
#         print(last_chars)
#
# user_input = input("Введіть пропозицію: ")
# print_last_3_chars(user_input)

#Task 5

# З клавіатури вводиться рядок, в якому є інформація про прізвище, ім'я, дату народження, електронну адресу та
# відгук про курси учня. Написати функцію, яка, використовуючи регулярні вирази, витягне дані з рядка і поверне словник.

#
# def parse_student_data(text):
#     data = {}
#     name_pattern = r"([A-ZА-ЯІЇҐЄ][a-zа-яіїґє]+)\s+([A-ZА-ЯІЇҐЄ][a-zа-яіїґє]+)"
#     date_pattern = r"\d{1,2}[./\s](?:[а-яА-ЯіІїЇґҐ]+|\d{1,2})[./\s]\d{4}"
#     email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
#     feedback_pattern = r"(?:відгук|відгук:)\s*(.+)$"
#     name_match = re.search(name_pattern, text)
#     if name_match:
#         data['surname'] = name_match.group(1)
#         data['name'] = name_match.group(2)
#
#     date_match = re.search(date_pattern, text)
#     if date_match:
#         data['birthday'] = date_match.group()
#
#     email_match = re.search(email_pattern, text)
#     if email_match:
#         data['email'] = email_match.group()
#
#     feedback_match = re.search(feedback_pattern, text, re.IGNORECASE)
#     if feedback_match:
#         data['feedback'] = feedback_match.group(1).strip()
#
#     return data
#
#
# def get_student_data_from_input() -> dict:
#     data = {}
#
#     data['surname'] = input("Введіть прізвище: ").strip()
#     data['name'] = input("Введіть ім'я: ").strip()
#     data['birthday'] = input("Введіть дату народження (наприклад, 22.11.1993): ").strip()
#     data['email'] = input("Введіть email: ").strip()
#     data['feedback'] = input("Залиште відгук про курси: ").strip()
#
#     return data
#
# user_data = get_student_data_from_input()
# print("\nОтримані дані:")
# for key, value in user_data.items():
#     print(f"{key.capitalize()}: {value}")


