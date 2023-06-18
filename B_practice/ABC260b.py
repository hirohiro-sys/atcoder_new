#入力
n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

#合格した人の受験番号保持する場所
flag = [0] * n


# 数学
for _ in range(x):
    pos = -1
    for i in range(n):
        if not flag[i]:  # まだ合格が決まっていない人のうち
            if pos == -1 or a[i] > a[pos]:  # 現時点で一番優秀な人
                pos = i
    flag[pos] = 1

# 英語
for _ in range(y):
    pos = -1
    for i in range(n):
        if not flag[i]:  # まだ合格が決まっていない人のうち
            if pos == -1 or b[i] > b[pos]:  # 現時点で一番優秀な人
                pos = i
    flag[pos] = 1

# 数学+英語
for _ in range(z):
    pos = -1
    for i in range(n):
        if not flag[i]:  # まだ合格が決まっていない人のうち
            if pos == -1 or a[i] + b[i] > a[pos] + b[pos]:  # 現時点で一番優秀な人
                pos = i
    flag[pos] = 1

#出力
for i in range(n):
    if flag[i]:
        print(i+1)
