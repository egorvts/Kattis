n = list(input())
m = list(input())

decimal = len(m) - 1

if n[-decimal:].count("0") != len(n[-decimal:]):
    res = f"{''.join(n[:-decimal])}.{''.join(''.join(n[-decimal:]).rsplit('0'))}"
    if res[0] == ".":
        print(f"0{res}")
    else:
        print(res)
else:
    print(f"{''.join(n[:-decimal])}")
