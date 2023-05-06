s = input()
if s.upper()==s or s.lower()==s or len(s)!=len(set(s)):
  print("No")
else:
  print("Yes")