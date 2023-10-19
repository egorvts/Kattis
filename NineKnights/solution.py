board = []

for _ in range(5):
    board.append(list(input()))


def knights_coordinates(board: list[list[str]]) -> list:
    coordinates = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == "k":
                coordinates.append((i, j))

    return coordinates


def solution(board: list) -> str:
    coordinates = knights_coordinates(board)

    if len(coordinates) != 9:
        return "invalid"

    for k in range(9):
        possible_moves = []
        position = coordinates[k]

        possible_moves.append((position[0]-2, position[1]-1))
        possible_moves.append((position[0]-2, position[1]+1))

        possible_moves.append((position[0]-1, position[1]+2))
        possible_moves.append((position[0]+1, position[1]+2))

        possible_moves.append((position[0]+2, position[1]-1))
        possible_moves.append((position[0]+2, position[1]+1))

        possible_moves.append((position[0]-1, position[1]-2))
        possible_moves.append((position[0]+1, position[1]-2))

        possible_moves = list(filter(lambda x: (x[0] >= 0) and (
            x[0] <= 4) and (x[1] >= 0) and (x[1] <= 4), possible_moves))

        for move in possible_moves:
            if move in coordinates:
                return "invalid"

    return "valid"


print(solution(board))
