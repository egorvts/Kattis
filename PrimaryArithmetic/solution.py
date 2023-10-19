while True:
    n1, n2 = input().split()
    len_1 = len(n1)
    len_2 = len(n2)
    if len_1 > len_2:
        n2 = "0" * (len_1 - len_2) + n2
    elif len_2 > len_1:
        n1 = "0" * (len_2 - len_1) + n1

    if n1 == n2 == "0":
        break

    ops = 0
    rem = 0
    for i in range(max(len_1-1, len_2-1), -1, -1):
        if int(n1[i]) + int(n2[i]) + rem > 9:
            ops += 1
            rem = 1
        else:
            rem = 0

    if str(ops)[-1] == "1":
        print(f"{ops} carry operation.")
    elif ops:
        print(f"{ops} carry operations.")
    else:
        print("No carry operation.")