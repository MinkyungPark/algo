n, m = map(int, input().split())
par = list(range(n+1))

def find(x):
    chk = []
    while x != par[x]:
        chk.append(x)
        x = par[x]
    for i in chk:
        par[i] = x
    return x

def union(x, y):
    px = find(x)
    py = find(y)
    if px != py:
        par[px] = py

buf = []
for i in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    else:
        buf.append("YES" if find(a) == find(b) else "NO")

print("\n".join(buf))