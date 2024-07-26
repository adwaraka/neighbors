def processIsland(i, j, arr):
    visited, queue = [(i, j)], [(i, j)]
    while queue != []:
       temp = queue.pop()
       # print(i, j)
       i, j = temp[0], temp[1]
       if isValid(i+1, j, arr) and arr[i+1][j]==1 and (i+1, j) not in visited:
           queue.append((i+1, j))
           visited.append((i+1, j))
       if isValid(i-1, j, arr) and arr[i-1][j]==1 and (i-1, j) not in visited:
           queue.append((i-1, j))
           visited.append((i-1, j))
       if isValid(i, j+1, arr) and arr[i][j+1]==1 and (i, j+1) not in visited:
           queue.append((i, j+1))
           visited.append((i, j+1))
       if isValid(i, j-1, arr) and arr[i][j-1]==1 and (i, j-1) not in visited:
           queue.append((i, j-1))
           visited.append((i, j-1))
    # print(sorted(visited))
    return visited


def countIslands(arr):
    islands, visited = 0, set()
    for i in range(len(arr)):
       for j in range(len(arr)):
           if arr[i][j] == 1 and (i,j) not in visited:
              # print("Process Island")
              vlist = processIsland(i, j, arr)
              for dimension in vlist:
                  visited.add(dimension)
              islands+=1
    return islands


def isValid(row, col, arr):
    # print(row, col, arr[row][col])
    return row > -1 and col > -1 and row < len(arr) and col < len(arr[0])

arr = [[ 0, 0, 1, 0, 0, 0, 0, 0, 0, 0 ], 
       [ 0, 0, 0, 0, 0, 1, 1, 1, 1, 0 ],
       [ 0, 0, 0, 0, 0, 0, 0, 1, 1, 0 ],
       [ 1, 0, 1, 1, 0, 0, 0, 1, 1, 0 ], 
       [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0 ],
       [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
       [ 0, 0, 0, 0, 0, 0, 1, 1, 0, 0 ], 
       [ 0, 0, 0, 0, 0, 0, 1, 0, 0, 0 ],
       [ 0, 0, 0, 1, 1, 1, 1, 0, 0, 0 ],
       [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ]
       ]
print(countIslands(arr))
