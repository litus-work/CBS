#Task1

# def reverse_generator(sequence: list):
#     index = len(sequence) - 1
#     while index >= 0:
#         yield sequence[index]
#         index -= 1
#
# my_list = [1, 2, 3, 4, 5]
#
# for item in reverse_generator(my_list):
#     print(item, end=" ")

#Task2
#Ver_1
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# even_squares = (x**2 for x in numbers if x % 2 == 0)
#
# print(list(even_squares))

#Ver_2
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# even_squares = []
# for x in numbers:
#     if x % 2 == 0:
#         even_squares.append(x**2)
#
# print(even_squares)

#Task3


def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator(n: int):
    count = 0
    number = 2
    while count < n:
        if is_prime(number):
            yield number
            count += 1
        number += 1

n = 10
primes = list(prime_generator(n))
print(f"Перші {n} простих чисел:", primes)