case = 0
for c in range(int(input())):
    case += 1
    s = list(input())
    t = list(input())
    ops = 0

    pairs_1_0 = 0
    pairs_1_0_inds = []
    pairs_0_1 = 0
    pairs_0_1_inds = []
    pairs_q_0 = 0
    pairs_q_0_inds = []

    for i in range(len(s)):
        if s[i] == "1" and t[i] == "0":
            pairs_1_0 += 1
            pairs_1_0_inds.append(i)
        elif s[i] == "0" and t[i] == "1":
            pairs_0_1 += 1
            pairs_0_1_inds.append(i)
        elif s[i] == "?" and t[i] == "0":
            pairs_q_0 += 1
            pairs_q_0_inds.append(i)
    if pairs_1_0 > pairs_0_1 + pairs_q_0:
        print(f"Case {case}: -1")
        flag = False
        continue
    if pairs_0_1 > pairs_1_0:
        for ind in range(pairs_1_0):
            s[pairs_0_1_inds[ind]] = "1"
            s[pairs_1_0_inds[ind]] = "0"
            ops += 1
            pairs_0_1_inds.pop(0)
    else:
        for ind in range(pairs_0_1):
            s[pairs_0_1_inds[ind]] = "1"
            s[pairs_1_0_inds[ind]] = "0"
            ops += 1
            pairs_1_0_inds.pop(0)
        for ind in range(pairs_1_0 - pairs_0_1):
            s[pairs_q_0_inds[ind]] = "1"
            s[pairs_1_0_inds[ind]] = "0"
            ops += 2
            pairs_q_0_inds.pop(0)
    for i in range(len(s)):
        flag = True
        if s[i] == "?" or (s[i] == "0" and t[i] == "1"): 
            s[i] = t[i]
            ops += 1
            
    if flag:
        print(f"Case {case}: {ops}")
    