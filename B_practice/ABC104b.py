#スライスとメソッドの使い方
s = input()
if s[0]=="A" and s[2:-1].count("C")==1 and s.replace("A","",1).replace("C","",1).islower():
  print("AC")
else:
  print("WA")