n,w=map(int,input().split())
A=list(map(int, input().split()))
s = set()
for i in range(n):
  if A[i]<=w:
    s.add(A[i])  
  for j in range(i+1,n,1):
    if A[i]+A[j]<=w:
      s.add(A[i]+A[j])  
    for k in range(j+1,n,1):
      if A[i]+A[j]+A[k]<=w:
        s.add(A[i]+A[j]+A[k])
print(len(s))