li = [input() for _ in range(10)]
tmp = []
tmp2 = []
for i in range(10):
  if "#" in li[i]:
    tmp.append(i+1)
    tmp2.append(li[i])
print(tmp[0], tmp[-1])
print(tmp2[0].find("#")+1, tmp2[-1].rfind("#")+1)