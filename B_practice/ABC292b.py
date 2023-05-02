n,q = map(int,input().split())
li = [0]*n
for _ in range(q):
  a,b = map(int,input().split())
  if a==1:
    li[b-1]+=1
  elif a==2:
    li[b-1]+=2
  else:
    print("Yes" if li[b-1]>=2 else "No")