n,t = map(int,input().split())
tmp = []
for i in range(n):
  a,b = map(int,input().split())
  if t>=b:
    tmp.append(a)

if not tmp:
  print("TLE")
else:
  print(min(tmp))