# Given an n x n binary matrix grid, return the length of the shortest
# clear path in the matrix. If there is no clear path, return -1.

def shortestPath(arr: list) -> int:
    # All 8 possible directions (including diagonals)
    distances = [
        [0,1], [1,0], [0,-1], [-1,0],
        [-1,1], [1,1], [1,-1], [-1,-1]
    ]

    destX, destY = len(arr) - 1, len(arr[0]) - 1
    # If start or end cell is blocked, no path exists
    if arr[destX][destY] != 0 or arr[0][0] != 0:
        print("Start/Dest blocked!")
        return -1

    queue = []
    queue.append((0, 0, 1))
    # instead of using a visited queue; mark visited as 1
    arr[0][0] = 1

    while queue:
        current_x, current_y, distance = queue.pop(0)

        if current_x == destX and current_y == destY:
            return distance

        for dx, dy in distances:
            newX = current_x + dx
            newY = current_y + dy
            if 0 <= newX <= destX and 0 <= newY <= destY:  # if valid
                if arr[newX][newY] == 0:  # if it can be visited; aka 0
                    arr[newX][newY] = 1  # mark as visited
                    queue.append([newX, newY, distance + 1])
    return -1

grid = [[0, 0, 0],
        [1, 0, 0],
        [1, 1, 0]]
print(shortestPath(grid))
