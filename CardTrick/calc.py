from string import ascii_lowercase
LETTERS = ascii_lowercase[:12]

for n in range(3, 13+1):
    cards = list(LETTERS[0] + "1" + LETTERS[1:n-1])
    pull = 1
    letters_code = {}
    while cards:
        for i in range(pull):
            cards.append(cards.pop(0))
        c = cards.pop(0)
        letters_code[c] = pull
        pull += 1

    res = ""
    for i in LETTERS[:n-1]:
        res += str(letters_code[i])

    # res = list(res[0] + "1" + res[1:])

    res = res[0] + "1" + res[1:]

    print(n, res)
