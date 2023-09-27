# accumulateはリストを累積和で表現する
from itertools import accumulate
n,m = map(int,input().split())
A = list(map(int,input().split()))
B = [0] + list(accumulate(A))
ans = 0
for i in range(m):
    ans += A[i] *(i+1)
tmp = ans
for i in range(0,n-m):
    tmp += A[i+m]*m-(B[i+m]-B[i])
    ans = max(ans, tmp)
print(ans)
