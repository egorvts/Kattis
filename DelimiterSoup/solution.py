from collections import deque

l = int(input())
brs = list(input())
d = deque([])

is_ok = True
for i in range(l):
    if brs[i] in "([{":
        d.appendleft(brs[i])
    elif brs[i] == " ":
        pass
    else:
        if not(d) or d.popleft() + brs[i] not in ["()", "[]", r"{}"]:
            print(brs[i], i)
            is_ok = False
            break
if is_ok:
    print("ok so far")