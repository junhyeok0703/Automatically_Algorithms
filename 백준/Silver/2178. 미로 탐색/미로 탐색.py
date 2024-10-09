# 4방향
# 1,1 -> N,M
from collections import deque

n, m = map(int,input().split())
maplist = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
visited = [[False]*(m+1) for _ in range(n+1)]
for i in range(n):
    maplist.append(list(map(int,input())))
def BFS(x,y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maplist[nx][ny] == 0:
                continue
            if maplist[nx][ny] == 1:
                maplist[nx][ny] = maplist[x][y]+1
                queue.append((nx,ny))

    return maplist[n-1][m-1]


print(BFS(0,0))