class Movement:
    """Класс Движения по местности"""
    def __init__(self):
        self.coord_x = 0
        self.coord_y = 0

    def set_coord_x(self, x):
        self.coord_x += x

    def set_coord_y(self, y:float):
        self.coord_y += y

    def get_coord_x(self):
        return self.coord_x

    def get_coord_y(self):
        return self.coord_y