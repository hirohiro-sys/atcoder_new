#問題文ちゃんと読んでそのまま実装
n = int(input())
k = int(input())
re = 1
for i in range(n):
   re = min(re*2,re+k)
print(re)