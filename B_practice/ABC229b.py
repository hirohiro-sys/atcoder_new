a,b = list(input().split())
a = a[::-1]
b = b[::-1]
for i in range(len(a)):
  if int(a[i])+int(b[i])>9:
    print("Hard")
    exit()
print("Easy")