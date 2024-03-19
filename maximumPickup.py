def leastValueGrid(arr):
    minVal, start_x, start_y = arr[0][0], 0, 0
    n = len(arr[0])
    for i in range(n):
         for j in range(n):
             if arr[i][j] < minVal:
                 minVal = arr[i][j]
                 # print(minVal)
                 start_x, start_y = i, j
    return start_x, start_y, minVal

def isValid(row, col, arr):
    # print(row, col, arr[row][col])
    return row > -1 and col > -1 and row < len(arr[0]) and col < len(arr[0])

def maximumPickup(arr):
    start_x, start_y, minVal = leastValueGrid(arr)
    # print(start_x, start_y)
    path, visited = [minVal], [(start_x, start_y)]
    while True:
        temp = []
        print("New position: {} {}".format(start_x, start_y))
        if isValid(start_x, start_y-1, arr) and (start_x, start_y-1) not in visited:
            print("Adding {}".format(arr[start_x][start_y-1]))
            temp.append((arr[start_x][start_y-1], start_x, start_y-1))

        if isValid(start_x, start_y+1, arr) and (start_x, start_y+1) not in visited:
            print("Adding {}".format(arr[start_x][start_y+1]))
            temp.append((arr[start_x][start_y+1], start_x, start_y+1))

        if isValid(start_x-1, start_y, arr) and (start_x-1, start_y) not in visited:
            print("Adding {}".format(arr[start_x-1][start_y]))
            temp.append((arr[start_x-1][start_y], start_x-1, start_y))

        if isValid(start_x+1, start_y, arr) and (start_x+1, start_y) not in visited:
            print("Adding {}".format(arr[start_x+1][start_y]))
            temp.append((arr[start_x+1][start_y], start_x+1, start_y))

        if temp == []:
            break
        temp = sorted(temp, key = lambda t: t[0])

        if temp[0][0] > path[-1]:
            path.append(temp[0][0])
            start_x, start_y = temp[0][1], temp[0][2]
        visited.append((temp[0][1], temp[0][2]))
    return path


arr = [[ 9, 7, 4 ], 
       [ 6, 6, 8 ],
       [ 2, 1, 1 ]]
# print(leastValueGrid(arr))
# print(isValid(2, 3, arr))
print(maximumPickup(arr))
