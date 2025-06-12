import requests


def http_client(url, method, data: dict = None):
    method = method.upper()

    try:
        if method == 'GET':
            response = requests.get(url, params=data)
        elif method == 'POST':
            response = requests.post(url, json=data)
        elif method == 'PUT':
            response = requests.put(url, json=data)
        elif method == 'DELETE':
            response = requests.delete(url, json=data)
        elif method == 'PATCH':
            response = requests.patch(url, json=data)
        else:
            print("Невідомий метод:", method)
            return

        print(f"Статус код: {response.status_code}")
        print("Заголовки:")
        for key, value in response.headers.items():
            print(f"  {key}: {value}")

        print("\nТіло відповіді:")
        print(response.text)

    except requests.RequestException as e:
        print("Помилка запиту:", e)


http_client(
    url='https://jsonplaceholder.typicode.com/posts',
    method='GET'
)

http_client(
    url='https://jsonplaceholder.typicode.com/posts',
    method='POST',
    data={
        "title": "Test post",
        "body": "Це тіло запиту",
        "userId": 1
    }
)