from itertools import combinations
n = int(input())
G = [list(map(int,input().split())) for _  in range(n)]
for a,b,c in combinations(range(n),3):
    # 3点が同一直線上にあるかどうかを判定する式
    if (G[b][0]-G[c][0])*(G[a][1]-G[b][1]) == (G[a][0]-G[b][0])*(G[b][1]-G[c][1]):
        exit(print("Yes"))
print("No")
