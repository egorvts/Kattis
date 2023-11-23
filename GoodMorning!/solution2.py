avaliable_inputs = {1: "1234567890",
                    2: "2356890",
                    3: "369",
                    4: "4567890",
                    5: "56890",
                    6: "69",
                    7: "7890",
                    8: "890",
                    9: "9",
                    0: "0"}

for t in range(int(input())):
    min_difference = 200
    res = 0

    k = input()
    for i in range(len(k)):
        k = int(k)
        for d1 in range(3):
            for d2 in range(10):
                for d3 in range(10):
                    num = int(str(d1) + str(d2) + str(d3))
                    if (str(d2) in avaliable_inputs[d1]) and (str(d3) in avaliable_inputs[d2]):
                        if abs(k - num) < min_difference:
                            min_difference = k - num
                            res = num
                    elif (d1 == 0) and (str(d3) in avaliable_inputs[d2]):
                        if abs(k - num) < min_difference:
                            min_difference = k - num
                            res = num
    print(res)
