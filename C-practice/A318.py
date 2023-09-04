n,d,p = map(int,input().split())
F = list(map(int,input().split()))
F.sort(reverse=True)
ans = 0
for i in range(0,n,d):
    ans += min(p,sum(F[i:i+d]))
print(ans)
