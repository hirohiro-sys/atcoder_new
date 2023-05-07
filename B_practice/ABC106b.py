num = int(input())
re = 0
for i in range(1,num+1,2):
  count = 0
  for j in range(1,i+1):
    if i % j == 0:
      count += 1
  if count == 8:
    re += 1
print(re)