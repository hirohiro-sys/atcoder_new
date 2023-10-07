# 入力
n,m = map(int,input().split())
a = list(map(int,input().split()))
s = [input() for _ in range(n)]

# 点数初期化(+1している理由は問題文に記載してある)
now_sc = [i+1 for i in range(n)]

# 各プレイヤーの得点を計算
for i in range(n):
    for j in range(m):
        if s[i][j]=="o":
            now_sc[i] += a[j]

# 得点の最大値を求める
mx = max(now_sc)

# 各プレイヤーが残り何問解く必要があるか求めるfor文
for i in range(n):
    # xの部分の得点を格納するリスト
    nokori = [a[j] for j in range(m) if s[i][j] == "x"]
    nokori.sort(reverse=True)

    # 現在の点数が最大の点数を超えるまで足す
    ans = 0
    while now_sc[i] < mx:
        now_sc[i] += nokori[ans]
        ans += 1
    
    # 出力
    print(ans)


'''
愚直シミュレーション問題
'''
