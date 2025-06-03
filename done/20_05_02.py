'''Завдання 2

Напишіть програму-калькулятор, яка підтримує такі операції: додавання, віднімання, множення,
ділення та піднесення до ступеня. Програма має видавати повідомлення про помилку та продовжувати роботу
під час введення некоректних даних, діленні на нуль та зведенні нуля в негативний степінь.'''


def calculator():
    print("=== Калькулятор ===")
    print("Підтримувані операції: +, -, *, /, **")
    print("Введіть 'exit' щоб вийти")

    while True:
        try:
            first = input("Введіть перше число: ")
            if first.lower() == 'exit':
                print("Роботу завершено.")
                break
            first = float(first)

            op = input("Операція (+, -, *, /, **): ").strip()
            if op not in ['+', '-', '*', '/', '**']:
                print("❌ Невідома операція.")
                continue

            second = input("Введіть друге число: ")
            if second.lower() == 'exit':
                print("Роботу завершено.")
                break
            second = float(second)

            if op == '+':
                result = first + second
            elif op == '-':
                result = first - second
            elif op == '*':
                result = first * second
            elif op == '/':
                if second == 0:
                    raise ZeroDivisionError("Не можна ділити на нуль.")
                result = first / second
            elif op == '**':
                if first == 0 and second < 0:
                    raise ValueError("Не можна зводити 0 в від’ємний степінь.")
                result = first ** second

            print(f"✅ Результат: {result}")

        except ValueError as ve:
            print(f"❌ Помилка значення: {ve}")
        except ZeroDivisionError as zde:
            print(f"❌ Помилка ділення: {zde}")
        except Exception as e:
            print(f"❌ Невідома помилка: {e}")

calculator()
