h,w = map(int,input().split())
a = [0 for _ in range(h)]
b = [0 for _ in range(w)]
for i in range(h):
  c = list(input())
  for j in range(w):
    if c[j]=="#":
      a[i]+=1
      b[j]+=1
print(a.index(max(a)-1)+1, b.index(max(b)-1)+1)
