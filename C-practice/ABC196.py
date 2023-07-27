n = int(input())
for i in range(1,1000001):
  if int(str(i)*2) > n:
    exit(print(i-1))
    
'''
制約からnが10の12乗までだからその半分の1000000くらいまでの反復でよい
'''
