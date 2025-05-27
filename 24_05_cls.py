



# def marks_generator(students: dict, subjects: dict):
#     for subject_id, subject_name in subjects.items():  # Проходимся по всем предметам
#         list_marks = []
#         for marks_dict in students.values():  # Все данные по каждому студенту
#             # Извлекаем оценки по текущему предмету:
#             list_marks.extend([mark_data['mark'] for mark_data in marks_dict[subject_id]])
#         yield (subject_name, list_marks)
#
# marks_by_subjects = {
#     subject_name: marks
#     for subject_name, marks in marks_generator(dict_students, subjects)
# }

# Task№1

# Створіть генератор аналог enumerate він приймає список і повертає одразу індекс елементе та його значення.
# при виконанні не можна використовувати enumerate

# def lis_generator(list_1: list):
#     index = 0
#     for value in list_1:
#         yield(index, value)
#         index+=1
#
#
# list_1 = [1,2,3,4,5,6,7,8,9]
# value_by_index = {
#     index: value
#     for index, value in lis_generator(list_1)
# }
#
# print(value_by_index)

# Task№2
# Напиши генератор compress_sequence(iterable), який пропускає повторення однакових елементів у
# вхідній послідовності підряд і повертає лише перші появи кожної нової серії елементів.
#
# def compress_sequence(iterable: list):
#     index = 0
#     prev_value = 0
#     for value in iterable:
#         if prev_value != value:
#             index += 1
#             yield (index, value)
#             prev_value = value
#         else:
#             value_1 = prev_value
#             index += 1
#             yield (index, value_1)
#             prev_value = value
# 
#
#
#
#
# iterable = [1,2,3,3,3,4,5,5,5,5,6,2,2,2,2,7,8,9]
# value_by_index = {
#     index: value
#     for index, value in compress_sequence(iterable)
# }
#
# print(value_by_index)


# Вхідна послідовність
iterable = [1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 2, 2, 2, 7, 8, 9]

def compress_sequence(iterable: list):
    prev_value = object()  # використовуємо унікальний об'єкт
    for value in iterable:
        if prev_value != value:
            yield value
            prev_value = value

# Генеруємо список без повторень підряд
list_1 = list(compress_sequence(iterable))
print(list_1)
