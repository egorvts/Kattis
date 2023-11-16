w, p = map(int, input().split())
partitions = [0] + list(map(int, input().split())) + [w]

widths = set()

for i in range(p+1):
    for j in range(i+1, p+2):
        # print(partitions[i], partitions[j])
        widths.add(partitions[j] - partitions[i])

print(" ".join(map(str, sorted(widths))))
