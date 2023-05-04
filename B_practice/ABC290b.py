n,k = map(int,input().split())
s = input()
count = 0
s2 = ""
for i in s:
  s2+=i
  if i=="o":
    count+=1
    if count==k:
      print("".join(s2)+((len(s)-len(s2))*"x"))
      exit()