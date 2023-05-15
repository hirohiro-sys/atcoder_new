n = int(input())
li = list(map(int,input().split()))
for i in range(n-1):
  if li[i] >= li[i+1]:
    exit(print(li[i]))
print(li[-1])