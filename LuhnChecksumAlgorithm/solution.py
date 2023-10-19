def str_sum(s):
    result = 0
    for i in s:
        result += int(i)
    return result

assert str_sum("110") == 2
assert str_sum("10") == 1

def solution(n):
    n.reverse()
    for i in range(len(n)):
        if i % 2 != 0:
            num = n[i] * 2
            if num > 9:
                num = str_sum(str(num))
            n[i] = num
    return sum(n)

for _ in range(int(input())):
    n = list(map(int, list(input())))
    if solution(n) % 10 == 0:
        print("PASS")
    else:
        print("FAIL")
