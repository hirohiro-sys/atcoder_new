#浮動小数展の計算は誤差を招くこともあるため割り算しないで条件式を立てる
n,x = map(int,input().split())
sm = 0
for i in range(n):
  a,b = map(int,input().split())
  sm += a*b
  if sm > x*100:
    exit(print(i+1))
print(-1)