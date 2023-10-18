n = int(input())
s = [input() for _ in range(n)]
for i in range(n):
    # 入出力結果みながら実装するとわかりやすい
    for j in range(n-1,-1,-1):
        print(s[j][i],end="")
    print()
