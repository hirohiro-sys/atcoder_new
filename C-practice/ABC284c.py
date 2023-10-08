# 深さ優先探索をする関数
def dfs(c):
    vis[c] = True
    for d in g[c]:
        if not vis[d]:
            dfs(d)


N,M = map(int,input().split())
# 隣接リストを初期化
g = [[] for _ in range(N)]
# 訪問状態初期化
vis = [False] * N

# 隣接リスト構築
for _ in range(M):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

# 答えを求める
ans = 0
for i in range(N):
    if not vis[i]:
        ans += 1
        dfs(i)

print(ans)

'''
超基本的な深さ優先探索問題
'''
