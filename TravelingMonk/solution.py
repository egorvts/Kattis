E = 0.1

a, d = map(int, input().split())

total_distance = 0

ascent = []
ascent_time = 0
for i in range(a):
    h, t = map(int, input().split())
    ascent_time += t
    total_distance += h
    ascent.append((h, t))

descent = []
descent_time = 0
for i in range(a):
    h, t = map(int, input().split())
    descent_time += t
    descent.append((h, t))

time = 0
ascent_ind = 0
descent_ind = 0

ascent_distance = 0
descent_distance = total_distance

min_time = min(ascent[ascent_ind][1], descent[descent_ind][1])
while True:
    print(time, ascent_distance, descent_distance)
    if ascent_distance > descent_distance:
        time -= min_time
        ascent_distance -= ascent[ascent_ind]
        descent_distance -= descent[descent_ind]
        while abs(ascent_distance - descent_distance) >= E:
            new_time = time + min_time/2
             
    if ascent[ascent_ind][1] == min_time:
        time += ascent[ascent_ind][1]
        ascent_distance += ascent[ascent_ind][0]
        descent_distance -= (ascent[ascent_ind][1] / descent[descent_ind][1]) * descent[descent_ind][0]
        ascent_ind += 1
    else:
        time += descent[descent_ind][1]
        ascent_distance += (descent[descent_ind][1] / ascent[ascent_ind][1]) * ascent[ascent_ind][0]
        descent_distance -= descent[descent_ind][0]
        descent_ind += 1
