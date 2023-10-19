for case in range(1, int(input())+1):
    s = list(input())
    t = list(input())

    ops = 0

    pairs_1_0 = 0
    pairs_0_1 = 0
    pairs_q_1 = 0
    other_unequal = 0

    for i in range(len(s)):
        if s[i] == "1" and t[i] == "0":
            pairs_1_0 += 1
        elif s[i] == "0" and t[i] == "1":
            pairs_0_1 += 1
        elif s[i] == "?" and t[i] == "1":
            pairs_q_1 += 1
        elif s[i] != t[i]:
            other_unequal += 1

    if pairs_1_0 <= pairs_0_1:
        ops += pairs_0_1 + pairs_q_1
    elif pairs_1_0 <= pairs_0_1 + pairs_q_1:
        ops += pairs_0_1
        ops += 2 * (pairs_1_0 - pairs_0_1)
        ops += pairs_q_1 - (pairs_1_0 - pairs_0_1)
    else:
        ops = -1

    if ops != -1:
        ops += other_unequal

    print(f"Case {case}: {ops}")
