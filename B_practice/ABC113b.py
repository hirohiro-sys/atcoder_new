n = int(input())
t,a = map(int,input().split())
h = list(map(int,input().split()))
tmp = []
for i in range(n):
  tmp.append(abs(a-(t-h[i]*0.006)))
print(tmp.index(min(tmp))+1)