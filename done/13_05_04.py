class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - {self.price}€"

    def __repr__(self):
        return f"Car(brand='{self.brand}', model='{self.model}', year={self.year}, price={self.price})"


class CarDealership:
    def __init__(self, name):
        self.name = name
        self.cars = []  # список авто на продаж

    def add_car(self, car):
        if isinstance(car, Car):
            self.cars.append(car)
        else:
            print("Додати можна лише автомобіль.")

    def sell_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Автомобіль {car} продано!")
        else:
            print("Такого автомобіля немає в наявності.")

    def list_cars(self):
        if not self.cars:
            return "Автомобілів немає в наявності."
        return "\n".join(str(car) for car in self.cars)



dealer = CarDealership("AutoLux")

car1 = Car("BMW", "X5", 2020, 45000)
car2 = Car("Tesla", "Model 3", 2022, 52000)
car3 = Car("Audi", "A6", 2019, 35000)

dealer.add_car(car1)
dealer.add_car(car2)
dealer.add_car(car3)

print("Автомобілі в наявності:")
print(dealer.list_cars())

dealer.sell_car(car2)

print("\nПісля продажу Tesla Model 3:")
print(dealer.list_cars())
