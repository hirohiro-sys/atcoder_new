s = input()
max_length = 0

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):  # jをi + 1から始めて部分文字列を考える
        if s[i:j] == s[i:j][::-1]:  # 部分文字列が回文かどうかをチェック
            max_length = max(max_length, len(s[i:j]))

print(max_length)
