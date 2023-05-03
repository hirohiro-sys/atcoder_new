n = int(input())
num = 0
count = 0 
for i in range(1, 10**9+1):
  num += i
  count += 1
  if num>=n:
    print(count)
    exit()