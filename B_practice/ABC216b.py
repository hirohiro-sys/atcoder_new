n = int(input())
li = [input() for _ in range(n)]
if n>len(set(li)):
  print("Yes")
else:
  print("No")