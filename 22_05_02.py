# Завдання 2
class Contact:
    def __init__(self, surname: str, name: str, age: int, mob_phone: str, email: str):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self) -> str:
        return f"{self.name} {self.surname}, {self.mob_phone}"

    def send_message(self, message: str) -> None:
        print(f"Повідомлення для {self.name}: {message}")


class UpdateContact(Contact):
    def __init__(self, surname: str, name: str, age: int, mob_phone: str, email: str, job: str):
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_message(self) -> str:
        return f"{self.name} {self.surname} працює як {self.job}."


# Створення екземплярів
c1 = Contact("Іваненко", "Іван", 30, "+380501112233", "ivan@example.com")
c2 = UpdateContact("Петренко", "Олена", 28, "+380671234567", "olena@example.com", "дизайнер")

# Дослідження стану об'єктів
print("\n__dict__:")
print("Contact:", c1.__dict__)
print("UpdateContact:", c2.__dict__)

print("\n__base__:")
print("UpdateContact.__base__:", UpdateContact.__base__)

print("\n__bases__:")
print("UpdateContact.__bases__:", UpdateContact.__bases__)

# Методи
print("\nМетоди:")
print("Contact: get_contact ->", c1.get_contact())
c1.send_message("Вітаємо у системі!")

print("UpdateContact: get_contact ->", c2.get_contact())
print("UpdateContact: get_message ->", c2.get_message())
c2.send_message("Оновлено вашу вакансію.")

# Завдання 3: hasattr, getattr, setattr, delattr
print("\nЗавдання 3: Тестування функцій introspection")

for attr in ["surname", "name", "age", "mob_phone", "email", "job"]:
    print(f"\nПеревірка атрибуту '{attr}' у c2:")
    if hasattr(c2, attr):
        value = getattr(c2, attr)
        print(f"  ✓ Є атрибут '{attr}' з значенням: {value}")
        setattr(c2, attr, "Змінено")
        print(f"  ✏️  Нове значення '{attr}': {getattr(c2, attr)}")
        delattr(c2, attr)
        print(f"  🗑️  Атрибут '{attr}' видалено.")
        print("  ✓ Чи існує тепер:", hasattr(c2, attr))
    else:
        print(f"  ✗ Атрибут '{attr}' відсутній")

# Завдання 4: isinstance() та issubclass()
print("\nЗавдання 4: isinstance() та issubclass()")

# new_instances
contact_1 = Contact("Коваль", "Марія", 34, "+380501234567", "maria@example.com")
contact_2 = Contact("Шевченко", "Андрій", 41, "+380631234567", "andrii@example.com")
update_contact_1 = UpdateContact("Бондар", "Оксана", 29, "+380991112233", "oksana@example.com", "маркетолог")
update_contact_2 = UpdateContact("Ткаченко", "Юрій", 36, "+380671234567", "yurii@example.com", "інженер")

# isinstance
for obj in [contact_1, contact_2, update_contact_1, update_contact_2]:
    print(f"\nОб'єкт {obj.__class__.__name__}:")
    print("  isinstance Contact:", isinstance(obj, Contact))
    print("  isinstance UpdateContact:", isinstance(obj, UpdateContact))

# issubclass
print("\nПеревірка наслідування:")
print("issubclass(UpdateContact, Contact):", issubclass(UpdateContact, Contact))
print("issubclass(Contact, UpdateContact):", issubclass(Contact, UpdateContact))
