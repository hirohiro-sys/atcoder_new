n = int(input())
li = list(map(int,input().split()))
li.sort()

li = li[n:]
for _ in range(n):
  li.pop()
  
  
print(sum(li)/len(li))