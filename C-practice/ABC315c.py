# 入力
n = int(input())
li = [tuple(map(int,input().split())) for _ in range(n)]

# タプルの2番目の値を基準に降順にソートする
li.sort(key=lambda x: x[1], reverse=True)

# 最大値を求めるメイン処理を問題文通り実装
ans = 0
for i in range(1,n):
    if li[0][0] == li[i][0]:
        ans = max(ans,li[0][1] + li[i][1] // 2)
    else:
        ans = max(ans, li[0][1] + li[i][1])

print(ans)

"""
tupleやsortで計算量を減らす工夫
"""
