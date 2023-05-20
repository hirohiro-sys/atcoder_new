#最頻値を求めることができるモジュール
from statistics import mode
n = int(input())
li = [input() for _ in range(n)]
most_frequent_value = mode(li)
print(most_frequent_value) 