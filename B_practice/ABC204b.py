n = int(input())
li = list(map(int,input().split()))
re = 0
for i in li:
  if i<=10:
    re+=0
  else:
    re+=(i-10)
print(re)