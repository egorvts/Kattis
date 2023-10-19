while True:
    n = int(input())
    if n == 0:
        break

    res = ["?"] * 32
    for _ in range(n):
        inp = list(input().split())
        # print(inp)
        if len(inp) == 2:
            todo, i = inp
        else:
            todo, i, j = inp
            j = int(j)

        i = int(i)

        if todo == "CLEAR":
            res[i] = "0"
        elif todo == "SET":
            res[i] = "1"
        elif todo == "OR":
            if res[i] == "1" or res[j] == "1":
                res[i] = "1"
            elif res[i] == "0" and res[j] == "0":
                res[i] = "0"
            elif res[i] == "?" and res[j] == "?":
                res[i] = "?"
                
        elif todo == "AND":
            if res[i] == "1" and res[j] == "1":
                res[i] = "1"
            elif res[i] == "0" or res[j] == "0":
                res[i] = "0"
            else:
                res[i] = "?"

    res.reverse()
    print(*res, sep="")