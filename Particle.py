
class Particle:
    def __init__(self, grid, x = 0, y = 0):
        self.grid = grid
        self.x = x
        self.y = y

    def __str__(self):
        return f"{type(self).__name__}({self.x},{self.y})"

    def move(self):
        new_pos = self.physics()
        if new_pos == None:
            return
        #fix this too please
        self.grid.set(self.x, self.y, None)
        self.x, self.y = new_pos
        self.grid.set(self.x, self.y, self)

    def physics(self):
        pass