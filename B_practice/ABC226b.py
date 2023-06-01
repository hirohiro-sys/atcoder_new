n = int(input())
li = [list(map(int,input().split())) for _ in range(n)]
tmp = []
for i in li:
    t = tuple(i)
    tmp.append(t[1:])
print(len(set(tmp)))