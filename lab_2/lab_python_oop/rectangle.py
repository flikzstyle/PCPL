from .figure import Figure
from .color import FigureColor

class Rectangle(Figure):

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color_obj = FigureColor()
        self.color_obj.color = color
        self.name = "Прямоугольник"

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "{} {} цвета шириной {} и высотой {} площадью {}.".format(
            self.name,
            self.color_obj.color,
            self.width,
            self.height,
            self.area()
        )
