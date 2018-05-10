# TODO
import heapq
def heapsort(arr):
    hp = []
    for item in arr:
        heapq.heappush(hp, item)
    while hp:
        print(heapq.heappop(hp))


heapsort([3, 10, 8, 2, 9])
