from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius)


shapes = [Circle(3), Square(4), Rectangle(6, 7), Pizza("Macroni", 4)]
for shape in shapes:
    print(f"The area of tha shape is {shape.area()}")
