n = int(input())
li = list(map(int,input().split()))
count = 0
for i in range(n-2):
  if li[i] < li[i+1] < li[i+2] or li[i] > li[i+1] > li[i+2]:
    count += 1
print(count)