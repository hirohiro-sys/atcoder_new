from collections import Counter

# nを入力
n = int(input())

# リストaの入力と変換
a = list(map(int, input().split()))

# リストbの入力と変換
b = list(map(int, input().split()))

# リストcの入力と変換
c = list(map(int, input().split()))

# リストaの各要素の出現回数をカウントし、結果をcntに格納
cnt = Counter(a)

# 答えの初期化
ans = 0

# リストcの各要素に対して処理を行う
for i in c:
    # リストb内でi-1番目の要素が何回出現するかをカウントし、結果をansに加算
    ans += cnt[b[i - 1]]

# 最終的な答えを出力
print(ans)
