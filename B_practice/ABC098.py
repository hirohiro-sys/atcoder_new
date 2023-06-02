n = int(input())
s = input()
tmp = []
for i in range(n):
  tmp.append(len(set(s[:i]) & set(s[i:])))
print(max(tmp))