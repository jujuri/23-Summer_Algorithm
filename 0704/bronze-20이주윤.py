import sys
input = sys.stdin.readline

arr = [''] * 5
ans = []

for i in range(5):
    inp = input().strip()
    arr[i] = inp
    if 'FBI' in inp:
        ans.append(i+1)

if len(ans) == 0:
    print("HE GOT AWAY!")
else:
    for i in ans:
        print(i, end=" ")
