class Book:
    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year}), Genre: {self.genre}"

    def __repr__(self):
        return f"Book(author='{self.author}', title='{self.title}', year={self.year}, genre='{self.genre}')"

book1 = Book("Джордж Орвелл", "1984", 1949, "Антиутопія")
book2 = Book("Леся Українка", "Лісова пісня", 1911, "Драма")
book3 = Book("Дан Браун", "Код да Вінчі", 2003, "Детектив")

# Приклади виведення
print(str(book1))  # Людське читання
print(repr(book2)) # Технічне представлення
print(book3)       # Автоматично викликає __str__
