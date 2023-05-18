n = int(input())
v = list(map(int,input().split()))
c = list(map(int,input().split()))
tmp = []
for i in range(n):
  if v[i]-c[i]>=0:
    tmp.append(v[i]-c[i])
print(sum(tmp))