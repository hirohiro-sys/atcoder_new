n,m = map(int,input().split())
li = [input() for _ in range(n)]
li2 = [input() for _ in range(m)]
count = 0
for i in range(n):
  if li[i][-3:] in li2:
    count += 1
print(count)