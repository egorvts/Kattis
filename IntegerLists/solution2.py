for test in range(int(input())):
    p = list(input())
    n = int(input())
    if n == 0:
        lst = []
    else:
        lst = list(map(int, input()[1:-1].split(",")))

    error = False
    is_reversed = False
    remove_front = 0
    remove_end = 0

    for i in range(len(p)):
        if p[i] == "R":
            is_reversed = not is_reversed
        else:
            if is_reversed:
                remove_end += 1
            else:
                remove_front += 1

    if remove_front + remove_end > n:
        error = True
    elif remove_front + remove_end == n:
        print("[]")
        continue

    lst = lst[remove_front:len(lst)-remove_end]

    if error:
        print("error")
    else:
        if is_reversed:
            print("[", ",".join(map(str, reversed(lst))), "]", sep="")
        else:
            print("[", ",".join(map(str, lst)), "]", sep="")
