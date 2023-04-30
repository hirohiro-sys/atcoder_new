n = int(input())
li = list(map(int,input().split()))
li2 = []
li3 = []
for i in li:
  if i%2==0:
    li2.append(i)
    
for i in li2:
  if i%3==0 or i%5==0:
    li3.append(i)
  
if li2==li3:
  print("APPROVED")
else:
  print("DENIED")