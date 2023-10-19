capacity, stations = map(int, input().split())

def solution(capacity: int, stations: int) -> str:
    passengers = 0

    for stop in range(stations):
        left, entered, stayed = map(int, input().split())
        if passengers < 0:
            return "impossible"
        elif passengers - left < 0:
            return "impossible"
        elif passengers - left + entered > capacity or passengers - left + entered < 0:
            return "impossible"
        elif (capacity - passengers - entered + left > stayed) and stayed != 0:
            return "impossible"
        elif stop == 0 and (left != 0 or passengers != 0):
            return "impossible"
        elif (stop == stations - 1) and (entered != 0 or stayed != 0 or passengers - left != 0):
            return "impossible"
        else:
            passengers = passengers - left + entered
    return "possible"

print(solution(capacity, stations))