n, t = map(int, input().split())
a = list(map(int, input().split()))[:n]

if t == 1:
    print(7)
elif t == 2:
    if a[0] > a[1]:
        print("Bigger")
    elif a[0] == a[1]:
        print("Equal")
    else:
        print("Smaller")
elif t == 3:
    lst = a[:3]
    lst.remove(max(lst))
    lst.remove(min(lst))
    print(*lst)
elif t == 4:
    print(sum(a))
    # filter_nums = lambda x: f"{type(x)}" == "<class 'int'>"
    # print(sum(list(filter(filter_nums, a))))
elif t == 5:
    print(sum(list(filter(lambda x: x % 2 == 0, a))))
elif t == 6:
    letters = "abcdefghijklmnopqrstuvwxyz"
    print(*list(map(lambda x: letters[x], list(map(lambda x: x % 26, a)))), sep="")
elif t == 7:
    i = 0
    checked = set()
    while True:
        i = a[i]
        if i > n-1:
            print("Out")
            break
        elif i == n-1:
            print("Done")
            break
        elif i in checked:
            print("Cyclic")
            break
        checked.add(i)
