def line_sort(l):
    m = sorted(l, key=str.lower)

    inds = [-1] * len(l)

    for i in range(len(l)):
        if l[i] == m[i]:
            inds[i] = i
            m[i] = "."

    for i in range(len(l)):
        if inds[i] == -1:
            m_ind = m.index(l[i])
            inds[i] = m_ind
            m[m_ind] = "."

    # print(inds)
    return inds


def sort_by_inds(l, inds):
    len_l = len(l)
    # print(inds)

    sorted_l = ["."] * len_l
    for i in range(len_l):
        # print(inds[i], l[i])
        sorted_l[inds[i]] = l[i]

    return sorted_l


t = 0
while True:
    r, c = map(int, input().split())
    if r == c == 0:
        break
    elif t != 0:
        print()
    else:
        t += 1

    lines = []
    for _ in range(r):
        lines.append(list(input()))

    inds = line_sort(lines[0])

    for l in lines:
        # print(l)
        # print()
        # print(line_sort(l))
        print("".join(sort_by_inds(l, inds)))
