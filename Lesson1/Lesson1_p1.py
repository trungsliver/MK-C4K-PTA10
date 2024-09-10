class Car():
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - ${self.price}"
    
class Student():
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return f'{self.name} - {self.age} tuổi - {self.score} điểm'