def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visit = [[False] * m for _ in range(n)]
    visit[0][0] = True
    queue = [(0, 0, 1)]
    
    while queue:
        x, y, cnt = queue.pop(0)
        
        if x == n - 1 and y == m - 1:
            return cnt
        
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and maps[nx][ny] == 1:
                visit[nx][ny] = True
                queue.append((nx, ny, cnt + 1))
                
    return -1
    