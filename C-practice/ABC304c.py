#幅優先探索
from queue import Queue

q = Queue()

n, d = map(int, input().split())

xs , ys = [], []

for _ in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

q.put(0)
visit = [0] * n
visit[0] = 1

while q.qsize():
    j = q.get()
    for i in range(n):
        if visit[i]:
            continue
        if (xs[i]-xs[j])**2+(ys[i]-ys[j])**2> d * d:
            continue
        q.put(i)
        visit[i] = 1

for ok in visit:
    print('Yes' if ok else 'No')
