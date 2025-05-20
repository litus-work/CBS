'''Завдання 4

Опишіть свій клас винятку. Напишіть функцію, яка викидатиме цей виняток, якщо користувач введе певне значення,
і перехопіть цей виняток під час виклику функції.'''


class ForbiddenValueError(Exception):
    """Клас винятку для забороненого значення."""
    def __init__(self, value):
        super().__init__(f"❌ Заборонене значення: '{value}'!")
        self.value = value

def check_input(user_input: str):
    forbidden_values = ["badword", "123", "exit"]
    if user_input.lower() in forbidden_values:
        raise ForbiddenValueError(user_input)
    else:
        print(f"✅ Ви ввели: {user_input}")

def main():
    while True:
        try:
            value = input("Введіть щось (або 'stop' для виходу): ")
            if value.lower() == "stop":
                print("Програма завершена.")
                break
            check_input(value)
        except ForbiddenValueError as fe:
            print(fe)
        except Exception as e:
            print(f"Інша помилка: {e}")

main()
