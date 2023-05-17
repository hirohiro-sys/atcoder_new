#AGCTが連続している文字列の最大の長さを求める
string = input()
answer = 0
count = 0
for i in string:
  if i in "AGCT":
    count += 1
    answer = max(answer, count)
  else:
    count = 0
print(answer)  