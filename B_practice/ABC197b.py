h,w,x,y = map(int,input().split())
li = [input() for _ in range(h)]
# インデックス調整
x -= 1
y -= 1
re = 0
 
# 上
for i in range(1,h):
    if 0<=x-i<h:
        if li[x-i][y]=="#":
            break
        else:
            re+=1
# 下
for i in range(1,h):
    if 0<=x+i<h:
        if li[x+i][y]=="#":
            break
        else:
            re+=1
# 左
for i in range(1,w):
    if 0<=y-i<w:
        if li[x][y-i]=="#":
            break
        else:
            re+=1
# 右
for i in range(1,w):
    if 0<=y+i<w:
        if li[x][y+i]=="#":
            break
        else:
            re+=1
re+=1
print(re)