n = int(input())
li = list(map(int,input().split()))
print(li[0],end=" ")
for i in range(n-1):
  print(li[i+1]-li[i],end=" ")