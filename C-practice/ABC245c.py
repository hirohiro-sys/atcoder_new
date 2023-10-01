N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

# 初めの処理をするためにansに値入れとく
ans = set([A[0], B[0]])
for i in range(N-1):
    tmp = set()
    # 問題文通り処理
    for j in ans:
        if abs(A[i+1]-j) <= K:
            tmp.add(A[i+1])
        if abs(B[i+1]-j) <= K:
            tmp.add(B[i+1])
    ans = tmp

print('Yes' if ans else 'No')

'''
貪欲法らしい
'''
