n,q = map(int,input().split())
li = [0] * n
for i in range(q):
    l,r,t = map(int,input().split())
    for j in range(l-1,r):
        li[j] = t
for i in li:
    print(i)
