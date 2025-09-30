import math
from .figure import Figure
from .color import FigureColor

class Circle(Figure):

    def __init__(self, radius, color):
        self.radius = radius
        self.color_obj = FigureColor()
        self.color_obj.color = color
        self.name = "Круг" 

    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return "{} {} цвета радиусом {} площадью {:.2f}.".format(
            self.name,
            self.color_obj.color,
            self.radius,
            self.area()
        )
