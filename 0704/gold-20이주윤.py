import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
farm = [[0] for i in range(n)]
for i in range(n):
    inp = list(map(int, input().split()))
    farm[i] = inp
    
rslt = 0
visited = [[False] * m for i in range(n)]
def bfs(a, b):
    global ans
    dx = [0, 0, 1, -1, -1, 1, -1, 1]
    dy = [1, -1, 0, 0, -1, -1, 1, 1]
    
    queue = deque()
    queue.append([a, b])
    
    visited[a][b] = True
    flag = False    

    while queue:   
        x, y = queue.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif farm[nx][ny] > farm[x][y]:
                flag = True
            elif visited[nx][ny]:
                continue
            elif farm[nx][ny] == farm[x][y]:
                visited[nx][ny] = True
                queue.append([nx, ny])
                                    
    if not flag:
        ans += 1
    return ans
ans = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            bfs(i, j)
print(ans) 
