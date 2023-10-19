from sys import stdin
from functools import cmp_to_key


def cmp_points(a, b) -> int:
    if a[0] == b[0]:
        return 0

    ords_ints = list(range(48, 57+1))
    ords_lower = list(range(97, 122+1))
    ords_upper = list(range(65, 90+1))

    ords = ords_ints + ords_lower + ords_upper

    if ords.index(ord(a[0])) < ords.index(ord(b[0])):
        return -1

    return 1


# input
images = []
image = ""
for line in stdin:
    if line != "\n":
        line.rstrip()
        image += line
    else:
        images.append(image)
        image = ""
images.append(image)


def str_to_points(img: str) -> list:
    """
    Creates list of all points with their coordinates
    """
    lines = img.split("\n")[:-1]
    points = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] != ".":
                points.append((lines[i][j], i, j))

    points.sort(key=cmp_to_key(cmp_points))
    # points.sort(key=lambda x: x[0])
    return points


def img_to_table(img: str) -> list:
    """
    Creates table from image
    """
    split_img = img.split("\n")[:-1]

    return list(map(list, split_img))


def table_to_img(table: list) -> str:
    """
    Creates image from table
    """
    return "\n".join(["".join(i) for i in table])


def solution(img: str) -> str:
    points = str_to_points(img)
    table = img_to_table(img)

    for i in range(len(points)-1):
        p1 = points[i]
        p2 = points[i+1]
        if p1[1] == p2[1]:
            if p1[2] < p2[2]:
                for i in range(p1[2]+1, p2[2]):
                    if table[p1[1]][i] == "|":
                        table[p1[1]][i] = "+"
                    elif table[p1[1]][i] == ".":
                        table[p1[1]][i] = "-"
            else:
                for i in range(p2[2]+1, p1[2]):
                    if table[p1[1]][i] == "|":
                        table[p1[1]][i] = "+"
                    elif table[p1[1]][i] == ".":
                        table[p1[1]][i] = "-"
        else:
            if p1[1] < p2[1]:
                for i in range(p1[1]+1, p2[1]):
                    if table[i][p1[2]] == "-":
                        table[i][p1[2]] = "+"
                    elif table[i][p1[2]] == ".":
                        table[i][p1[2]] = "|"
            else:
                for i in range(p2[1]+1, p1[1]):
                    if table[i][p1[2]] == "-":
                        table[i][p1[2]] = "+"
                    elif table[i][p1[2]] == ".":
                        table[i][p1[2]] = "|"

    return table_to_img(table)


print("\n\n".join(list(map(solution, images))).rstrip())
