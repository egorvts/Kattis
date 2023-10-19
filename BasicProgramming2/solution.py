n, t = map(int, input().split())
a = list(map(int, input().split()))

if t == 1:
    a.sort()
    is_in = False
    for x in range(len(a)-1):
        too_big = False

        if a[x] > 7777:
            break

        for y in range(x+1, len(a)):
            if a[y] > 7777:
                break
            elif a[x] != a[y] and a[x] + a[y] == 7777:
                is_in = True
                break
            elif a[x] + a[y] > 7777:
                too_big = True
                break

        if is_in or too_big:
            break

    if is_in:
        print("Yes")
    else:
        print("No")

elif t == 2:
    if len(a) == len(set(a)):
        print("Unique")
    else:
        print("Contains duplicate")

elif t == 3:
    a.sort()
    outp = -1
    count = 1
    num = a[0]
    for i in range(1, len(a)):
        if a[i] != num:
            count = 1
            num = a[i]
        else:
            count += 1
            if count > n / 2:
                outp = num
                break
    print(outp)

elif t == 4:
    a.sort()
    if n % 2 != 0:
        print(a[n // 2])
    else:
        print(a[n // 2 - 1], a[n // 2])

else:
    b = list(filter(lambda x: 100 <= x <= 999, a))
    b.sort()
    print(*b)
