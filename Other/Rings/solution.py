rows, columns = map(int, input().split())

img = []

for _ in range(rows):
    img.append(list(input()))

max_ring = 0


def calc_rings(ts_count):
    max_ring_row = ts_count // 2
    global max_ring

    if ts_count % 2 == 0:
        max_ring = max(max_ring, max_ring_row)
        return list(range(1, max_ring_row+1)) + list(range(max_ring_row, 0, -1))
    else:
        max_ring = max(max_ring, max_ring_row+1)
        return list(range(1, max_ring_row+2)) + list(range(max_ring_row, 0, -1))


for i in range(rows):
    ts_count = img[i].count("T")
    rings = calc_rings(ts_count)
    result = []
    for j in range(ts_count):
        result.append(rings[j])
    print(result)
