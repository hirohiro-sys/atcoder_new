# 入力
n,w = map(int,input().split())

# 可能なピザの美味しさの最大値を求めるためvを降順でソートする
v = []
for _ in range(n):
    a,b = map(int,input().split())
    v.append((a,b))
v.sort(reverse=True)

# メイン処理
res = 0
for a,b in v:
    # もしwが0以下になったら処理をやめる
    if w<=0:
        break
    take = min(w,b)
    # 美味しさを求めて足す
    res += take * a
    w -= take

# 出力
print(res)
