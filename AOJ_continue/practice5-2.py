while True:
    a,b = map(int,input().split())
    if a==0 and b==0:
        break
    print("#"*b)
    for i in range(a-2):
        print("#","."*(b-2),"#",sep="")
    print("#"*b)
    print()