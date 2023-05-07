n = int(input())
li = [input() for _ in range(n)]
tmp = ["H","D","C","S"]
tmp2 = ["A" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "T" , "J" , "Q" , "K"]
for i in range(n):
  if li.count(li[i])>=2:
    print("No")
    exit()
    
for i in li:
  if i[0] not in tmp or i[1] not in tmp2:
    print("No")
    exit()

print("Yes")