n,q = map(int,input().split())
s = input()
count = 0
for i in range(q):
  a,b = map(int,input().split())
  if a==1:
    count += b
  else:
    print(s[(b-count-1)%n])

"""
modの法則
"""
