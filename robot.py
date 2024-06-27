# Unique paths from left-top to bottom-right
def uniquePaths(row, col):
    # current x, y
    memo = [[-1]*col for i in range(row)]
    startX, startY = 0, 0
    return uniquePathsRecursion(startX, startY, row, col, memo)

def uniquePathsRecursion(startX, startY, row, col, memo):
    # reached the bottom right
    if startX == row-1 and startY == col-1:
        return 1

    # memoized value
    if memo[startX][startY] != -1:
        return memo[startX][startY]

    allRight, allDown = 0, 0
    if startX < row-1:
        allRight = uniquePathsRecursion(startX+1, startY, row, col, memo)
    if startY < col-1:
        allDown = uniquePathsRecursion(startX, startY+1, row, col, memo)
    memo[startX][startY] = allDown + allRight
    return memo[startX][startY]


if __name__ == "__main__":
    environment = [[1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],]
    print("Unique paths: {}".format(
      uniquePaths(len(environment), len(environment[0]))))
