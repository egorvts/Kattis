# Input
attributes = list(input().split())

songs_count = int(input())
songs = []
for i in range(songs_count):
    song = list(input().split())
    songs.append(song)

sorts_count = int(input())
sorts = []
for i in range(sorts_count):
    sort = input()
    sorts.append(sort)

# Sorting
for sort in range(sorts_count):
    sort_ind = attributes.index(sorts[sort])
    songs.sort(key=lambda x: x[sort_ind])
    print(" ".join(attributes))
    for song in songs:
        print(" ".join(song))
    if sort != sorts_count-1:
        print()