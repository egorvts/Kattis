for t in range(int(input())):
    n = int(input())
    votes = {}
    for i in range(n):
        votes[i] = int(input())
    votes_count = sum(votes.values())
    winner_votes = max(votes.values())
    if list(votes.values()).count(winner_votes) != 1:
        print("no winner")
    elif votes_count / winner_votes < 2:
        print(f"majority winner {list(votes.values()).index(winner_votes) + 1}")
    else:
        print(f"minority winner {list(votes.values()).index(winner_votes) + 1}")
