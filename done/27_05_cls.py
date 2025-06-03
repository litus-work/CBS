# Створіть систему керуванян списком запрошених користувач має меню з наступними пунктами:
# 1 - Переглянути список запрошених
# 2 - Додати запрошеного
# 3 - Вихід.
# При введені 1 користувач має побачити кожного запрошеного з його номером в терміналі виведеног ов стовпчик.
# При натисканні 2 користувач має ввести ім'я запрошеного його треба записати в файл.
# В файлі імена запрошених мають зберігатис таким чином щоб кожне ім'я було з нового рядку.
# Переконайтесь що код працює правильно за всіх обстави


import os

PATH = os.path.abspath(__file__ + '/../')
file_name = os.path.join(PATH, 'guests.txt')
num_queue = 0


def get_guests():
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            data = f.read()
    else:
        open(file_name, 'x').close()
        data = ''
    return data

while True:
    choice = input("1 - Get guest names, 2 - Add guest name, 3 - exit: ")
    match choice:
        case "1":
            print(get_guests())
        case "2":
            guest = str(input())
            with open(file_name, 'a') as f:
                if not get_guests():


                    f.write(f'{num_queue+1}: {guest}')
                else:
                    # num_queue = +1
                    f.write(f'{num_queue+1}: {guest}')
        case "3":
            break
