from itertools import product
p = list(product([1, 2, 3, 4, 5], repeat=5))

cnt = 0
for i in p:
    if i.count(1) == 3:
        cnt += 1

print(cnt)