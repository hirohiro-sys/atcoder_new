s = input()
li = [0]*6

for i in s:
  if i=="A":
    li[0] += 1
  elif i=="B":
    li[1] += 1
  elif i=="C":
    li[2] += 1
  elif i=="D":
    li[3] += 1
  elif i=="E":
    li[4] += 1
  else:
    li[5] += 1
  
print(*li)
