from collections import deque

batch = [input() for _ in range(5)]

def bfs(lis):
    visited = [[1] * 5 for _ in range(5)]
    for pos in lis[1:]:
        x, y = pos // 5, pos % 5
        visited[x][y] = 0
    
    visit_cnt = 1
    q = deque([(lis[0] // 5, lis[0] % 5)])
    while q:
        x, y = q.popleft()
        for dx, dy in zip([0, 1, -1, 0], [1, 0, 0, -1]):
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < 5 and 
                0 <= ny < 5 and 
                not visited[nx][ny]
            ):
                q.append((nx, ny))
                visit_cnt += 1
                visited[nx][ny] = 1
    
    return visit_cnt == 7

def dfs(pos, route, y_cnt):
    global cnt
    # backtrack
    if y_cnt > 3:
        return
    
    # check adjacency
    if len(route) == 7:
        if bfs(route):
            cnt += 1
        return

    for i in range(pos, 25):
        route.append(i)
        dfs(i + 1, route, y_cnt + int(batch[i // 5][i % 5] == 'Y'))
        route.pop()
        
cnt = 0
# combinations
dfs(0, [], 0)
print(cnt)