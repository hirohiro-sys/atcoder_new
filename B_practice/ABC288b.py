#入出力例よく見る
a,b = map(int,input().split())
li = [input() for _ in range(b)]
li.sort()
for i in range(b):
  print(li[i])