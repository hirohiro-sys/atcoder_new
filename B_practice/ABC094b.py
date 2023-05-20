n,m,x = map(int,input().split())
li = list(map(int,input().split()))
tmp = [i for i in range(0,n+1)]
tmp1 = 0
tmp2 = 0
for i in range(x,n+1):
  if tmp[i] in li:
    tmp1+=1
for i in range(0,x+1):
  if tmp[i] in li:
    tmp2+=1
print(min(tmp1, tmp2))