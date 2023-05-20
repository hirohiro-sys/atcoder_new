n = int(input())
k = int(input())
li = list(map(int,input().split()))
re = 0
for i in range(n):
  if li[i]<k-li[i]:
    re+=li[i]*2
  elif li[i]>k-li[i]:
    re+=(k-li[i])*2
  else:
    re+=li[i]*2
print(re)