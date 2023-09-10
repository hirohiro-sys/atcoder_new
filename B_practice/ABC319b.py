n = int(input())

ans = ''
for i in range(n+1):
  ans += '-'
  for j in range(1,10):
    if n%j==0 and i%(n//j)==0:
      ans = ans[:i] + str(j) + ans[i+1:]
      break

print(ans)

'''
問題文通り実装
'''
