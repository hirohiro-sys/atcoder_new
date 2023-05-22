#普通にやる
a,b = map(int,input().split())
li = list(map(int,input().split()))
count = 1
sm = 0
for i in range(a):
  sm += li[i]
  if sm<=b:
    count+=1
print(count)