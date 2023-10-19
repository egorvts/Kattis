cases = {}

for c in range(int(input())):
    s = input()
    t = input()
    cases[c+1] = [s, t]

for case in cases:
    s, t = cases[case]

    result = {s: "", t: ""}
    ops_count = 0

    for s_elt, t_elt in zip(s, t):
        if s_elt == "?":
            if t_elt == "0":
                result[s] += "0"
                result[t] += "0"
                ops_count += 1
            else:
                result[s] += "1"
                result[t] += "1"
                ops_count += 1
        elif s_elt == "0":
            if t_elt == "0":
                result[s] += "0"
                result[t] += "0"
            else:
                result[s] += "1"
                result[t] += "1"
                ops_count += 1
        else:
            if t_elt == "1":
                result[s] += "1"
                result[t] += "1"
            else:
                result[s] += "1"
                result[t] += "0"

    print(f"Case {case}: {ops_count}")
