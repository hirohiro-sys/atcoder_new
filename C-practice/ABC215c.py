#順列生成ライブラリ
from itertools import permutations

n,m = input().split()
m = int(m)

li = set()
for i in permutations(n):
  li.add(i)

print(*sorted(li)[m-1],sep="")
