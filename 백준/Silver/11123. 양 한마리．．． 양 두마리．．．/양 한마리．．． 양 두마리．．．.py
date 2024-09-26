from collections import deque

t = int(input())
resultarr = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph,x,y,visited,w,h):
    queue = deque()
    queue.append((x,y))
    visited[x][y]= True
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx =  x + dx[i]
            ny =  y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:  
                if not visited[nx][ny] and graph[nx][ny] == '#':
                    queue.append((nx, ny))
                    visited[nx][ny] = True



for _ in range(t):
    h,w = list(map(int,input().split()))
    cnt=0
    maplist = []

    for x in range(h):
        maplist.append(list(input()))

    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and maplist[i][j]=='#':
                bfs(maplist,i,j,visited,w,h)
                cnt+=1
    resultarr.append(cnt)

for i in resultarr:
    print(i)