while True:
    a,b = map(int,input().spilt())
    if a==0 and b==0:
        break
    print(min(a,b), max(a,b))