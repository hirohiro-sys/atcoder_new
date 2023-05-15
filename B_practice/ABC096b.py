a,b,c = map(int,input().split())
k = int(input())
print(max(a*2**k+b+c,  a+b*2**k+c,  a+b+c*2**k))