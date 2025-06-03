class GraphicObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Малюю графічний об'єкт на позиції ({self.x}, {self.y})")


class Rectangle(GraphicObject):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def draw(self):
        print(f"Малюю прямокутник розміром {self.width}x{self.height} на позиції ({self.x}, {self.y})")


class Clickable:
    def click(self):
        print("Обробка натискання...")  # Заглушка


class Button(Rectangle, Clickable):
    def __init__(self, x, y, width, height, text):
        super().__init__(x, y, width, height)
        self.text = text

    def draw(self):
        print(f"[{self.text}] кнопка розміром {self.width}x{self.height} на позиції ({self.x}, {self.y})")

    def click(self):
        print(f"Кнопку '{self.text}' натиснуто!")


rect = Rectangle(10, 20, 100, 50)
rect.draw()

btn = Button(30, 40, 120, 60, "OK")
btn.draw()
btn.click()
