n = int(input())
li = list(map(int,input().split()))
#t逆算で計算式を作る
print(n*(n+1)*2-sum(li))