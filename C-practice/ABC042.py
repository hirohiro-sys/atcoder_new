N, K = map(int, input().split())
D = list(input().split())

while True:
    if all(d not in str(N) for d in D):
        print(N)
        break
    N += 1
