h,w = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(h)]
ans = "Yes"
for i in range(h-1):
  for j in range(w-1):
    #問題文をちゃんと理解する
    if li[i][j]+li[i+1][j+1]>li[i][j+1]+li[i+1][j]:
      ans = "No"
      break
print(ans)