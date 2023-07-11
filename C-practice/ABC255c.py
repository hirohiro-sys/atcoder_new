X, A, D, N = map(int, input().split())

if D == 0:
    print(abs(X - A))
    exit()

first = A
last = A + D * (N - 1)

if D < 0:
    first, last = last, first
    D *= -1

if X <= first:
    print(first - X)
elif X >= last:
    print(X - last)
else:
    ans = D

    #大きい方へ
    num = X
    while True:
        if (num - A) % D == 0:
            ans = min(ans, num - X)
            break
        else:
            num += 1
    #小さい方へ
    num = X
    while True:
        if (num - A) % D == 0:
            ans = min(ans, X - num)
            break
        else:
            num -= 1
    print(ans)
    
'''
公式解説参照
'''
