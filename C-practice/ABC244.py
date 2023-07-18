# 入力
n=int(input())
s={i for i in range(1,2*n+2)}

# シミュレーション
while len(s)>0:
    print(s.pop())
    m=int(input())
    s.remove(m)
