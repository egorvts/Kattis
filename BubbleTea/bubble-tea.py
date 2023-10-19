n = int(input())  # amount of kinds of tea
tea_prices = list(map(int, input().split()))
m = int(input())  # amount of kinds of toppings
topping_prices = list(map(int, input().split()))

topping_pairs = {}  # toppings which can be paired with tea

for i in range(n):
    inp = list(map(int, input().split()))
    topping_pairs[i] = inp[1:]

x = int(input())  # amount of money

possible_variants = []
for tea in range(n):
    cheapest_topping = min(list(map(lambda t: topping_prices[t - 1], topping_pairs[tea])))
    possible_variants.append(tea_prices[tea] + cheapest_topping)

if x // (min(possible_variants)) == 0:
    print(0)
else:
    print(x // (min(possible_variants)) - 1)
