k,n = map(int,input().split())
A = list(map(int,input().split()))
A += [k+A[0]]
for i in reversed(range(1,n+1)):
  A[i]-=A[i-1]
print(k-max(A[1:]))
