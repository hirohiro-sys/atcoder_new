import itertools

# 文字列 A, Bの文字が異なる箇所の個数を求める関数
def diff(A,B):
    res = 0
    for a, b in zip(A, B):
        if a!=b:
            res += 1
    return res

# 入力
N,M = map(int,input().split())
S = [input() for _ in range(N)]
S.sort()

# 順列全探索
for T in itertools.permutations(S):
    ok = True
    for i in range(N - 1):
        if diff(T[i],T[i+1]) != 1:
            ok = False
    
    # 出力
    if ok:
        exit(print("Yes"))
print("No")

'''
それぞれ異なる場所が一箇所かどうかを調べる
'''
