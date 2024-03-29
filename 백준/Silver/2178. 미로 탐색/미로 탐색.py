import sys
input = sys.stdin.readline
from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and nm[nx][ny] == 1:
                nm[nx][ny] = nm[x][y]+ 1
                queue.append((nx,ny))
    return nm[n-1][m-1]


n,m = map(int,input().split())

nm = []
temp = [[0] * m for i in range(n)]
for i in range(n):
    nm.append(list(map(int,input().rstrip())))

print(bfs(0,0))