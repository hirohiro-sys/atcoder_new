N = int(input())
B = list(map(int,input().split()))

ans = 0
ans += B[0]
for i in range(1, N-1):
  ans += min(B[i],B[i-1])
ans += B[N-2]

print(ans)

'''
問題文の式を読み替えて解く
'''
