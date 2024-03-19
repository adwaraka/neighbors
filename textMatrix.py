def startPoint(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if str(arr[i][j]) != "*":
                # print(i, j)
                return (i, j)

def isValid(row, col, arr):
    return row > -1 and col > -1 and row < len(arr) and col < len(arr)

def textMatrix(arr):
    start_x, start_y = startPoint(arr)
    next_x, next_y = None, None
    text = [str(arr[start_x][start_y])]
    visited = [(start_x, start_y)]
    while True and start_x is not None and start_y is not None:
        if isValid(start_x, start_y-1, arr) and str(arr[start_x][start_y-1]) != "*" and (start_x, start_y-1) not in visited:
            text.append(str(arr[start_x][start_y-1]))
            next_x, next_y = start_x, start_y-1
        if isValid(start_x, start_y+1, arr) and str(arr[start_x][start_y+1]) != "*" and (start_x, start_y+1) not in visited:
            text.append(str(arr[start_x][start_y+1]))
            next_x, next_y = start_x, start_y+1
        if isValid(start_x-1, start_y, arr) and str(arr[start_x-1][start_y]) != "*" and (start_x-1, start_y) not in visited:
            text.append(str(arr[start_x-1][start_y]))
            next_x, next_y = start_x-1, start_y
        if isValid(start_x+1, start_y, arr) and str(arr[start_x+1][start_y]) != "*" and (start_x+1, start_y) not in visited:
            text.append(str(arr[start_x+1][start_y]))
            next_x, next_y = start_x+1, start_y
        start_x, start_y = next_x, next_y
        # print(start_x, start_y)
        visited.append((next_x, next_y))
        next_x, next_y = None, None
    return "".join(text)

arr = [[ "*", "*", "*", "*", "*", "*", "*", "*", "*", "*" ], 
       [ "*", "*", "*", "*", "*", "a", "-", "c", "o", "*" ],
       [ "*", "*", "*", "*", "*", "*", "*", "*", "d", "*" ],
       [ "!", "*", "*", "*", "*", "*", "*", "*", "i", "*" ], 
       [ "k", "c", "u", "l", "*", "*", "*", "*", "n", "*" ],
       [ "*", "*", "*", "-", "*", "*", "*", "*", "g", "*" ],
       [ "*", "*", "*", "d", "*", "*", "e", "t", "-", "*" ], 
       [ "*", "*", "*", "o", "*", "*", "s", "*", "*", "l" ],
       [ "*", "*", "*", "o", "g", "-", "t", "*", "*", "o" ],
       [ "*", "*", "*", "*", "*", "*", "*", "*", "*", "l" ],]
print(textMatrix(arr))
