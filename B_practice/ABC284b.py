n = int(input())
for i in range(n):
  m = int(input())
  li = list(map(int,input().split()))
  count = 0
  for j in li:
    if j % 2 !=0:
      count += 1
  print(count)  