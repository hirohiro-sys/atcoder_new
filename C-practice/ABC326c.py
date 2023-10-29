# 2つの整数 n と m を受け取る
n, m = map(int, input().split())

# 整数リスト a を受け取り、リストとして格納する
a = list(map(int, input().split()))

# リスト a を昇順にソートする
a.sort()

# リスト a の末尾に非常に大きな数を追加する（要素の差が m を超えないようにするトリック）
a.append(9000000000000)

# 結果の変数 res を初期化（連続する要素の最大数）
res = 0

# 右側のインデックス r を初期化
r = 0

# リスト a の各要素を左からスキャンする
for l in range(0, n):
    # 右側の要素が m 以下の差を持つまで r を増加させる
    while a[r] < a[l] + m:
        r += 1

    # 連続する要素の最大数を更新
    res = max(res, r - l)

# 結果を出力
print(res)
