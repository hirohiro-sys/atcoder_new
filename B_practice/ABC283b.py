#問題文よく読む　そのまま実装
n = int(input())
li = list(map(int,input().split()))
q = int(input())
for i in range(q):
  tmp = list(map(int,input().split()))
  if len(tmp)==2:
    print(li[tmp[1]-1])
  else:
    li[tmp[1]-1]=tmp[2]