n = input()
m = input()


def solution(n: str, m: str) -> str:
    int_len = len(n) - (len(m) - 1)
    # if int_len >= 0:
    #     decimal_part = n[int_len:]
    # else:
    #     decimal_part = n
    # if decimal_part == "":
    #     decimal_part = "0"

    outp = ""
    for i in range(len(n)):
        if int_len > 0:
            if i == int_len:
                outp += "."
                outp += n[i:]
                break
            else:
                outp += n[i]
        elif int_len == 0:
            return "0." + n
        else:
            outp += "0."
            outp += "0" * abs(int_len)
            outp += n
            break

    return outp.rstrip("0").rstrip(".")

    if int_len == 0:
        return "0." + n
    elif int(decimal_part) == 0:
        return n[:int_len]
    elif int_len < 0:
        return "0." + "0" * abs(int_len) + decimal_part
    else:
        return n[:int_len] + "." + decimal_part.rstrip("0")


@lambda _: _()
def tests():
    assert solution("92746237", "100000") == "927.46237"
    assert solution("100000", "100") == "1000"
    assert solution("1234500", "10000") == "123.45"
    assert solution("1", "10") == "0.1"
    assert solution("1", "1") == "1"
    assert solution("1", "100") == "0.01"
    assert solution("123", "10000") == "0.0123"



print(solution(n, m))
