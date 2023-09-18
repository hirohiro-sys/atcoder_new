# 入力
M = int(input())
N = 3
S = [input() for _ in range(N)]

# メイン処理 
INF = 1e9
ans = INF
for i in range(N * M):
    for j in range(N * M):
        for k in range(N * M):
            if i != j and i != k and j != k and S[0][i % M] == S[1][j % M] == S[2][k % M]:
                ans = min(ans, max(i, j, k))

# 出力
print(ans if ans < INF else -1)

'''公式解説
リールが 
3 周するまでに数字を揃えられないなら永遠に揃えられません。よって、各ボタンを時刻 
0,1,…,3M-1 のうちいつ押すかをすべて試せば十分です。
'''
