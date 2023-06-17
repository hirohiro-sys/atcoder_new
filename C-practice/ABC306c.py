# 1~nまでの空配列に入力した配列を回していき先に２になったものから出力していく
# どうやったらsortを使わずに実装できるか考える
n = int(input())
li = list(map(int,input().split()))
tmp = [0 for _ in range(n+1)]
ans = []
for i in li:
  tmp[i]+=1
  if tmp[i]==2:
    ans.append(i)
print(*ans)
