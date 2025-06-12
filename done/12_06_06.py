import urllib.request
import json
import requests

def get_posts_urllib():
    url = 'https://jsonplaceholder.typicode.com/posts'
    with urllib.request.urlopen(url) as response:
        data = response.read().decode('utf-8')
        posts = json.loads(data)
    return posts

posts = get_posts_urllib()
print(f"Отримано {len(posts)} постів. Перший:\n{posts[0]}")



url = 'https://jsonplaceholder.typicode.com/posts'

def get_data(url):
    try:
        response = requests.get(url, timeout=10)
        print("✅ Успіх! Статус:", response.status_code)
        print(response.json()[0])
    except requests.exceptions.RequestException as e:
        print("❌ Помилка:", e)



def new_post(text_post, url):
    response = requests.post(url, json=text_post)
    print("Код відповіді:", response.status_code)
    print("Новий пост:", response.json())

text_post = {
    "title": "Мій тестовий пост",
    "body": "Це просто приклад.",
    "userId": 1
}

new_post(text_post, url)