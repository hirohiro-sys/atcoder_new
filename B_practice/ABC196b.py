x = input()
re = ""
for i in x:
  if i==".":
    break
  re+=i
  
print("".join(re))