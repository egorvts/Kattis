games = []
inp = {}
while True:
    guess = int(input())
    if guess == 0:
        break
    else:
        response = input()
        inp[guess] = response
        if response == "right on":
            games.append(inp)
            inp = {}