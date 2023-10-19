from collections import deque

for _ in range(int(input())):
    inp = list(input().lstrip("<[]").rstrip("[]"))
    outp = []
    cursor_ind = 0
    for i in range(len(inp)):
        ch = inp[i]

        if ch == "<":
            if cursor_ind != 0:
                outp.pop(cursor_ind-1)
                cursor_ind -= 1
        elif ch == "[":
            cursor_ind = 0
        elif ch == "]":
            cursor_ind = len(outp)
        else:
            outp.insert(cursor_ind, ch)
            cursor_ind += 1

    print("".join(outp))

            

