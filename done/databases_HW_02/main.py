from datetime import datetime, timedelta
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os
load_dotenv()

connect = psycopg2.connect(
    host=os.environ.get("DB_HOST"),
    database=os.environ.get("DB_NAME"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    port=os.environ.get("DB_PORT"),
)

cursor = connect.cursor(cursor_factory=RealDictCursor)
connect.autocommit = True
CURENT_DATE = datetime.now()

def create_table_products():
    query = '''CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL UNIQUE,
        price DECIMAL(10,2) NOT NULL,
        description VARCHAR(200) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        published_at timestamp,
        country VARCHAR(20) NOT NULL
    );
    '''
    cursor.execute(query)

def create_table_orders():
    query = '''CREATE TABLE IF NOT EXISTS orders (
        id SERIAL PRIMARY KEY,
        amount DECIMAL(10,2) NOT NULL,
        count_products INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    '''
    cursor.execute(query)

def insert_data_products(name: str, price: float, description: str, published_at: str, country: str):
    query = '''
        INSERT INTO products (name, price, description, published_at, country)
        VALUES (%s, %s, %s, %s, %s);
    '''
    cursor.execute(query, (name, price, description, published_at, country))

def insert_data_orders(amount, count_products):
    query = '''
        INSERT INTO orders (amount, count_products)
        VALUES (%s, %s);
    '''
    cursor.execute(query, (amount, count_products))

def get_all_data(table_name: str, limit: Optional[int] = None):
    if limit is not None and limit > 0:
        query = f"SELECT * FROM {table_name} LIMIT {limit};"
    else:
        query = f"SELECT * FROM {table_name};"
    cursor.execute(query)
    return cursor.fetchall()

def delete_data(table_name: str, row_id: int):
    query = f"DELETE FROM {table_name} WHERE id = %s;"
    cursor.execute(query, (row_id,))

def custom_query(query):
    cursor.execute(query)
    return cursor.fetchall()


def main():
    create_table_products()
    create_table_orders()
    while True:
        choice = int(input("1-Add data\n2-View data\n3-Delete data\n4-Editional operations with tables\n5-Exit\nChoose an option: "))
        match choice:
            case 1:
                table_name = input("Enter table name: ")
                if table_name == "products":
                    name = input("Enter name: ")
                    price = float(input("Enter price: "))
                    description = input("Enter description: ")
                    published_at = input("Enter published_at: ")
                    country = input("Enter country: ")
                    insert_data_products(name, price, description, published_at, country)
                    print("Data added successfully into table products.")
                elif table_name == "orders":
                    amount = float(input("Enter amount: "))
                    count_products = int(input("Enter count_products: "))
                    insert_data_orders(amount, count_products)
                    print("Data added successfully into table orders.")
                else:
                    print("Invalid table name.")
                    continue

            case 2:
                name_table = input("Enter table name: ")
                limit = input("Enter limit or press ENTER to see all data: ")
                if limit:
                    data = get_all_data(name_table, int(limit))
                else:
                    data = get_all_data(name_table, limit=None)
                for row in data:
                    print(dict(row))
            case 3:
                name_table = input("Enter table name: ")
                row_id = int(input("Enter row ID to delete: "))
                delete_data(name_table, row_id)
                print("Row has been deleted successfully.")

            case 4:
                choice_editional = int(input("Оберіть таблицю:\n"
                                   "1- products\n"
                                   "2- orders\n"
                                   "3- Exit\n"
                                   "Choose an option: "))

                match choice_editional:
                    case 1:
                        choice_operetion = int(input("Оберіть операцію над таблицею products\n"
                            "1- Отримати продукти які були опубліковані в певну дату\n"
                            "2- Отримати продукти які були опубліковані сьогодні\n"
                            "3- Отримати продукти ціна яких більше \ менше ніж\n"
                            "4- Отримати продукти за назвою\n"
                            "5- Отримати продукти за країної виробником\n"
                            "6- Отримати кількість продуктів вироблених в кожній країні\n"
                            "7- Exit\n"
                            "Choose an option: "))

                        match choice_operetion:
                            case 1:
                                date_input = input("Введіть дату (у форматі YYYY-MM-DD)")
                                try:
                                    current_date = datetime.strptime(date_input, "%Y-%m-%d").date()
                                    query = f"SELECT * FROM products WHERE published_at = '{current_date}';"
                                    data = custom_query(query)
                                except ValueError:
                                    print("❌ Невірний формат дати. Введіть у форматі YYYY-MM-DD.")
                                for row in data:
                                    print(dict(row))

                            case 2:
                                current_date = datetime.now().date()
                                query = f"SELECT * FROM products WHERE published_at = '{current_date}';"
                                data = custom_query(query)
                                if not data:
                                    print(f"❌ Жодного товару не знайдено.")
                                else:
                                    for row in data:
                                        print(dict(row))

                            case 3:
                                try:
                                    print("Введіть ціновий діапазон в якому ви шукаєте товар:")
                                    price_min_input = float(input("Найменша ціна: "))
                                    price_max_input = float(input("Найбільша ціна: "))
                                    query = f"SELECT * FROM products WHERE price BETWEEN {price_min_input} AND {price_max_input};"
                                    data = custom_query(query)
                                except ValueError:
                                    print("❌ Немає товарів в заданому діапазоні")
                                for row in data:
                                    print(dict(row))

                            case 4:
                                name_product_input = str(input("Введіть назву товару який ви шукаєте: "))
                                query = f"SELECT * FROM products WHERE name = '{name_product_input}';"
                                data = custom_query(query)
                                if not data:
                                    print(f"❌ Товару з назвою «{name_product_input}» не знайдено.")
                                else:
                                    for row in data:
                                        print(dict(row))

                            case 5:
                                country_product_input = str(input("Введіть назву країни: "))
                                query = f"SELECT * FROM products WHERE country = '{country_product_input}';"
                                data = custom_query(query)
                                if not data:
                                    print(f"❌ Товару з країни «{name_product_input}» не знайдено.")
                                else:
                                    for row in data:
                                        print(dict(row))

                            case 6:
                                print("Кількість продуктів вироблених в кожній країні:")
                                query = f"SELECT country, count(id) FROM products group by country order by count(id) desc;"
                                data = custom_query(query)

                                if not data:
                                    print(f"❌ Жодного товару не знайдено.")
                                else:
                                    for row in data:
                                        print(dict(row))



                    case 2:
                        choice_operetion = int(input("Оберіть операцію над таблицею orders\n"
                            "1- Отримати найдорожче \ найдешевше замовлення\n"
                            "2- Отримати замовлення зроблені сьогодні\n"
                            "3- Отримати замовлення за цей місяць\n"
                            "4- Отримати суму всіх замовлень\n"
                            "5- Отримати середній чек\n"
                            "6- Отримати Кількість товарів проданих за цей місяць\n"
                            "7- Отримати суму замовлень за цей місяць\n"
                            "8- Exit\n"
                            "Choose an option: "))

                        match choice_operetion:
                            case 1:
                                print("Найдорожче \ найдешевше замовлення:")
                                query = f"SELECT min(amount), max(amount) FROM orders;"
                                data = custom_query(query)

                                if not data:
                                    print(f"❌ Жодного товару не знайдено.")
                                else:
                                    for row in data:
                                        print(dict(row))

                            case 2:

                                query = f"SELECT * FROM orders WHERE created_at between '{CURENT_DATE.date()}' and '{CURENT_DATE.date() + timedelta(days=1)}';"
                                data = custom_query(query)
                                if not data:
                                    print(f"❌ Жодного товару не знайдено.")
                                else:
                                    for row in data:
                                        print(dict(row))

                            case 3  :
                                query = f"SELECT * FROM orders WHERE EXTRACT(MONTH FROM created_at) = {CURENT_DATE.month} and EXTRACT(YEAR FROM created_at) = {CURENT_DATE.year}; ;"
                                data = custom_query(query)
                                if not data:
                                    print(f"❌ Жодного товару не знайдено.")
                                else:
                                    for row in data:
                                        print(dict(row))

                            case 4:
                                query = f"SELECT sum(amount) FROM orders;"
                                data = custom_query(query)
                                if not data:
                                    print(f"❌ Жодного товару не знайдено.")
                                else:
                                    for row in data:
                                        print(dict(row))

                            case 5:
                                query = f"SELECT avg(amount) FROM orders;"
                                data = custom_query(query)
                                if not data:
                                    print(f"❌ Жодного товару не знайдено.")
                                else:
                                    for row in data:
                                        print(dict(row))

                            case 6:
                                query = f"SELECT EXTRACT(MONTH FROM created_at) as month, EXTRACT(YEAR FROM created_at) as year, sum(count_products) FROM orders GROUP BY EXTRACT(MONTH FROM created_at), EXTRACT(YEAR FROM created_at)  HAVING EXTRACT(MONTH FROM created_at) = {CURENT_DATE.month} and EXTRACT(YEAR FROM created_at) = {CURENT_DATE.year};"
                                data = custom_query(query)
                                if not data:
                                    print(f"❌ Жодного товару не знайдено.")
                                else:
                                    for row in data:
                                        print(dict(row))

                            case 7:
                                query = f"SELECT EXTRACT(MONTH FROM created_at) as month, EXTRACT(YEAR FROM created_at) as year, sum(amount) FROM orders GROUP BY EXTRACT(MONTH FROM created_at), EXTRACT(YEAR FROM created_at)  HAVING EXTRACT(MONTH FROM created_at) = {CURENT_DATE.month} and EXTRACT(YEAR FROM created_at) = {CURENT_DATE.year};"
                                data = custom_query(query)
                                if not data:
                                    print(f"❌ Жодного товару не знайдено.")
                                else:
                                    for row in data:
                                        print(dict(row))

            case 5:
                print("Exiting...")
                break
main()