import math as m
from random import randint

def slowSolution(inp):
    p, a, b, c, d, n = inp
    prices = []

    for k in range(1, n + 1):
        prices.append(p * (m.sin(a * k + b) + m.cos(c * k + d) + 2))

    diffs = []
    decline = 0

    for i in prices:
        for j in prices[prices.index(i):]:
            diffs.append(i - j)

    return max(diffs), prices

def solution(inp):
    p, a, b, c, d, n = inp
    prices = []


    for k in range(1, n + 1):
        prices.append(p * (m.sin(a * k + b) + m.cos(c * k + d) + 2))
    maxPrice = 0
    maxDiff = 0

    for i in range(0, len(prices) - 1):
        pricePrev = prices[i]
        priceNext = prices[i + 1]
        maxPrice = max(pricePrev, max(priceNext, maxPrice))
        if priceNext < pricePrev:
            if maxPrice - priceNext > maxDiff:
                maxDiff = maxPrice - priceNext

    return maxDiff, prices

def generateInput():
    return [randint(1, 1001), randint(0, 1001), randint(0, 1001), randint(0, 1001), randint(0, 1001), randint(1, 1001)]

def oracle() -> bool:
    inputs = [generateInput() for _ in range(100)]
    for inp in inputs:
        sol = solution(inp)
        slowSol = slowSolution(inp)
        if (sol != slowSol) and (inp[5] < 5):
            print(sol, slowSol)
            break
    return all(list(map(lambda inp: solution(inp) == slowSolution(inp), inputs)))

print(oracle())
#print(slowSolution([831, 833, 561, 908, 261, 267]))
#print(solution([831, 833, 561, 908, 261, 267]))
