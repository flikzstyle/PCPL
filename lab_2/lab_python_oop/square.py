from .rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, side, color):
        super().__init__(side, side, color)
        self.name = "Квадрат"

    def __repr__(self):
        return "{} {} цвета со стороной {} площадью {}.".format(
            self.name,
            self.color_obj.color,
            self.width,
            self.area()
        )
