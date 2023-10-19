for _ in range(int(input())):
    inp = list(input().lstrip("<[]").rstrip("[]"))
    is_opened = False
    open_ind = 0
    i = 0
    parts = []
    while i < len(inp):
        if inp[i] == "[":
            open_ind = i + 1
            is_opened = True
            i += 1
        elif inp[i] == "]":
            if is_opened:
                parts.append((open_ind, i))
                is_opened = False
                i += 1
            else:
                inp.pop(i)
        else:
            i += 1

    for p in parts:
        part = inp[p[0]:p[1]]
        inp[p[0]:p[1]] = [""]*len(part)
        inp = part + inp

    i = 0
    while i < len(inp):
        if inp[i] == "<":
            inp.pop(i)
            inp.pop(i-1)
            i -= 1
        elif inp[i] in "[]":
            inp.pop(i)
        else:
            i += 1

    print("".join(inp))