n = int(input())
count = 0
for _ in range(n):
  a,b = map(int,input().split())
  if a==b:
    count+=1
    if count >=3:
      print("Yes")
      exit()
  else:
    count = 0
print("No")