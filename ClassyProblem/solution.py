from functools import cmp_to_key


def sort(c1, c2):
    for i in range(len(c1[1])):
        if c1[1][i] < c2[1][i]:
            return 1
        elif c1[1][i] > c2[1][i]:
            return -1
    if c1[0] > c2[0]:
        return 1
    elif c1[0] < c2[0]:
        return -1
    return 0


for t in range(int(input())):
    classes = []
    max_len = 0

    for p in range(int(input())):
        name, cl = input().split(": ")
        cl = cl[:-6].split("-")
        cl.reverse()
        classes_int = [0] * len(cl)

        for c in range(len(cl)):
            if cl[c] == "middle":
                classes_int[c] = 1
            elif cl[c] == "upper":
                classes_int[c] = 2

        classes.append([name, classes_int])
        max_len = max(max_len, len(cl))

    for i in range(len(classes)):
        if len(classes[i][1]) < max_len:
            classes[i][1] += [1] * (max_len - len(classes[i][1]))

    classes.sort(key=cmp_to_key(sort))

    for c in classes:
        print(c[0])
    print("="*30)
