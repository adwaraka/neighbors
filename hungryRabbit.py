'''
There is a rabbit that starts in the middle of an n x m matrix, n > 0, m > 0.
Each element of a matrix is an integer representing points gained for being on the spot. 

If there are multiple possible "middles" then choose the one which has the highest point
value to start on.

On each iteration, the rabbit can move up, left, right, or down. 
The rabbit will always move to the next spot with the highest point value 
and will "consume" those points (set the point value in that position to 0). 
The rabbit spots when all positions around it are 0s. 

Calculate how many points the rabbit will score for a given m x n matrix.
'''
def potentialCenter(garden):
    row = len(garden)
    col = len(garden[0])
    if row%2 == 0 and col%2 == 0:
        higherCarrotCount = {
            '1': garden[row//2][col//2],
            '2': garden[row//2-1][col//2],
            '3': garden[row//2][col//2-1],
            '4': garden[row//2-1][col//2-1]
            }
        sorted_d = sorted(higherCarrotCount.items(), key=lambda x:x[1], reverse=True)
        if sorted_d[0][0] == '1':
            potentialCenter_x, potentialCenter_y = row//2, col//2
        elif sorted_d[0][0] == '2':
            potentialCenter_x, potentialCenter_y = row//2-1 , col//2
        elif sorted_d[0][0] == '3':
            potentialCenter_x, potentialCenter_y = row//2, col//2-1 
        else:
            potentialCenter_x, potentialCenter_y = row//2-1, col//2-1 
    elif row%2 != 0 and col%2 == 0:
        higherCarrotCount = {'1': garden[row//2][col//2], '2': garden[row//2][col//2-1]}
        sorted_d = sorted(higherCarrotCount.items(), key=lambda x:x[1], reverse=True)
        if sorted_d[0][0] == '1':
            potentialCenter_x, potentialCenter_y = row//2, col//2
        else:
            potentialCenter_x, potentialCenter_y = row//2 , col//2-1
    elif row%2 == 0 and col%2 != 0:
        higherCarrotCount = {'1': garden[row//2][col//2], '2': garden[row//2-1][col//2]}
        sorted_d = sorted(higherCarrotCount.items(), key=lambda x:x[1], reverse=True)
        if sorted_d[0][0] == '1':
            potentialCenter_x, potentialCenter_y = row//2, col//2
        else:
            potentialCenter_x, potentialCenter_y = row//2-1, col//2
    else:
        potentialCenter_x, potentialCenter_y = row//2, col//2
    return potentialCenter_x, potentialCenter_y 


def isValid(arr, row, col):
    return row > -1 and col > -1 and row < len(arr) and col < len(arr[0])


def hungryRabbit(garden):
    startingPos_x, startingPos_y = potentialCenter(garden)
    print("Starting point {}, {}".format(startingPos_x, startingPos_y))
    carrotsEaten = garden[startingPos_x][startingPos_y]
    cur_x, cur_y = startingPos_x, startingPos_y
    print(
        "Position {}, {} and currently eaten "
        "carrot quantity {}".format(cur_x, cur_y, carrotsEaten))
    garden[cur_x][cur_y] = 0
    while getAdjacentsquares(garden, cur_x, cur_y) != (0, 0, 0, 0):
        new_pos_x, new_pos_y = getnextMaxCarrot(garden, cur_x, cur_y)
        carrotsEaten+=garden[new_pos_x][new_pos_y]
        garden[new_pos_x][new_pos_y] = 0
        print(
            "Position {}, {} and currently eaten "
            "carrot quantity {}".format(new_pos_x, new_pos_y, carrotsEaten))
        cur_x, cur_y = new_pos_x, new_pos_y
        # print(garden)
    return carrotsEaten


def getAdjacentsquares(garden, cur_x, cur_y):
    first, second, third, fourth = 0, 0, 0, 0
    if isValid(garden, cur_x+1, cur_y):
        first = garden[cur_x+1][cur_y]
    if isValid(garden, cur_x-1, cur_y):
        second = garden[cur_x-1][cur_y]
    if isValid(garden, cur_x, cur_y+1):
        third = garden[cur_x][cur_y+1]
    if isValid(garden, cur_x, cur_y-1):
        fourth = garden[cur_x][cur_y-1]
    return (first, second, third, fourth)


def getnextMaxCarrot(garden, cur_x, cur_y):
    first, second, third, fourth = 0, 0, 0, 0
    if isValid(garden, cur_x+1, cur_y):
        first = garden[cur_x+1][cur_y]
    if isValid(garden, cur_x-1, cur_y):
        second = garden[cur_x-1][cur_y]
    if isValid(garden, cur_x, cur_y+1):
        third = garden[cur_x][cur_y+1]
    if isValid(garden, cur_x, cur_y-1):
        fourth = garden[cur_x][cur_y-1]

    carrot_count = {
        '1': first,
        '2': second,
        '3': third,
        '4': fourth
    }
    sorted_d = sorted(carrot_count.items(), key=lambda x:x[1], reverse=True)
    # print(sorted_d)
    if sorted_d[0][0] == '1':
        new_pos_x, new_pos_y = cur_x+1, cur_y
    elif sorted_d[0][0] == '2':
        new_pos_x, new_pos_y = cur_x-1, cur_y
    elif sorted_d[0][0] == '3':
        new_pos_x, new_pos_y = cur_x, cur_y+1 
    else:
        new_pos_x, new_pos_y = cur_x, cur_y-1 
    return new_pos_x, new_pos_y


if __name__ == "__main__":
    garden = [[5, 7, 8, 6, 3],
              [1, 0, 7, 0, 4],
              [4, 6, 3, 4, 9],
              [3, 1, 0, 5, 8],]
    print("Carrots Eaten: {}".format(hungryRabbit(garden)))
