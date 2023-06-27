n,m = map(int,input().split())
S = input().split()
#setを使うことで計算量減らセル
T = set(input().split())
for i in S:
  if i in T:
    print("Yes")
  else:
    print("No")
