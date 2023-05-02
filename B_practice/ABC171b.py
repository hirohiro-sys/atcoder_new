n,k = map(int,input().split())
li = list(map(int,input().split()))
li.sort()
re = 0
for i in range(k):
  re += li[i]
print(re)