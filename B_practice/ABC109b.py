n = int(input())
li = [input() for _ in range(n)]
for i in range(n-1):
  if  li[i][-1]!=li[i+1][0] or len(set(li))!=n:
    print("No")
    exit()
print("Yes")