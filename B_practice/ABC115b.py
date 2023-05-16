n = int(input())
li = [int(input()) for _ in range(n)]
mx = max(li)
for i in range(n):
  if li[i]==max(li):
    li[i] = li[i]//2
    exit(print(sum(li)))