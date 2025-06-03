import re
string = "Test1 Test2 Test3 Test4 Test5"
result = re.findall(r"Test", string)
print("Список усіх знайдених співпадінь:", result)
print("Кількість усіх співпадінь =", len(result))