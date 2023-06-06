n = int(input())
li = list(map(int,input().split()))
count = 0
while True:
  for i in range(n):
    if li[i]%2!=0:
      exit(print(count))
      
  for i in range(n):
    li[i] = li[i]//2
  count += 1