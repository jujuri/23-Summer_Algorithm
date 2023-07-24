import sys
input = sys.stdin.readline

n = input().strip()
left = n[:(len(n)+1)//2]
if n == '9'*len(n):
    print(int(n)+2)
elif len(n) == 1:
    print(int(n)+1)
elif len(n) % 2 == 0:
    tmp = left + left[::-1]
    if int(tmp) > int(n):
        print(tmp)
    else:
        tmp = str(int(left)+1)
        tmp = tmp[:] + tmp[::-1]
        print(tmp)          
else:
    tmp = left + left[-2::-1]
    if int(tmp) > int(n):
        print(tmp)
    else:
        tmp = str(int(left)+1)
        tmp = tmp[:] + tmp[-2::-1]
        print(tmp)  
