s = input()
sm = 0
for i in s:
  sm+=int(i)
if int(s)%sm==0:
  print("Yes")
else:
  print("No")