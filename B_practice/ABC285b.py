#問題文通り実装
n = int(input())
s = input()
for i in range(1,n):
  k = 0
  while k+i<=n and s[k]!=s[k+i]:
    k+=1
  print(k)