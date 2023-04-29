h,w = map(int,input().split())
a = [input() for _ in range(h)]
b = [input() for _ in range(h)]
for i in range(h):
  for j in range(w):
    if a==b:
      print("Yes")
      exit()
    a = [x[1:]+x[:1] for x in a]
  a = a[1:]+a[:1]

print("No")