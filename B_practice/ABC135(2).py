n = int(input())
li = list(map(int,input().split()))
count = 0
for i in range(n):
  if li[i]!=i+1:
    count += 1
if count <= 2:
  print("YES")
else:
  print("NO")