n,s,d = map(int,input().split())
for i in range(n):
  a,b = map(int,input().split())
  if a<s and b>d:
    exit(print("Yes"))
print("No")