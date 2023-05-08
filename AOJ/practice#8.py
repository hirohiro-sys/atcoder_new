w,h,x,y,r = map(int,input().split())
if x>=r and w-r>=x and y>=r and h-r>=y:
    print("Yes")
else:
    print("No")