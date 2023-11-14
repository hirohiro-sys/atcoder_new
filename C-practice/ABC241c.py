# マスを6つ以上繋げられるか判定する関数
def calc(x,y,dx,dy):
    count = 0
    for i in range(6):
        # マスからはみ出しだらアウト
        if not (0<=min(x,y) and max(x,y)<N):
           return False
        if S[x][y] == "#":
            count += 1
        # 次のマスへ移動
        x += dx
        y += dy
    # 4つ以上黒く塗られていればOK
    return count >= 4

# calcを使って順に探索
N = int(input())
S = [input() for _ in range(N)]
Dx = [1,0,1,1]
Dy = [0,1,1,-1]
for i in range(N):
    for j in range(N):
        for dx,dy in zip(Dx,Dy):
            if calc(i,j,dx,dy):
                print("Yes")
                exit()
print("No")

"""
関数で処理を共通化することで少ないコードでシンプルに実装できる
"""
