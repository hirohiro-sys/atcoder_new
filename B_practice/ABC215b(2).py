#問題文通り実装する
n = int(input())
k = 0
while 2**k<=n:
  k+=1
  
print(k-1)