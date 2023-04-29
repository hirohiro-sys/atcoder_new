n = int(input())
li = [2,1]
for i in range(n-1):
  li.append(li[i]+li[i+1])
print(li[-1])