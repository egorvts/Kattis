trips = dict()
# trips_is_sorted = set()

for i in range(int(input())):
    country, year = input().split()
    if country in trips:
        trips[country].append(year)
    else:
        trips[country] = [year]

for t in trips:
    trips[t].sort()

print(trips)

for i in range(int(input())):
    country, trip_num = input().split()
    trip_num = int(trip_num)
    # if country not in trips_is_sorted:
    # trips[country].sort()
    # trips_is_sorted.add(country)
    print(trips[country][trip_num-1])
