from collections import deque

# 입력 받기
N, M, V = map(int, input().split())

# 인접 리스트 생성
maplist = [[] for _ in range(N + 1)]

# 간선 정보 입력 받기
for _ in range(M):
    v1, v2 = map(int, input().split())
    maplist[v1].append(v2)
    maplist[v2].append(v1)

# 정점 번호가 작은 순서대로 방문하도록 정렬
for adj in maplist:
    adj.sort()

# DFS 탐색
visited_dfs = [False] * (N + 1)

def dfs(V):
    visited_dfs[V] = True
    print(V, end=' ')  # 공백을 출력에 추가
    for next_vertex in maplist[V]:
        if not visited_dfs[next_vertex]:
            dfs(next_vertex)

# BFS 탐색
visited_bfs = [False] * (N + 1)

def bfs(V):
    queue = deque([V])
    visited_bfs[V] = True
    while queue:
        current = queue.popleft()
        print(current, end=' ')  # 공백을 출력에 추가
        for next_vertex in maplist[current]:
            if not visited_bfs[next_vertex]:
                queue.append(next_vertex)
                visited_bfs[next_vertex] = True

# 결과 출력
dfs(V)
print()  # 줄바꿈
bfs(V)
print()  # 줄바꿈
