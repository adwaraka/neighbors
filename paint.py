'''
Not neighbor problem per-se but mixture of graphs and stacks

You are expected to work through a basic “Paint” program (think of Microsoft Paint), 
where we have a fixed m x n grid. 
The initial grid should be all white, where colors are in the format of a 
simple char code (e.g. W for white). Only one color can fill a cell at a time.

Each cell can be identified by its coordinates (x, y), where 0≤x<m and 0≤y<n.

The initial expected functionality is:

clear - sets the whole canvas back to all white

draw_cell - takes in a coordinate and color and paints the cell that color

draw_rectangle - takes in top left and bottom right coordinates and a color. 
The coordinates are inclusive corners of the rectangle to be filled with the input color

undo - undoes the previous action

redo - redoes the previous undo – after we perform a new drawing action, 
the redo history should be cleared

draw - helper function to draw the grid to standard output

color_fill - fill in color
'''
import copy

class Paint(object):

    def __init__(self, row, col):
        self.row, self.col = row, col
        self.arr = [["-"]*col for i in range(row)]
        self.sequence, self.history = [], []

    def clear(self):
        for i in range(self.row):
            for j in range(self.col):
                self.arr[i][j] = "W"
        arrCopy = copy.deepcopy(self.arr)
        self.sequence.append(arrCopy)
        self.history = []

    def draw(self):
        array = copy.deepcopy(self.sequence[len(self.sequence) - 1])
        for i in range(self.row):
            for j in range(self.col):
                print(array[i][j], end="")  # print without newline
            print()
        print()

    def draw_cell(self, coord_x, coord_y, col):
        array = copy.deepcopy(self.sequence[len(self.sequence) - 1])
        try:
            if self.__isValid(coord_x, coord_y):
                array[coord_x][coord_y] = col
            else:
                print("Invalid position")
        finally:
            arrCopy = copy.deepcopy(array)
            self.sequence.append(arrCopy)
            self.history = []

    def draw_rectangle(self, coord_x1, coord_y1, coord_x2, coord_y2, col):
        array = copy.deepcopy(self.sequence[len(self.sequence) - 1])
        if self. __isValid(coord_x1, coord_y1) and self.__isValid(coord_x2, coord_y2):
            for i in range(coord_y1, coord_y2):
                for j in range(coord_x1, coord_x2):
                    array[i][j] = col
        arrCopy = copy.deepcopy(array)
        self.sequence.append(arrCopy)
        self.history = []

    def redo(self):
        try:
            recentHistory = self.history.pop()
            self.sequence.append(recentHistory)
        except IndexError:
            print("Cannot redo")

    def undo(self):
        try:
            lastAction = self.sequence.pop()
            self.history.append(lastAction)
        except IndexError:
            print("Cannot undo")

    def __isValid(self, row, col):
        return row>-1 and col>-1 and row<self.row and col<self.col


def testPaint():
    paint = Paint(3, 3)
    paint.clear()
    paint.draw_cell(0, 0, 'R')
    paint.draw_cell(0, 1, 'R')
    paint.draw_cell(0, 2, 'R')
    paint.draw_cell(1, 1, 'R')
    paint.draw_cell(1, 1, 'B')
    paint.draw()
    paint.undo()
    paint.undo()
    paint.undo()
    paint.undo()
    paint.draw()

testPaint()
