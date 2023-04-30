a,b,c = map(int,input().split())
"""
もしcが偶数なら -の値がプラスになるから値を最初から絶対値で+にしてから条件分岐.
cが奇数ならどのみち-になるからそのまま条件分岐.
"""
if c%2==0:                
  a = abs(a)
  b = abs(b)

if a>b:
  print(">")
elif a<b:
  print("<")
else:
  print("=")