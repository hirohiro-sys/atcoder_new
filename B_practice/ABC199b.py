#入出力例から推測する
n = int(input())
li = list(map(int,input().split()))
li2 = list(map(int,input().split()))
print(0 if min(li2)<max(li) else min(li2)-max(li)+1)