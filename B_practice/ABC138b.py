n = int(input())
li = list(map(int,input().split()))
re = 0
for i in range(n):
  re += 1/li[i]
print(1/re)