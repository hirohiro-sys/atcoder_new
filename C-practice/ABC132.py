"""(公式解説)
まずはソートしよう。
ソートして、N/2-1個目とN/2個目の間を見れば整数Kの取りうる範囲が分かる。
N/2-1個目の数をA, N/2個目の数をBとすると、条件を満たすKの範囲は(A,B]となる。
つまり条件を満たすKの個数はB-Aとなり、これが答え。
"""

#　自分のコード
n = int(input())
d = sorted(map(int,input().split()))
print(d[n//2]-d[n//2-1])
