import sys 
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
heapq.heapify(heap)
for i in range(n):
    inp = int(input())
    if inp == 0:
        if len(heap) > 0:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, inp)
