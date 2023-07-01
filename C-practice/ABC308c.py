#高精度の数値計算ライブラリ
from decimal import Decimal, getcontext
#演算結果を100桁に指定
getcontext().prec = 100
 
n = int(input())
x = []
for i in range(n):
    a,b = map(Decimal,input().split())
    #-aにしておくことでリストをsortする際に降順でsortされる(らしい)
    x.append((-a/(a+b),i))
 
x.sort()
print(*[i+1 for xx, i in x])
