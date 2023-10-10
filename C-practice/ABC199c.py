n = int(input())
s = input()
q = int(input())

x = [[],[]]
x[0] = list(s[:n])
x[1] = list(s[n:])

for _ in range(q):
    t,a,b = map(int,input().split())
    a -= 1
    b -= 1
    if t==1:
        x[a//n][a%n],x[b//n][b%n] = x[b//n][b%n],x[a//n][a%n]
    if t==2:
        x[0],x[1] = x[1],x[0]

ans = "".join(x[0]+x[1])
print(ans)

'''
T==2を高速で処理するのが大事
前半部と後半部で分けることで高速に処理できる
'''
