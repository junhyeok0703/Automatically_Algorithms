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
    queue = deque([V]) # 처음에 방문한 친구 큐에 넣어
    visited_bfs[V] = True # 처음 방문한 친구 방문했다고해
    while queue:# q가 없을떄까지
        current = queue.popleft()# 큐Pop해서 v에 넣고 출력해
        print(current, end=' ')  # 공백을 출력에 추가
        for next_vertex in maplist[current]:# 큐pop인덱스를 그래프에 넣고 확인해
            # 계속 bfs pop한거의 인접리스트 다 보고 또 그다음에 방문안한곳가서
            # 인접리스트 다보고
            if not visited_bfs[next_vertex]:# 만약 list안에 방문하지않았을경우
                queue.append(next_vertex)#큐에다가 삽입하고
                visited_bfs[next_vertex] = True# 방문했다고해


dfs(V)
print()  
bfs(V)
print()  # 줄바꿈
