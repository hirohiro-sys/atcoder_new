num = int(input())
li = list(map(int,input().split()))
count = 0
while num > 1:
  num = li[num-2]
  count+=1
print(count)