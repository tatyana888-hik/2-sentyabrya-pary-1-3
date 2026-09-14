class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color

    def draw(self):
        print("Рисуется фигура")


class Line(Figure):
    def __init__(self, coords, width, color, length):
        super().__init__(coords, width, color)
        self.length = length

    def draw(self):
        print(f"Рисуется линия длиной {self.length}")


class Rect(Figure):
    def __init__(self, coords, width, color, height):
        super().__init__(coords, width, color)
        self.height = height

    def draw(self):
        print(f"Рисуется прямоугольник высотой {self.height}")


class Ellipse(Figure):
    def __init__(self, coords, width, color, radius):
        super().__init__(coords, width, color)
        self.radius = radius

    def draw(self):
        print(f"Рисуется эллипс с радиусом {self.radius}")


figures = [
    Line((10, 20), 2, "красный", 100),
    Rect((30, 40), 3, "синий", 50),
    Ellipse((50, 60), 4, "зелёный", 25)
]

for figure in figures:
    figure.draw()