n = int(input())
s = input()
re_str = ""
for i in range(n-1):
  if s[i]==s[i+1]:
    continue
  else:
    re_str += s[i]
print(len(re_str)+1)
