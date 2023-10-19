import math as m


def calc_width(word, font):
    return m.ceil(9/16 * len(word) * font)


cloud_num = 1
while True:
    # w – max width; n – number of words
    max_width, n = map(int, input().split())
    if max_width == n == 0:
        break

    words = []
    max_count = 0  # number of occurrences of the most frequent word

    for i in range(n):
        w, c = input().split()
        c = int(c)
        max_count = max(max_count, c)
        if c < 5:
            continue
        else:
            words.append((w, c))

    words.sort(key=lambda x: x[0])

    def calc_font(c):
        return m.ceil(8 + ((40 * (c - 4)) / (max_count - 4)))

    current_width = max_width
    height = 0
    current_height = 0
    for word in words:
        w, c = word
        font = calc_font(c)
        width = calc_width(w, font)
        if current_width >= width:
            current_width -= width + 10  # Need to check if the word is last in the row
            current_height = max(current_height, font)
        else:
            current_width = max_width - width
            height += current_height
            current_height = font

    height += current_height

    print(f"CLOUD {cloud_num}: {int(height)}")
    cloud_num += 1
