n,x = map(int,input().split())
li = list(map(int,input().split()))
tmp = []
for i in range(n):
  if li[i]!=x:
    tmp.append(li[i])
print(*tmp)