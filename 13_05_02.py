class Review:
    def __init__(self, reviewer, text, rating):
        self.reviewer = reviewer
        self.text = text
        self.rating = rating  # Наприклад, від 1 до 5

    def __str__(self):
        return f"{self.reviewer} ({self.rating}/5): {self.text}"


class Book:
    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre
        self.reviews = []  # Список відгуків

    def add_review(self, review):
        if isinstance(review, Review):
            self.reviews.append(review)
        else:
            print("Можна додавати лише об'єкти класу Review.")

    def __str__(self):
        review_text = "\n".join(str(r) for r in self.reviews) if self.reviews else "Відгуків поки немає."
        return (f"Книга: '{self.title}'\n"
                f"Автор: {self.author}\n"
                f"Рік: {self.year}\n"
                f"Жанр: {self.genre}\n"
                f"Відгуки:\n{review_text}")

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year}, genre='{self.genre}')"


# Створення книги
book1 = Book("Ліна Костенко", "Маруся Чурай", 1979, "Історичний роман")

# Додавання відгуків
book1.add_review(Review("Оля", "Чудова книга, глибока та емоційна.", 5))
book1.add_review(Review("Ігор", "Трохи важко читати, але зміст неймовірний.", 4))

# Виведення
print(book1)
