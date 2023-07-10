import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
for i in range(n-1):
    inp = list(map(int,input().split()))
    for j in inp:
        if j > arr[0]:
            heapq.heappop(arr)
            heapq.heappush(arr,j)

print(arr[0])
