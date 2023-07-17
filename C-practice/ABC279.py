# 入力
H,W = map(int, input().split())
S = list(input() for _ in range(H))
T = list(input() for _ in range(H))

# メイン処理
S = sorted(list(zip(*S)))
T = sorted(list(zip(*T)))
print("Yes") if S == T else print("No")

'''
中身を転置して全体の構造をsort
'''
