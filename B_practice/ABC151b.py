n,k,m = map(int,input().split())
li = list(map(int,input().split()))
for i in range(k+1):
  if (sum(li)+i)//n>=m:
    exit(print(i))
print(-1)