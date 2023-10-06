# 順列全探索のためのライブラリ
from itertools import permutations

# 入力
li = []
for _ in range(3):
    li += list(map(int,input().split()))

# 縦横斜めの列の一覧
cand = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

# がっかりした時はFalse、そうじゃない時はTrueを返す関数
def check(p):
    for a,b,c in cand:
        for _ in range(3):
            if li[a]==li[b] and p.index(a)<p.index(c) and p.index(b)<p.index(c):
                return False
            a,b,c = b,c,a
    return True

# がっかりしなかった組み合わせを数える
ans = 0
for p in permutations(range(9)):
    if check(p):
        ans += 1
        
        
'''
がっかりしなかった組み合わせを0~8までの
全ての順列の総数362880で割るとがっかりせずに
マスに書かれた数字を知る確率を求めれる
'''
print(ans/362880)
