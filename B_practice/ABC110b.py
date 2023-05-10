#問題文そのまま実装
n,m,x,y = map(int,input().split())
li1 = list(map(int,input().split()))
li2 = list(map(int,input().split()))
print("No War" if max(x,li1) < min(y,li2) else "War")