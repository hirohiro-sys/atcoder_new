# 入力
N = int(input())
S, T = [], []
for i in range(N):
    s,t = input().split()
    S.append(s)
    T.append(int(t))

# 最高点のインデックスと最高点を格納する変数
best = -1
best_score = -1

# メイン処理
# appearedにオリジナルの値を入れてく過程でもしbest_scoreより高い値を出てきたら２つの変数更新
appeared = set()
for i in range(N):
    if S[i] in appeared:
        continue
    appeared.add(S[i])
    if best_score < T[i]:
        best = i
        best_score = T[i]

# 出力
print(best + 1)

'''
計算量を減らす必要がある場合、集合のデータ構造と使うときが多い
'''
