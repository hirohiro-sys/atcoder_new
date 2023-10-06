# 入力
n,m,k = map(int,input().split())

# 二次元のdpテーブル初期化 行数はn+1 列数はk+1
dp = [[0]*(k+1) for _ in range(n+1)]
dp[0][0] = 1

# メイン処理
for i in range(n):
    for j in range(k+1):
        for a in range(1,m+1):
            if dp[i][j] > 0 and j+a <= k:
                dp[i+1][j+a] += dp[i][j]

# 出力
print(sum(dp[n])%998244353)
