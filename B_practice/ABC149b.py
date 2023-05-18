#TLEが出る時は反復文を使わずにしたり、計算量をなるべく減らす
a,b,k = map(int,input().split())
print(max(0,a-k),max(0,b-max(0,k-a)))