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
for tea in tea_prices:
    cheapest_topping = min(topping_pairs[tea_prices.index(tea)])
    possible_variants.append(tea + cheapest_topping)

print((x // min(possible_variants)) - 1)
