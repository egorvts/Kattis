candidates = {}

max_votes = 0
while True:
    candidate = input()
    if candidate == "***":
        break
    if candidate in candidates:
        candidates[candidate] += 1
        if candidates[candidate] > max_votes:
            max_votes = candidates[candidate]
    else:
        candidates[candidate] = 1
        if 1 > max_votes:
            max_votes = 1

if list(candidates.values()).count(max_votes) > 1:
    print("Runoff!") 
else:
    print([c for c in candidates if candidates[c] == max_votes][0])

