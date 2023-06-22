n = int(input())
li = list(map(int,input().split()))
count = 0
li.sort()
#print(li)
for i in range(n-1):
  if li[i]==li[i+1]:
    count+=1
    li[i]=0
    li[i+1]=0
print(count)
