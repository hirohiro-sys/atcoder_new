n,k = map(int,input().split())
a = set(map(int,input().split()))

for i in range(k):
    if not i in a:
        print(i)
        break
else:
    print(i+1)
