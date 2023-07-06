# 入力
N, M, H, K = map(int,input().split())
S = input()
items = set(tuple(map(int,input().split())) for _ in range(M))

# 愚直シミュレーション
res = True
x,y = 0,0
for i in S:
    if i == "R":
        x += 1
    elif i == "L":
        x -= 1
    elif i == "U":
        y += 1
    else:
        y -= 1
    
    H -= 1
    if H < 0:
        res = False
    
    if (x,y) in items and H < K:
        H = K
        items.remove((x,y))

# 出力
print("Yes" if res else "No")
