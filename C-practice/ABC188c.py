#シミュレーションしないで解く
N = int(input())
A = list(map(int,input().split()))
A1 = A[:2**(N-1)]
A2 = A[2**(N-1):]
A_max = [max(A1), max(A2)]
print(A.index(min(A_max))+1)
