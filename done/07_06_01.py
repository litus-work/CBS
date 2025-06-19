import time



def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        fmt = time.gmtime(end - start)
        strf = time.strftime("%T", fmt)
        print(strf)
        return result

    return wrapper




@timer
def calculator():
    print("=== Калькулятор ===")
    print("Підтримувані операції: +, -, *, /, **")
    print("Введіть 'exit' щоб вийти")


    try:
        first = input("Введіть перше число: ")
        if first.lower() == 'exit':
            print("Роботу завершено.")
        first = float(first)

        op = input("Операція (+, -, *, /, **): ").strip()
        if op not in ['+', '-', '*', '/', '**']:
            print("❌ Невідома операція.")

        second = input("Введіть друге число: ")
        if second.lower() == 'exit':
            print("Роботу завершено.")
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