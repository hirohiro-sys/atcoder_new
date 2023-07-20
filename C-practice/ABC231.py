# 二分探索ライブラリ
import bisect
# 入力
n,q = map(int,input().split())
a = list(map(int,input().split()))
# 二分探索するためにsort
a.sort()
# 二分探索して出力
for i in range(q):
  x = int(input())
  y = bisect.bisect_left(a,x)
  print(n-y)

'''
C問題で計算量を減らすにはsortやset、または二分探索などのアルゴリズムを使う
'''
