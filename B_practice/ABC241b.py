n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
for i in range(m):
  if b[i] not in a:
    exit(print("No"))
  else:
    a.remove(b[i])
print("Yes")