from Particle import Particle

class Sand(Particle):
    def is_move_okay(self, x,y):
        #makes sure its in bounds
        if not self.grid.in_bounds(x,y):
            return False
        #move straight down
        if x == self.x and y == self.y + 1:
            if self.grid.get(x,y) is None:
                return True
        #move to the down and left
        if x == self.x - 1 and y == self.y + 1:
            if self.grid.get(x,y) is None and self.grid.get(self.x - 1, self.y) is None:
                return True
        #move down right
        if x == self.x + 1 and y == self.y + 1:
            if self.grid.get(x,y) is None and self.grid.get(self.x + 1, self.y) is None:
                return True
        return False

    def physics(self):
        if self.is_move_okay(self.x, self.y + 1):
            return (self.x, self.y + 1)
        elif self.is_move_okay(self.x - 1, self.y + 1):
            return (self.x - 1, self.y + 1)
        elif self.is_move_okay(self.x + 1, self.y + 1):
            return (self.x + 1, self.y + 1)
        else:
            return None

class Rock(Particle):
    def physics(self):
        return None

class Bubble(Particle):
    def is_move_okay(self, x,y):
        #makes sure its in bounds
        if not self.grid.in_bounds(x,y):
            return False
        #move straight up
        if x == self.x and y == self.y - 1:
            if self.grid.get(x,y) is None:
                return True
        if x == self.x + 1 and y == self.y - 1:
            if self.grid.get(x,y) is None and self.grid.get(self.x + 1, self.y) is None:
                return True
        #move to the up and left
        if x == self.x - 1 and y == self.y - 1:
            if self.grid.get(x,y) is None and self.grid.get(self.x - 1, self.y) is None:
                return True
        #move up right
        return False

    def physics(self):
        if self.is_move_okay(self.x, self.y - 1):
            return (self.x, self.y - 1)
        elif self.is_move_okay(self.x + 1, self.y - 1):
            return (self.x + 1, self.y - 1)
        elif self.is_move_okay(self.x - 1, self.y - 1):
            return (self.x - 1, self.y - 1)
        else:
            return None