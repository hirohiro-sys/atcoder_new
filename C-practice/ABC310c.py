N = int(input())
t = set()
for _ in range(N):
    S = input()
    t.add(min(S, S[::-1]))
print(len(t))

'''
C問題で計算量で悩んだらset()を使えるかどうか考える
'''
