n,m = map(int,input().split())
li = [[] for _ in range(n)]
for i in range(m):
  a,b = map(int,input().split())
  li[a-1].append(b)
  li[b-1].append(a)
for i, l in enumerate(li):
  l.sort()
  print(len(l),*l)