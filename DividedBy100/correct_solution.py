import sys

n = []
n_len = 0
zeroes = 0

read_n = True
read_0 = False
"""
1. Количество 0 в конце
2.  1. Если есть 0 в конце:
        1. zeroes - end_0
    2. Нет 0 в конце
"""
while True:
    ch = sys.stdin.read(1)
    if ch.isdigit() and read_n:
        n.append(ch)
        n_len += 1
    elif ch.isdigit() and ch != "1":
        zeroes += 1
    elif not (read_n) and not (ch.isdigit()):
        break
    else:
        read_n = False


for i in range(len(n)-1, 0-1, -1):
    if (n[i] == "0") and (zeroes != 0):
        zeroes -= 1
        n_len -= 1
        n.pop(i)
    elif zeroes == 0:
        print("".join(n))
        break
    else:
        result = "".join(n)
        result = "0" * (zeroes - len(result)) + result

        if result[0] == "0":
            print("0." + result)
        else:
            result = list(result)
            result.insert(-zeroes, ".")
            if result[0] == ".":
                print("0" + "".join(result))
                break
            print("".join(result))
        break
        # if result[0] == ".":
        #     print("0"+result)
        # else:
        #     print(result)
        # break


# @lambda _: _()
# def tests():
#     assert solution("92746237", "100000") == "927.46237"
#     assert solution("100000", "100") == "1000"
#     assert solution("1234500", "10000") == "123.45"
#     assert solution("1", "10") == "0.1"
#     assert solution("1", "1") == "1"
#     assert solution("1", "100") == "0.01"
#     assert solution("123", "10000") == "0.0123"


# print(solution(n, m))
