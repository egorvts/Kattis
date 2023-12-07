def f(n):
    b = bin(n)[2:]
    b = "0" * (8 - len(b)) + b
    num = ""
    for i in b:
        if i == "0":
            num += "1"
        else:
            num += "0"
    return int(num, 2) - n

for n in range(1000):
    if f(n) == 111:
        print(n)
        break