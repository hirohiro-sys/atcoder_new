n = int(input())
A = list(map(int,input().split()))
count = 0
for i in range(n-1):
  if A[i]>A[i+1]:
    count+=A[i]-A[i+1]
    A[i+1] = A[i]
print(count)



'''
初めに提出したコード。whileがあることによりTLE。
n = int(input())
A = list(map(int,input().split()))
count = 0
for i in range(n-1):
  if A[i]>A[i+1]:
    while A[i]>A[i+1]:
      A[i+1]+=1
      count+=1
print(count)
'''
