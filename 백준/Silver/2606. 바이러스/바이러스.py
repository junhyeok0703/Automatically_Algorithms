from collections import deque

c = int(input())
rks = int(input())
maplist = [[] for _ in range(c+1)]
for i in range(rks):
    v,t = list(map(int,input().split()))
    maplist[v].append(t)
    maplist[t].append(v)
vc = c+1
visited = [False] * vc

def bfs(v):
    queue=deque([v])
    visited[v]=True
    cnt = 0
    while queue:
        v = queue.popleft()
        for i in maplist[v]:
            if visited[i]==False:
                visited[i] = True
                queue.append(i)
                cnt += 1
    print(cnt)

bfs(1)