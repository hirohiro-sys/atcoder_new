a,b = map(int,input().split())
li = []
are = ""
bre = ""
a = str(a)
b = str(b)
for i in range(int(b)):
   are+=a
for i in range(int(a)):
   bre+=b
li.append(are)
li.append(bre)
li = sorted(li)
print(li[0])