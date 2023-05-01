n = int(input())
li = [input() for _ in range(n)]
for i in range(n):
  for j in range(n):
    #制約からもしi==jならその処理をスキップする。
    if i==j:
      continue
    if li[i][j]=="W":
      if li[j][i]!="L":
        print("incorrect")
        exit()
    elif li[i][j]=="L":
      if li[j][i]!="W":
        print("incorrect")
        exit()
    elif li[i][j]=="D":
      if li[j][i]!="D":
        print("incorrect")
        exit()
print("correct")