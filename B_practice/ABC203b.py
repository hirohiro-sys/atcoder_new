n,k = map(int,input().split())
re = 0
for i in range(1,n+1):
  for j in range(1,k+1):
    re += int(str(i)+"0"+str(j))
print(re)