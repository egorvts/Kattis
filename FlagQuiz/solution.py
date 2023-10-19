_ = input()
alternatives = []
for i in range(int(input())):
    alternatives.append(input().split(", "))

def calc_cost(alt1, alt2):
    cost = 0
    for i in range(len(alt1)):
        if alt1[i] != alt2[i]:
            cost += 1

    return cost


costs = []
for i in range(len(alternatives)):
    max_cost = 0
    for j in range(len(alternatives)):
        if i != j:
            max_cost = max(max_cost, calc_cost(alternatives[i], alternatives[j]))
    costs.append(max_cost)

result = []
min_cost = min(costs)
for i in range(len(alternatives)):
    if costs[i] == min_cost:
        print(", ".join(alternatives[i]))
    

# result = set()
# for i in range(len(alternatives[0])):
#     variants = []
#     counts = []
#     for j in range(len(alternatives)):
#         variants.append(alternatives[j][i])

#     for variant in variants:
#         counts.append(variants.count(variant))

#     for i in range(len(counts)):
#         if counts[i] == max(counts):
#             result.add(variants[i])

# print(", ".join(result))
