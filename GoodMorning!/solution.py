for t in range(int(input())):
    k = input()
    res = k[0]

    for i in range(1, len(k)-1):
        print("k[i]", k[i])
        if res[-1] == "0":
            res += "0"
        elif (int(k[i]) >= int(res[-1])) or (k[i] == "0"):
            res += k[i]
        else:
            res += str(int(res[-1]) + 1) 

    print(res)
