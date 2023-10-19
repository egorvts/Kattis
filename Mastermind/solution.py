n, code, guess = input().split()
n, code, guess = int(n), list(code), list(guess)

r = 0
s = 0

for i in range(n-1, 0-1, -1):
    if code[i] == guess[i]:
        r += 1
        code.pop(i)
        guess.pop(i)
        n -= 1


for i in range(n-1, 0-1, -1):
    if code[i] in guess:
        s += 1
        guess.remove(code[i])
        code.pop(i)

print(r, s)
