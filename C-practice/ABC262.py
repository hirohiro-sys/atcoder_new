# 入力
n = int(input())
a = list(map(int,input().split()))

# 0から始まるリストにする
for i in range(n):
    a[i] -= 1

# リストの各要素とインデックスが一致する回数
same = 0
for i,x in enumerate(a):
    if i == x:
        same += 1

# sameの組の総数を求める式
ans = same * (same - 1) // 2

# カウント
for i,j in enumerate(a):
    if i < j and a[j] == i:
        ans += 1

# 出力
print(ans)
