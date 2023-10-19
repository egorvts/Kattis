restaurants_count = int(input())
menus = {}

res = []
for r in range(restaurants_count):
    for i in range(int(input()) + 1):
        res.append(input())
    menus[res[0]] = res[1:]
    res = []

otp = []
for restaurant in menus:
    if "pea soup" in menus[restaurant] and "pancakes" in menus[restaurant]:
        otp.append(restaurant)

if otp:
    print(otp[0])
else:
    print("Anywhere is fine I guess")
