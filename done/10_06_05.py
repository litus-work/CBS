numbers = list(range(1, 11))  # [1..10]

odd = filter(lambda x: x % 2 != 0, numbers)

squares = map(lambda x: x ** 2, odd)
print(f'Начальный спитсок: {list(numbers)}')
# print(f'Отфильтрованный спитсок: {list(odd)}')
print(f'Квадраты нечетных чисел: {list(squares)}')

# Чому, якщо виводимо:
# print(f'Отфильтрованный спитсок: {list(odd)}')
# не працюэ  print(f'Квадраты нечетных чисел: {list(squares)}')

