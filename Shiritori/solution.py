from sys import stdin, exit

used_words = set()
last_word = ""

for i in range(int(input())):
    word = stdin.readline()[:-1]
    used_words.add(word)
    if len(used_words) != i + 1 or (i != 0 and word[0] != last_word[-1]):
        print(f"Player {1 if i % 2 == 0 else 2} lost")
        exit(0)
    else:
        last_word = word

print("Fair Game")
