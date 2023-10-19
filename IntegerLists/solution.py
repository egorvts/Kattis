from collections import deque

for test in range(int(input())):
    p = list(input())
    n = int(input())
    if n == 0:
        lst = deque([])
    else:
        lst = deque(map(int, input()[1:-1].split(",")))

    error = False
    is_reversed = False
    for i in range(len(p)):
        # print(lst)
        if p[i] == "R":
            is_reversed = not is_reversed
        else:
            if lst == deque():
                error = True
                break
            else:
                if is_reversed:
                    lst.pop()
                else:
                    lst.popleft()
    if error:
        print("error")
    else: 
        #if is_reversed:
        #    print("[", ",".join(map(str, reversed(lst))), "]", sep="")
        #else:
        #    print("[", ",".join(map(str, lst)), "]", sep="")
        print("[", end="")
        while lst != deque([]):
            if is_reversed:
                print(lst.pop(), end="")
            else:
                print(lst.popleft(), end="")
            if lst != deque([]):
                print(",", end="")
        print("]")
