n = int(input())
li = set()
for i in range(1,int(n**0.5)+1):
  if n%i==0:
    li.add(i)
    li.add(n//i)

for i in sorted(li):
  print(i)

'''
約数全列挙問題
'''
