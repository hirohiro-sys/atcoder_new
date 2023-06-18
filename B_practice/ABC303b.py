#入力
n,m = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(m)]
#隣り合うペアを格納する集合（順番は考慮しない）
t = set()

for i in range(m):
  for j in range(n-1):
    a,b = li[i][j],li[i][j+1]
    #順番は考慮しないため左に小さい値,右に大きい値をおくと決める
    t.add((min(a,b),max(a,b)))
#全体の組み合わせの数から隣り合う組み合わせの数を引く
print(n*(n-1)//2-len(t))
　
