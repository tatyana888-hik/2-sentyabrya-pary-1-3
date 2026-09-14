class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color


figure = Figure((10, 20), 5, "красный")

print("Координаты:", figure.coords)
print("Ширина:", figure.width)
print("Цвет:", figure.color)