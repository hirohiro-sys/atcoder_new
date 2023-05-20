n = int(input())
s = input()
x,y = 0,0
count = 0
for i in s:
  if i=="R":
    count+=1
  elif count%4==0:
    x+=1
  elif count%4==1:
    y-=1
  elif count%4==2:
    x-=1
  else:
    y+=1
print(x,y)