n = int(input())
s = list(input())
even_or_odd = True
for i in range(n):
    if even_or_odd and s[i]==",":
        s[i] = "."
    #""の中の,なのか判別
    if s[i]=='"':
        even_or_odd = not even_or_odd
print("".join(s))
