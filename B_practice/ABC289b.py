#自分が書いたコードをトレースしながら確認するとわかりやすい
n,m = map(int,input().split())
li = list(map(int,input().split()))

num = []
temp = []
re = []
for i in range(1,n+1):
  num.append(i)
if li==False:
  print(*num)
  exit()

for i in range(n):
  if num[i] in li:
    temp.append(num[i])
  else:
    re.append(num[i])
    for _ in range(len(temp)):
      re.append(temp[-1])
      temp.pop()
  
print(*re)