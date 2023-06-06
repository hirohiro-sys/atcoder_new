n = int(input())
li = sorted(map(int,input().split()), reverse=True)
print(sum(li[::2])-sum(li[1::2]))