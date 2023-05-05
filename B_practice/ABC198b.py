s = input()
for _ in range(len(s)):
  if s==s[::-1]:
    print("Yes")
    exit()
  else:
    s = "0"+s
  
print("No")