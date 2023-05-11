#問題文の条件以外の条件も汲み取る必要あり
s = input()
#値が数値なのか文字なのか判定するメソッド
if len(s) != 8 or s[0].isdigit() or s[7].isdigit():
  print("No")
#すべての文字が10進数の数字かどうか判定するメソッド
elif not s[1:7].isdecimal() or s[1] == '0':
  print("No")
else:
  print("Yes")