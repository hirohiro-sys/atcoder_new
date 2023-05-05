li = [input() for _ in range(3)]
t = input()
re = ""
for i in t:
  if i=="1":
    re+=li[0]
  elif i=="2":
    re+=li[1]
  else:
    re+=li[2]
print("".join(re))