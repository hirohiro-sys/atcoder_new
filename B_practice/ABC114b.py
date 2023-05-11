n = input()
tmp1 = []
tmp2 = []
for i in range(len(n)-1):
  tmp1.append(n[i:i+3])
  for i in range(len(tmp1)):
    tmp2.append(abs(753-int(tmp1[i])))
print(min(tmp2))