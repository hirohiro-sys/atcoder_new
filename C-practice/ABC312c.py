# 入力
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Bの各要素に1を加えた新しいリストを生成し、Aと結合します
# そして、この結合されたリストを昇順にソートします
# 最終的なリストから、M番目の要素（0から始まるインデックスで）を取得して出力します
print(sorted(A + list(map(lambda x: x + 1, B)))[M - 1])

"""
二分探索でもできる
"""
