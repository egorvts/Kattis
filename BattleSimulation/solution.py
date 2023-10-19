moves = input()
len_moves = len(moves)

combos = ["RBL", "BLR", "LRB", "LBR", "BRL", "RLB"]
replacements = {"R": "S", "B": "K", "L": "H"}
result = []

i = 0
while i < len_moves:
    if moves[i:i+3] in combos:
        result.append("C")
        i += 3
    else:
        result.append(replacements[moves[i]])
        i += 1

print("".join(result))
