n,m = map(int,input().split())
li = [input() for _ in range(n)]
count = 0
for i in range(n):
  for j in range(i+1,n):
    #for~elseはforの処理が全部終わったらelseを処理するからforでbreakされたらelseは処理されない
    for s,t in zip(li[i],li[j]):
      if s=="x" and t=="x":
        break
    else:
      count+=1
print(count)