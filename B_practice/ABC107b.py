h,w = map(int,input().split())
li = [input() for _ in range(h)]
tmp = []
tmp2 = []
for i in range(len(li)):
  if "#" in li[i]:
    tmp.append(li[i])
#二次元配列を右に回転    
arr_rotated = [list(x)[::-1] for x in zip(*tmp)]

for i in range(len(arr_rotated)):
  if "#" in arr_rotated[i]:
    tmp2.append(arr_rotated[i])
#二次元配列を左に回転    
arr_rotated2 = [list(x)[::-1] for x in zip(*tmp2[::-1])]

for i in range(len(arr_rotated2),0,-1):
  print(*arr_rotated2[i-1],sep="")