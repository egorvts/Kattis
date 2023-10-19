board = []

for _ in range(4):
    board.append(list(map(int, input().split())))

arrow = int(input())


def mirror_vertical(board):
    for i in range(4):
        board[i] = list(reversed(board[i]))

    return board


def rotate(board):
    rotated = []
    for i in range(3, -1, -1):
        row = []
        for j in range(4):
            row.append(board[j][i])
        rotated.append(row)

    return rotated


def rotate_clockwise(board):
    rotated = []
    for i in range(4):
        row = []
        for j in range(3, -1, -1):
            row.append(board[j][i])
        rotated.append(row)

    return rotated


def move(row):
    for i in range(4):
        if row[i] == 0:
            row = row[:i] + row[i+1:] + [0]

    if len(row) == len(set(row)):
        return row

    row = [i for i in row if i != 0]
    if len(row) == len(set(row)):
        return row + [0] * (4-len(row))

    for i in range(len(row)-1):
        try:
            if row[i] == row[i+1]:
                row = row[:i] + [row[i]*2] + row[i+2:]
        except IndexError:
            break

    return row + [0] * (4-len(row))


def move_board(board):
    board = list(map(move, board))
    return board
    

if arrow == 0:
    result = move_board(board)
    for i in result:
        print(*i)
elif arrow == 1:
    result = rotate_clockwise(move_board(rotate(board)))
    for i in result:
        print(*i)
elif arrow == 2:
    result = mirror_vertical(move_board(mirror_vertical(board)))
    for i in result:
        print(*i)
else:
    result = rotate(move_board(rotate_clockwise(board)))
    for i in result:
        print(*i)
