# nに整数を入力します。これはデータの数を表します。
n = int(input())

# データを整数のリストとして入力します。
data = list(map(int, input().split()))

# データの合計を計算し、平均値mを求めます。
m = sum(data) // n

# cu（カウントアップ）とcd（カウントダウン）変数を初期化します。
cu = 0  # カウントアップ変数 - 平均値以上の要素を平均値まで増やすための操作回数
cd = 0  # カウントダウン変数 - 平均値以下の要素を平均値まで減らすための操作回数

# データの各要素に対してループします。
for x in data:
    if x <= m:
        # 要素が平均値以下の場合、カウントアップ変数を増やします。
        cu += m - x
    else:
        # 要素が平均値より大きい場合、カウントダウン変数を増やします。
        cd += x - (m + 1)  # 平均値以下に減らすためには1を引きます。

# カウントアップとカウントダウンの操作回数のうち、大きい方を出力します。
# これは、平均値に近づけるために最小限の操作回数を計算します。
print(max(cu, cd))
