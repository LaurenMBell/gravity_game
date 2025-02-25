from copy import deepcopy


class Grid:
    """
    2D grid with (x, y) int indexed internal storage
    Has .width .height size properties
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = [[None] * width for i in range(height)]

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def get(self, x, y):
        if self.in_bounds(x, y):
            return self.array[y][x]
        else:
            #print("cleanup on aisle THIS PROGRAM!")
            raise IndexError

    def set(self,x,y,val):
        #print(f"this is {x}, {y} in grid thats {self.width} by {self.height}")
        if not self.in_bounds(x,y):
            raise IndexError
        self.array[y][x] = val

    def __str__(self):
        element1 = self.get(0,0)
        return f"Grid({self.height}, {self.width}, first = {element1})"

    def __repr__(self):
        #return self.__str__()
        return f"Grid.build({self.array})"

    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.array == other.array
        elif isinstance(other, list):
            return self.array == other
        else:
            return False

    #@staticmethod
    #def check_list_malformed(lst):
        #if not isinstance(lst, list):
            #raise ValueError
        #if len(lst) == 0 or len(lst[0]) == 0:
            #raise ValueError
        #w = len(lst[0])
        #for l in lst:
            #if not isinstance(l, list) or len(l) != w:
                #raise ValueError
        #return None

    @staticmethod
    def check_list_malformed(lst):
        if not isinstance(lst, list):
            raise ValueError
        if not lst:
            raise ValueError
        if any(not isinstance(sublist, list) for sublist in lst):
            raise ValueError
        if any(set(len(sublist) for sublist in lst)) != 1:
            raise ValueError
        w = len(lst[0])
        if any(len(l) != w for l in lst):
            raise ValueError

    @staticmethod
    def build(lst):
        Grid.check_list_malformed(lst)
        height = len(lst)
        width = len(lst[0])
        new_grid = Grid(width, height)
        new_grid.array = deepcopy(lst)
        return new_grid

    def copy(self):
        return Grid.build(deepcopy(self.array))