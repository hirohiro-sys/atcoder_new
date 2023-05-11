n = int(input())
li1 = list(map(int,input().split()))
li2 = list(map(int,input().split()))
re = 0
for i in range(n):
  re += li1[i]*li2[i]
if re==0:
  print("Yes")
else:
  print("No")