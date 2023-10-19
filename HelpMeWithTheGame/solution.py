from functools import cmp_to_key

LETTERS = "ABCDEFGH"
PRIORITY = {"K": 0, "Q": 1, "R": 2, "B": 3, "N": 4, "P": 5}

board = []
_ = input()
for i in range(8):
    row = input()
    board.append(row)
    sep = input()

def sort_pieces_white(p1: list, p2: list) -> int:
    if PRIORITY[p1[0]] < PRIORITY[p2[0]]:
        return -1
    elif PRIORITY[p1[0]] > PRIORITY[p2[0]]:
        return 1
    else:
        if p1[1] < p2[1]:
            return -1
        elif p1[1] > p2[1]:
            return 1
        else:
            if p1[2] < p2[2]:
                return -1
            elif p1[2] > p2[2]:
                return 1
            return 0
        
def sort_pieces_black(p1: list, p2: list) -> int:
    if PRIORITY[p1[0]] < PRIORITY[p2[0]]:
        return -1
    elif PRIORITY[p1[0]] > PRIORITY[p2[0]]:
        return 1
    else:
        if p1[1] > p2[1]:
            return -1
        elif p1[1] < p2[1]:
            return 1
        else:
            if p1[2] < p2[2]:
                return -1
            elif p1[2] > p2[2]:
                return 1
            return 0
    '''
    Сортировка:
        1. приоритет
        2. номер строки 
            2.1 белые – меньше
            2.2 чёрные – больше
        3. номер колонки (меньше)
    '''

def coordinates_to_position(coordinates: list) -> str:
    if coordinates[0] != "P":
        return str(coordinates[0]) + LETTERS[coordinates[2]].lower() + str(coordinates[1])
    else:
        return LETTERS[coordinates[2]].lower() + str(coordinates[1])

def solution(board):
    pieces = []
    for row in board:
        row_upd = []
        for i in range(2, 32, 4):
            row_upd.append(row[i])
        pieces.append(row_upd)

    white =[]
    black = []

    for row in range(8):
        for piece in range(8):
            if pieces[row][piece] != "." and pieces[row][piece] != ":":
                if pieces[row][piece] == pieces[row][piece].lower():
                    black.append([pieces[row][piece].upper(), 8-row, piece])
                else:
                    white.append([pieces[row][piece], 8-row, piece])

    white = sorted(white, key=cmp_to_key(sort_pieces_white))
    black = sorted(black, key=cmp_to_key(sort_pieces_black))

    white = list(map(coordinates_to_position, white))
    black = list(map(coordinates_to_position, black))

    white = "White: " + ",".join(white)
    black = "Black: " + ",".join(black)

    print(white)
    print(black)
    
solution(board)
