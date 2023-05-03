n = int(input())
a, b = input().split()
re = ""
for i in range(n):
  re+=a[i]
  re+=b[i]
print("".join(re))