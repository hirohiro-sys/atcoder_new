n = int(input())
re = 0
for i in range(n):
  a,b = input().split()
  if b=="JPY":
    re+=float(a)
     
#1.0 BTC あたり380000.0 円
  else:
    re+=float(a)*380000.0
print(re)