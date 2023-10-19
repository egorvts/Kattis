LETTERS = "ABCDEFGH"

white = input()[7:].split(",")
black = input()[7:].split(",")

# Adds "P" for pawns
for i in range(len(white)):
    if len(white[i]) == 2:
        white[i] = "P" + white[i]
    if len(black[i]) == 2:
        black[i] = "P" + black[i]

# From string returns a piece and its coordinates
def string_to_piece(p: str) -> tuple:
    return (p[0], LETTERS.index(p[1].upper()), 8 - int(p[2]))

assert string_to_piece("Pa2") == ("P", 0, 6)
assert string_to_piece("Ra1") == ("R", 0, 7)

# Creates empty board 8 by 8
def create_board_8_8() -> list:
    board = []
    for i in range(4):
        board.append([".", ":"] * 4)
        board.append([":", "."] * 4)
    return board

# From a row of pieces creates an image of row
def row_to_full_row(row: list, isWhiteFirst: bool) -> str:
    
    white_row = [i for i in "|" + "...|:::|" * 4 + "\n"] 
    black_row = [i for i in "|" + ":::|...|" * 4 + "\n"]

    if isWhiteFirst:
        for i in range(2, 32, 4):
            white_row[i] = row[0]
            row.pop(0)
        return "".join(white_row)
    else:
        for i in range(2, 32, 4):
            black_row[i] = row[0]
            row.pop(0)
        return "".join(black_row)

# From board 8 by 8 creates a full image of board
def board_8_8_to_full(board) -> str:
    global white, black

    # Every piece converted to tuple with its coordinates
    table_8_8 = create_board_8_8()
    if white != [""]:
        white = list(map(string_to_piece, white))
    if black != [""]:
        black = list(map(string_to_piece, black))

    # Pieces placed at their coordinates
    for p in white:
        if p != "":
            table_8_8[p[2]][p[1]] = p[0]
    for p in black:
        if p != "":
            table_8_8[p[2]][p[1]] = p[0].lower()

    # Every row converted to image of row
    for row in range(len(table_8_8)):
        table_8_8[row] = row_to_full_row(table_8_8[row], row%2==0)

    # Full image of table created as list
    table = ["\n"] * 17
    for i in range(0, 17, 2):
        table[i] = "+" + "---+" * 8 + "\n"
        if i != 16:
            table[i+1] = table_8_8[i//2]
    
    # Full image of table created as string
    image = ""
    for i in table:
        image += "".join(i)

    return image

print(board_8_8_to_full(create_board_8_8()))
