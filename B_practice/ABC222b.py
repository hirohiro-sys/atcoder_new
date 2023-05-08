n,p = map(int,input().split())
li = list(map(int,input().split()))
count = 0
for i in range(n):
  if li[i]<p:
    count += 1
print(count)