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


def solution(game: dict) -> str:
    final_guess = list(game.keys())[-1]

    for i in game:
        response = game[i]
        if response == "too low" and final_guess < i:
            return "Stan is dishonest"
        elif response == "too high" and final_guess > i:
            return "Stan is dishonest"
        elif response == "right on" and final_guess != i:
            return "Stan is dishonest"

    return "Stan may be honest"


for game in games:
    print(solution(game))
