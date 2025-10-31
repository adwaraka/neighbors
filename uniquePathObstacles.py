# unique paths with obstacles
def uniquePathObstacles(matrix: list) -> int:
    row, col = len(matrix), len(matrix[0])
    if matrix[row - 1][col - 1] == 1:
        return 0
    # temp for memoization
    temp = [[-1]*col for _ in range(row)]
    return getPaths(0, 0, row - 1, col - 1, matrix, temp)

def getPaths(start_x, start_y, row, col, matrix, temp):
    # base; we are at our destination
    if start_x == row and start_y == col:
        return 1

    # a valid cell?? Is it an obstacle?
    if start_x > row or start_y > col or matrix[start_x][start_y] == 1:
        return 0

    # read memoized data
    if temp[start_x][start_y] != -1:
    	return temp[start_x][start_y]

    # all the rights and all the lefts
    allRights = getPaths(start_x+1, start_y, row, col, matrix, temp)
    allDowns = getPaths(start_x, start_y+1, row, col, matrix, temp)
    temp[start_x][start_y] = allRights + allDowns
    return temp[start_x][start_y]


grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(uniquePathObstacles(grid))
