import math
from datetime import datetime

def safe_get_value(obj, default=0.0):
    if isinstance(obj, dict):
        return obj.get('value', default)
    elif isinstance(obj, (int, float, str)):
        return obj
    return default

data = items[0]['json']
prediction = data.get('document', {}).get('inference', {}).get('prediction', {})

# Общая информация
receipt_date = safe_get_value(prediction.get('date'))
receipt_number = safe_get_value(prediction.get('receipt_number'))
supplier = safe_get_value(prediction.get('supplier_name'))
category = safe_get_value(prediction.get('category'))
total_amount = data.get('document', {}).get('inference', {}).get('prediction', {}).get('total_amount', {}).get('value', 0.0)
currency = prediction.get('locale', {}).get('currency', 'EUR')
line_items = prediction.get('line_items', [])

# Сумма по строкам
calculated_total = sum(safe_get_value(item.get('total_amount')) for item in line_items)

# Разница
diff_amount = round(abs(calculated_total - total_amount), 2)
is_equal = math.isclose(calculated_total, total_amount, abs_tol=0.01)

# Уникальное время для идентификации
now = int(datetime.now().timestamp())

# Если нет позиций вообще
if not line_items:
    return [{
        "json": {
            "Row_id": now * 100,
            "Дата": receipt_date,
            "Номер чека": receipt_number,
            "Поставщик": supplier,
            "Категория": category,
            "Сумма по чеку": total_amount,
            "Сумма по строкам": calculated_total,
            "Разница в сумме": diff_amount,
            "Совпадают ли суммы": is_equal,
            "Валюта": currency,
            "Название товара": "❌ Позиции не распознаны",
            "Цена": 0,
            "Кол-во": 0
        }
    }]

# Если позиции есть
output = []
for i, item in enumerate(line_items):
    output.append({
        "Row_id": now * 100 + i,
        "Дата": receipt_date,
        "Номер чека": receipt_number,
        "Поставщик": supplier,
        "Категория": category,
        "Сумма по чеку": total_amount,
        "Сумма по строкам": calculated_total,
        "Разница в сумме": diff_amount,
        "Совпадают ли суммы": is_equal,
        "Валюта": currency,
        "Название товара": safe_get_value(item.get('description'), 'Без названия'),
        "Цена": safe_get_value(item.get('total_amount')),
        "Кол-во": safe_get_value(item.get('quantity'), 1)
    })

return [{ "json": row } for row in output]
