n,m = map(int,input().split())
s = list(input())
s[n-1:m] = reversed(s[n-1:m])
print(*s,sep="")