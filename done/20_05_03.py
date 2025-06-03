'''Завдання 3

Опишіть клас співробітника, який вміщує такі поля: ім'я, прізвище, відділ і рік початку роботи.
Конструктор має генерувати виняток, якщо вказано неправильні дані.
Введіть список працівників із клавіатури. Виведіть усіх співробітників, які були прийняті після цього року.'''

class Employee:
    def __init__(self, first_name: str, last_name: str, department: str, start_year: int):
        if not first_name or not last_name or not department:
            raise ValueError("Ім'я, прізвище та відділ не можуть бути порожніми.")
        if not (1900 <= start_year <= 2100):
            raise ValueError("Рік початку роботи має бути в діапазоні 1900-2100.")

        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.start_year = start_year

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Відділ: {self.department}, Початок роботи: {self.start_year}"


def main():
    employees = []
    print("Введення співробітників (введіть 'stop' для зупинки):")

    while True:
        try:
            first = input("Ім'я: ")
            if first.lower() == 'stop':
                break

            last = input("Прізвище: ")
            dept = input("Відділ: ")
            year = input("Рік початку роботи: ")

            if year.lower() == 'stop':
                break

            employee = Employee(first, last, dept, int(year))
            employees.append(employee)
            print("✅ Співробітника додано.\n")
        except ValueError as ve:
            print(f"❌ Помилка: {ve}")
        except Exception as e:
            print(f"❌ Невідома помилка: {e}")

    try:
        filter_year = int(input("Вивести співробітників, які були прийняті після року: "))
        print("\n📋 Список співробітників:")
        filtered = [emp for emp in employees if emp.start_year > filter_year]
        if not filtered:
            print("Немає співробітників після вказаного року.")
        else:
            for emp in filtered:
                print(emp)
    except ValueError:
        print("❌ Некоректне значення року.")

main()
