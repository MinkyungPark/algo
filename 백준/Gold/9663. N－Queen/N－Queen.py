N = int(input())

def dfs(r, queens):
    global cnt
    if r == N:
        cnt += 1
        return
    
    for c in range(N):
        check = True
        queens[r] = c # queens (r,c)
        for prev_r in range(r):
            prev_c = queens[prev_r]
            # promising
            # 이전 퀸과 같은 r,c거나 대각선이거나
            if prev_c == c or abs((r - prev_r) / (c - prev_c)) == 1:
                check = False
                break
        if check:
            dfs(r + 1, queens)

cnt = 0
dfs(0, [0] * N)
print(cnt)