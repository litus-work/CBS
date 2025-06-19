import json

users = [
    {"name": "Іван", "age": 30, "email": "ivan@example.com"},
    {"name": "Олена", "age": 25, "email": "olena@example.com"}
]

with open("users.json", "w", encoding="utf-8") as f:
    json.dump(users, f, indent=2, ensure_ascii=False)



with open("users.json", "r", encoding="utf-8") as f:
    loaded_users = json.load(f)

print("Дані з JSON-файлу:")
for user in loaded_users:
    print(user)