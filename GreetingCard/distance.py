from math import sqrt

# for n in range(10, 100):
#     count = 0
#     print(n, end=": ")
#     for x in range(-n, n+1):
#         for y in range(-n, n+1):
#             if sqrt(x**2 + y**2) == n:
#                 count += 1
#     print(count)


for x in range(-85, 85+1):
    for y in range(-85, 85+1):
        if sqrt(x**2 + y**2) == 85:
            print(x, y)

    
