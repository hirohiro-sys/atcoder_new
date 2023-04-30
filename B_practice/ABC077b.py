import math
n = int(input())
for i in range(n,0,-1):
  if i//math.sqrt(i)==math.sqrt(i):
    print(i)
    exit()