#貪欲解
from math import factorial
n = int(input())
count = 0
for i in range(10,0,-1):
  while n>=factorial(i):
    n-=factorial(i)
    count += 1
print(count)