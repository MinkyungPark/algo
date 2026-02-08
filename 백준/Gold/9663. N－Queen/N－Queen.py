N = int(input())

def dfs(r, c_mask, dl, dr):
    # c_mask : cols prev queens attack
    # dl, dr : col prev queen diagonal
    global cnt
    if r == N:
        cnt += 1
        return
    
    vacant = ((1 << N) - 1) & ~(c_mask | dl | dr)
    while vacant:
        col = vacant & -vacant
        vacant -= col
        dfs(r + 1, c_mask | col, (dl | col) << 1, (dr | col) >> 1)

cnt = 0
dfs(0, 0, 0, 0)
print(cnt)