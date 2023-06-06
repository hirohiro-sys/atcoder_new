n,y = map(int,input().split())
for i in range(n+1):
  for j in range(n-i+1):
    if 10000*i+5000*j+1000*(n-j-i)==y:
      exit(print(i,j,n-j-i))
print(-1,-1,-1)