n,k = map(int,input().split())
A = list(map(int,input().split()))
li = []
for i in range(1,n+1):
  if i%2==0:
    li.append(A[i-1] - 1)
  else:
    li.append(A[i-1])
  
if sum(li)<=k:
  print("Yes")
else:
  print("No")