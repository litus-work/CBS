import random

with open("numbers.txt", "w") as file:
    for _ in range(10000):
        number = random.uniform(0, 1000)
        file.write(f"{number}\n")

total = 0.0

with open("numbers.txt", "r") as file:
    for line in file:
        total += float(line.strip())

print(f"Сума всіх чисел: {total}")