import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
cnt = 0
ans = 0

for i in arr:
    if i == 0:
        cnt = 0
    else:
        cnt += 1
    ans += cnt
print(ans)
