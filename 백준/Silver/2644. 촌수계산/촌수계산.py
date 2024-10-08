from collections import deque

n = int(input())
maplist = [[] for _ in range(n+1)]
target1 , target2 = map(int,input().split())

vistied = [False]*(n+1)
def bfs(start,vistied):
    queue = deque([(start,0)])
    vistied[start]=True
    while queue:
        v,dis= queue.popleft()
        if v==target2:
            return dis
        for i in maplist[v]:
            if vistied[i]==False:
                vistied[i]=True
                queue.append((i,dis+1))
    return -1




k = int(input())
for i in range(k):
    a,b = map(int,input().split())
    maplist[a].append(b)
    maplist[b].append(a)


print(bfs(target1,vistied))