a,b,c = map(int,input().split())
for i in range(1,201):
  if a*i%b==c:
    exit(print("YES"))
print("NO")