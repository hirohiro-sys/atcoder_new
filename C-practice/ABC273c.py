# 二分探索ライブラリ
import bisect
N = int(input())
A = list(map(int,input().split()))
B = list(set(A))
B.sort()
count = [0]*N
for i in range(N):
  # 重複がなく昇順に並んでいる配列BからA[i]のインデックスを取得するメソッド
  count[len(B)-bisect.bisect_right(B,A[i])] += 1
print(*count)
