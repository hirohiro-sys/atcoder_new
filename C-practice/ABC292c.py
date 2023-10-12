N = int(input())

num = [0] * (N+1)
for x in range(1,N+1):
    for y in range(1,N//x+1):
        num[x*y] += 1
ans = 0
for v in range(1,N+1):
    ans += num[v] * num[N-v]
print(ans)
