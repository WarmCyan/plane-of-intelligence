

class GridSquare:
   
    def __init__(self, x, y):
        self.x = x
        self.y = y


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.grid = [][][]

    def initalizeGrid(self):
        print("Initalizing grid of size " + str(width) + "x" + str(height))
        for y in range(0, self.height):
            for x in range(0, self.width):
                
            
