# 入力
A = [list(map(int, input().split())) for _ in range(9)]

answer = list(range(1,10))
# 横ライン判定
for r in A:
    if sorted(r) != answer:
        print('No')
        quit()

# 縦ライン判定
for c in range(9):
    if sorted([r[c] for r in A]) != answer:
        print('No')
        quit()

# 3 x 3ブロック判定
for r in range(3):
    for c in range(3):
        cube = []
        rows = A[r*3:r*3+3]     
        for row in rows:
            cube += row[c*3:c*3+3]
        if sorted(cube) != answer:
            print('No')
            quit()

# 出力
print('Yes')

"""
解説AC
自分で実装できるように
"""
