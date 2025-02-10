'''
Not neighbor problem per-se but close enough.

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
'''


class Paint(object):

    def __init__(self, row, col):
        self.row, self.col = row, col
        self.arr = [["-"]*col for i in range(row)]

    def clear(self):
        for i in range(self.row):
            for j in range(self.col):
                self.arr[i][j] = "W"

    def draw(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.arr[i][j], end="")  # print without newline
            print()
        print()

    def draw_cell(self, coord_x, coord_y, col):
        if self.__isValid(coord_x, coord_y):
            self.arr[coord_x][coord_y] = col
        else:
            print("Invalid position")

    def draw_rectangle(self, coord_x1, coord_y1, coord_x2, coord_y2, col):
        if self. __isValid(coord_x1, coord_y1) and self.__isValid(coord_x2, coord_y2):
            for i in range(coord_y1, coord_y2):
                for j in range(coord_x1, coord_x2):
                    self.arr[i][j] = col

    def undo(self):
    	# TODO
    	pass

    def redo(self):
    	# TODO
    	pass

    def __isValid(self, row, col):
        return row>-1 and col>-1 and row<=self.row and col<=self.col


def testPaint():
    paint = Paint(22, 22)
    paint.clear()
    paint.draw()
    paint.draw_cell(20, 2, 'G')
    paint.draw()
    paint.clear()
    paint.draw()
    paint.draw_rectangle(6, 3, 18, 10, 'B')
    paint.draw()
    paint.draw_rectangle(11, 15, 19, 20, 'R')
    paint.draw()

testPaint()