#それぞれのインデックスを求めて横の差と縦の差を求めればいける気がする
h,w = map(int,input().split())
li = [input() for _ in range(h)]
tmp = []
for i in range(h):
  for j in range(w):
    if li[i][j]=="o":
      tmp.append(i)
      tmp.append(j)
      
print(abs(tmp[2]-tmp[0])+abs(tmp[3]-tmp[1]))