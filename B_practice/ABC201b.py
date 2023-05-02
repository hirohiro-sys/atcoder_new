n = int(input())
li = []
for i in range(n):
  a,b = input().split()
  b = int(b)
  li.append([b,a])
li.sort(reverse=True)
print(li[1][1])