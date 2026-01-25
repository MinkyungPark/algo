is_Y = [0] * 25
for i in range(5):
    for j, p in enumerate(input()):
        if p == 'Y':
            is_Y[i * 5 + j] = 1

adj = [0] * 25
for i in range(5):
    for j in range(5):
        pos = 5 * i + j
        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            if (0 <= ni < 5) and (0 <= nj < 5):
                adj[pos] |= 1 << (ni * 5 + nj)


def dfs(depth, last, combs, y_cnt):
    global ans
    if y_cnt > 3:
        return
    if depth == 7:
        ans += 1
        return
    
    for i in range(last):
        cur = 1 << i
        if cur & combs: # remove repeated combs
            continue
        if not adj[i] & combs: # backtrack not adj 
            continue
        new_combs = combs | cur
        if new_combs not in visited:
            visited.add(new_combs)
            dfs(depth + 1, last, new_combs, y_cnt + is_Y[i])


visited = set() # backtrack not expand same mask
ans = 0
for l in range(6, 25):
    visited.add(1 << l)
    dfs(1, l, 1 << l, is_Y[l])

print(ans)