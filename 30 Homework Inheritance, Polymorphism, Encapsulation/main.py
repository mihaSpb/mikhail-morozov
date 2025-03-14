import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


if __name__ == "__main__":
    rectangle = Rectangle(3, 5)
    circle = Circle(8)

    print("Площадь прямоугольника:", rectangle.area())
    print("Площадь круга:", circle.area())
