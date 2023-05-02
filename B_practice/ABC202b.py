s = input()
re = ""
for i in s:
  if i=="0":
    re+="0"
  elif i=="1":
    re+="1"
  elif i=="6":
    re+="9"
  elif i=="8":
    re+="8"
  elif i=="9":
    re+="6"
    
re = re[::-1]
print("".join(re))