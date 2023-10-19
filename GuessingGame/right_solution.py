# Input
games = []
game = []

while True:
    guess = int(input())
    if guess == 0:
        break
    response = input()
    game.append((guess, response))
    if response == "right on":
        games.append(game)
        game = []

def solution(game: list) -> str:
    right = game[-1][0]
        
    for i in range(len(game)-1):
        guess = game[i][0]
        response = game[i][1]
        if response == "too high" and guess <= right:
            return "Stan is dishonest"
        elif response == "too low" and guess >= right:
            return "Stan is dishonest"
    return "Stan may be honest"
        
for game in games:
    print(solution(game))
