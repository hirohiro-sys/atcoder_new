n,t = map(int,input().split())
a = list(map(int, input().split()))

rem = t % sum(a)
sum_val = 0
for i in range(n):
    if sum_val + a[i] > rem:
        print(i + 1, rem - sum_val)
        break
    sum_val += a[i]
