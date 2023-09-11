from collections import Counter

n = int(input())
A = list(map(int,input().split()))

count = Counter(A)
#異なる要素のペアの数は N * (N - 1)
#ペアが2回ずつ数えられるため実際の値が異なるペアを求めるため2でわる
ans = n * (n -1) // 2

for i in count.values():
  ans -= i * (i - 1) // 2

print(ans)
