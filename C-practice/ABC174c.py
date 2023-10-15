K = int(input())
seven = 7
for i in range(K):
  if seven%K: seven = (10*seven+7)%K
  else: exit(print(i+1))
print(-1)
