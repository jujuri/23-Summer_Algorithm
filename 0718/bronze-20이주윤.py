import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    inp = int(input())
    arr.append(inp)
left = 1
mini = arr[0]
for i in range(1, n):
    if arr[i] > mini:
        left += 1
        mini = arr[i]
right = 1
maxi = arr[-1]
for i in range(n-2, -1, -1):
    if arr[i] > maxi:
        right += 1
        maxi = arr[i]
print(left)
print(right)
