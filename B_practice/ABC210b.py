n = int(input())
s = input()
count = 0
for i in s:
  count += 1
  if i=="1":
    if count % 2 == 0:
      print("Aoki")
    else:
      print("Takahashi")
    exit()