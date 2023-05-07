s = input()
for i in range(len(s)):
  if (i+1)%2!=0 and s[i].isupper():
    exit(print("No"))
  elif (i+1)%2==0 and s[i].islower():
    exit(print("No"))
print("Yes")