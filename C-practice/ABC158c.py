'''公式解説
A,Bは100以下である。8%して100なので、税抜き価格は雑にやると100倍くらいになる。
よって、10000以下で全探索すれば答えが存在すれば見つけることができる。
税抜き価格xから消費税を計算する場合は、例えば8%であれば、x0.08をすればいいのだが、
最終的には小数点以下は切り捨てるし、小数を介するのは、誤差とかがちょっと怖い。
なので、x8をして、100で割ることで整数上で正確に切り捨てを計算することができる。

あとは、同じか判定して条件を満たせばxを答える。
ループ抜けたら答えがないので、-1を答える。
'''

a,b = map(int,input().split())
for i in range(1,10001):
  ans1 = i * 8//100
  ans2 = i * 10//100
  
  if ans1==a and ans2==b:
    exit(print(i))
print(-1)