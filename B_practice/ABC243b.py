n = int(input())
li1 = list(map(int,input().split()))
li2 = list(map(int,input().split()))
count1 = 0
count2 = 0
for i in range(n):
  if li1[i]==li2[i]:
    count1+=1
for i in range(n):
  if li1[i]!=li2[i] and li1[i] in li2:
    count2+=1
print(count1)
print(count2)