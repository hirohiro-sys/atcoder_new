a,b,c,x = int(input()),int(input()),int(input()),int(input())
count = 0
# 引数に+1するのを忘れない
for i in range(a+1):
  for j in range(b+1):
    for k in range(c+1):
      if 500*i+100*j+50*k==x:
        count += 1
print(count)