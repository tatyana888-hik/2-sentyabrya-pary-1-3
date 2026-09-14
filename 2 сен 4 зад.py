class Graph:
    def __init__(self, x=0, y=0, scale=1):
        self._x = x
        self._y = y
        self._scale = scale

    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    def change_scale(self, factor):
        self._scale *= factor

    def show(self):
        print(f"Координаты: ({self._x}, {self._y}), масштаб: {self._scale}")


graph1 = Graph(10, 20, 1)
graph2 = Graph(30, 40, 1)
graph3 = Graph(50, 60, 1)

graph1.move(5, -10)
graph2.change_scale(2)

graph1.show()
graph2.show()
graph3.show()