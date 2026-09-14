class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color


class Line(Figure):
    def __init__(self, coords, width, color, length):
        super().__init__(coords, width, color)
        self.length = length


class Rect(Figure):
    def __init__(self, coords, width, color, height):
        super().__init__(coords, width, color)
        self.height = height


class Ellipse(Figure):
    def __init__(self, coords, width, color, radius):
        super().__init__(coords, width, color)
        self.radius = radius


line = Line((10, 20), 2, "красный", 100)
rect = Rect((30, 40), 3, "синий", 50)
ellipse = Ellipse((50, 60), 4, "зелёный", 25)


print("Линия:", line.coords, line.width, line.color, line.length)
print("Прямоугольник:", rect.coords, rect.width, rect.color, rect.height)
print("Эллипс:", ellipse.coords, ellipse.width, ellipse.color, ellipse.radius)