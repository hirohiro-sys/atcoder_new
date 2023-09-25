N = int(input())
p = list(map(int,input().split()))
ok=[0]*N
for i in range(N):
    res=p[i]-i
    ok[(res-1)%N]+=1
    ok[res%N]+=1
    ok[(res+1)%N]+=1
print(max(ok))
