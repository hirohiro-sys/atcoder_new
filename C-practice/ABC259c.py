# モジュールをインポート
from itertools import groupby

# 2つの文字列SとTを入力
S = input()
T = input()

# 文字列を連続した部分文字列に分割し、タプルのリストに変換
S = [(a, len(list(b))) for a, b in groupby(S)]
T = [(a, len(list(b))) for a, b in groupby(T)]

# SとTの部分文字列の数が異なる場合、Tを生成できないので "No" と出力してプログラム終了
if len(S) != len(T):
    print("No")
    exit()

# SとTの対応する部分文字列を比較
for (s, i), (t, j) in zip(S, T):
    # 最初の文字が異なる場合、Tを生成できないので "No" と出力してプログラム終了
    if s != t:
        print("No")
        exit()

    # 同じ文字の連続回数が一致する場合、何もせずに次の部分文字列を比較
    if i == j:
        continue

    # Sの連続回数が2以上であり、Tの連続回数がS以上の場合、次の部分文字列を比較
    elif i >= 2 and j >= i:
        continue

    # 上記の条件に該当しない場合、Tを生成できないので "No" と出力してプログラム終了
    else:
        print("No")
        exit()

# すべての条件を満たす場合、TがSから生成できると判断し、"Yes" と出力
print("Yes")
