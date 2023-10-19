l = int(input())
A = list(map(int, input().split()))
G = [A[0]]
for i in range(1, l):
    if A[i] > G[-1]:
        G.append(A[i])

print(len(G))
print(" ".join(map(str, G)))