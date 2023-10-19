n, code, guess = input().split()
n = int(n)


def solution(n: int, code: str, guess: str) -> tuple[int, int]:
    r = 0
    matched = []
    unmatched = []

    for i in range(n):
        if code[i] == guess[i]:
            r += 1
            matched.append(i)
        else:
            unmatched.append(code[i])

    for i in range(n):
        if guess[i] in unmatched:
            matched.append(i)
            unmatched.remove(guess[i])

    return (r, len(matched)-r)


@lambda _: _()
def tests():
    assert solution(1, "A", "A") == (1, 0)
    assert solution(1, "A", "B") == (0, 0)
    assert solution(2, "AB", "AB") == (2, 0)
    assert solution(2, "AB", "BA") == (0, 2)


print(*solution(n, code, guess))
