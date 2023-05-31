n,m = map(int,input().split())
li = list(map(int,input().split()))
s = 0
for i in range(m):
  s += li[i]
  if s>n:
    exit(print(-1))
print(n-s)