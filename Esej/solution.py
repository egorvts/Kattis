from string import ascii_lowercase
from random import randint
a, b = map(int, input().split())

letters = ascii_lowercase
text = []
for i in range(b):
    word = []
    for j in range(randint(1, 15)):
        word.append(letters[randint(0, 25)])
    text.append("".join(word))

print(" ".join(text))