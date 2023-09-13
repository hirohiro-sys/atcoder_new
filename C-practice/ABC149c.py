# 素数判定ライブラリ
from sympy import isprime

x = int(input())

while True:
  if isprime(x):
    exit(print(x))
  
  x += 1
