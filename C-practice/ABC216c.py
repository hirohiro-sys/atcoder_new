'''
まず、操作を逆順に見ていきます。
N が奇数ならば魔法 A の逆操作、
N が偶数ならば魔法 B の逆操作を行うということを繰り返すと、最終的に 
N は 0 になります。
ここで魔法Aの逆操作とは Nから1引くこと操作Bの逆操作とはNを 2で割ることを意味します。
'''

N = int(input())
result = ""
while N>0:
  if N%2==0:
    result = "B"+result
    N = N//2
  else:
    result = "A"+result
    N = N-1
print(result)
