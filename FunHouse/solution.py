count = 1


def one_move(coordinates, direction):
    if direction == "up":
        return (coordinates[0]-1, coordinates[1])
    elif direction == "right":
        return (coordinates[0], coordinates[1]+1)
    elif direction == "down":
        return (coordinates[0]+1, coordinates[1])
    return (coordinates[0], coordinates[1]-1)


while True:
    w, l = map(int, input().split())
    if w == l == 0:
        break

    house = []
    coordinates = (0, 0)
    for i in range(l):
        row = list(input())
        if "*" in row:
            coordinates = (i, row.index("*"))
        house.append(row)

    move = ""
    if coordinates[0] == 0:
        move = "down"
    elif coordinates[0] == l - 1:
        move = "up"
    elif coordinates[1] == 0:
        move = "right"
    else:
        move = "left"

    while True:
        coordinates = one_move(coordinates, move)
        location = house[coordinates[0]][coordinates[1]]
        if location != ".":
            if location == "x":
                house[coordinates[0]][coordinates[1]] = "&"
                print("HOUSE", count)
                print("\n".join("".join(i) for i in house))
                break
            else:
                if location == "/":
                    if move == "up":
                        move = "right"
                    elif move == "right":
                        move = "up"
                    elif move == "down":
                        move = "left"
                    else:
                        move = "down"
                else:
                    if move == "up":
                        move = "left"
                    elif move == "right":
                        move = "down"
                    elif move == "down":
                        move = "right"
                    else:
                        move = "up"

    count += 1
