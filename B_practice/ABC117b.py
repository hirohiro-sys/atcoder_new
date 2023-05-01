n = int(input())
li = list(map(int,input().split()))
if sum(li)-max(li)>max(li):
  print("Yes")
else:
  print("No")