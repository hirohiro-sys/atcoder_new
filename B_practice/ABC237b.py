n,m = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(n)]
for i in range(m):
    for j in range(n):
        print(li[j][0+i],end=" ")
    print()