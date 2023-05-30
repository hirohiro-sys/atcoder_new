n = int(input())
li = list(map(int,input().split()))
tmp = []
for i in range(n-1):
  tmp.append(abs(sum(li[:i+1])-sum(li[i+1:])))
print(min(tmp))