def check(n):
    if n == str(len(n)):
        return 1
    else:
        return 1 + check(len(n))


while True:
    inp = input()
    if inp == "END":
        break
    else:
        for i in range(0, 10 ** 6):
            x = str(len(inp))
            if inp == x:
                print(i + 1)
                break
            else:
                inp = x
